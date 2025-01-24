import {Injectable, Logger, OnApplicationBootstrap} from "@nestjs/common";
import {InjectRepository} from "@nestjs/typeorm";
import {Between, Repository} from "typeorm";
import {GoogleSheetsService} from "../google-sheets/google-sheets.service";
import {Schedule} from "./entities/schedule.entity";
import {PointsService} from "../points/points.service";


const allMonths = [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
    'Декабрь',
];

const PointAbbreviations = {
    'КР': 'Красота',
    'С': 'Светланская',
    'Ч': 'Чуркин',
    'ЛУГ': 'Луговая',
    'ТИХ': 'Тихая',
    'П': 'Парк',
    'ТОБ': 'Тобольская',
    'Выезд': 'Выездное мероприятие',
};


@Injectable()
export class SchedulesService implements OnApplicationBootstrap {
    constructor(
        @InjectRepository(Schedule)
        private schedulesRepository: Repository<Schedule>,
        private googleSheetsService: GoogleSheetsService,
        private pointsService: PointsService,
    ) {}

    async onApplicationBootstrap() {
        await this.fetchDataFromTablesSchedule(allMonths);
    }


    async fetchDataFromTablesSchedule(months: string[]) {
        const today = new Date();
        for (const month of months) {
            try {
                const spreadsheetId = '1Dipx58MDz-4UcWMncgr3N6NMn8_oUqFk3GaZpENNOXI';

                const monthIndex = allMonths.indexOf(month) + 1;
                const monthDate = monthIndex.toString().padStart(2, '0');
                const year = today.getFullYear();

                const data = await this.googleSheetsService.getSheetData(
                    spreadsheetId,
                    `${month} ${today.toLocaleDateString('ru', { year: '2-digit' })}`
                );

                const nestedArray = [];
                for (const listsData of data) {
                    if (
                        listsData.length !== 0 &&
                        listsData[0] !== '' &&
                        listsData[0].split(' ').length > 1
                    ) {
                        nestedArray.push(listsData);
                    }
                }
                const removeFirstData = nestedArray.slice(1);

                for (const items of removeFirstData) {
                    let index = -2;
                    const name = items[0];
                    for (const item of items) {
                        let day = index + 1;

                        if (index >= 0) {
                            let pointName = '';
                            let endPointName = '';
                            let pointAbbreviation = item.match(/^([А-ЯЁа-яё]+)(?:\s*\((.*?)\))?/);
                            let startTime = '';
                            let endTime = '';

                            if (pointAbbreviation) {
                                const abbreviation = pointAbbreviation[1];
                                if (PointAbbreviations[abbreviation]) {
                                    pointName = PointAbbreviations[abbreviation];
                                    endPointName = PointAbbreviations[abbreviation];

                                    if (pointAbbreviation[2]) {
                                        endPointName += ` (${pointAbbreviation[2]})`;
                                    }

                                    const timeMatch = item.match(/\d{2}:\d{2}\s*-\s*\d{2}:\d{2}/);
                                    if (timeMatch) {
                                        const timeRange = timeMatch[0].split(' - ');
                                        startTime = timeRange[0];
                                        endTime = timeRange[1];
                                    } else {
                                        const point = await this.pointsService.findByName(pointName);
                                        if (point) {
                                            const openingTime = point.opening instanceof Date
                                                ? point.opening
                                                : new Date(`1970-01-01T${point.opening}`);
                                            const closingTime = point.closing instanceof Date
                                                ? point.closing
                                                : new Date(`1970-01-01T${point.closing}`);

                                            startTime = openingTime.toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' });
                                            endTime = closingTime.toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' });
                                        }
                                    }

                                    if (startTime && endTime) {
                                        const scheduleDate = new Date(`${year}-${monthDate}-${day.toString().padStart(2, '0')}`);
                                        const startDateTime = new Date(`${year}-${monthDate}-${day.toString().padStart(2, '0')}T${startTime}`);
                                        const endDateTime = new Date(`${year}-${monthDate}-${day.toString().padStart(2, '0')}T${endTime}`);

                                        const existingSchedule = await this.schedulesRepository.findOne({
                                            where: {
                                                name: name,
                                                date: scheduleDate,
                                                point: endPointName,
                                            },
                                        });

                                        if (existingSchedule) {
                                            existingSchedule.startTime = startDateTime;
                                            existingSchedule.endTime = endDateTime;
                                            await this.schedulesRepository.save(existingSchedule);
                                        } else {
                                            const schedule = new Schedule();
                                            schedule.name = name;
                                            schedule.date = scheduleDate;
                                            schedule.point = endPointName;
                                            schedule.startTime = startDateTime;
                                            schedule.endTime = endDateTime;

                                            await this.schedulesRepository.save(schedule);
                                        }
                                    }
                                }
                            }
                        }
                        index++;
                    }
                }
            } catch (e) {
                Logger.error(e);
            }
        }
    }



}
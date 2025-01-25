import { Injectable, Logger, OnApplicationBootstrap } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Between, FindManyOptions, FindOneOptions, Repository } from 'typeorm';
import { GoogleSheetsService } from '../google-sheets/google-sheets.service';
import { Schedule } from './entities/schedule.entity';
import { PointsService } from '../points/points.service';
import { endOfMonth } from 'date-fns';

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

const columnsNames = [
  'A',
  'B',
  'C',
  'D',
  'E',
  'F',
  'G',
  'H',
  'I',
  'J',
  'K',
  'L',
  'M',
  'N',
  'O',
  'P',
  'Q',
  'R',
  'S',
  'T',
  'U',
  'V',
  'W',
  'X',
  'Y',
  'Z',
  'AA',
  'AB',
  'AC',
  'AD',
  'AE',
  'AF',
  'AG',
];

@Injectable()
export class SchedulesService implements OnApplicationBootstrap {
  constructor(
    @InjectRepository(Schedule)
    private schedulesRepository: Repository<Schedule>,
    private googleSheetsService: GoogleSheetsService,
    private pointsService: PointsService,
  ) {}

  async onApplicationBootstrap() {
    // await this.fetchDataFromTablesSchedule(allMonths);
  }

  async fetchDataFromTablesSchedule(months: string[]) {
    const today = new Date();
    for (const month of months) {
      try {
        const listName = `${month} ${today.toLocaleDateString('ru', { year: '2-digit' })}`;
        const data = await this.googleSheetsService.getSheetData(
          '1Dipx58MDz-4UcWMncgr3N6NMn8_oUqFk3GaZpENNOXI',
          listName,
        );
        const slicedData = data.slice(2);
        for (const line of slicedData) {
          if (line.length > 1) {
            for (let i = 2; i < line.length; i++) {
              const dateArray = data[0][i].split('.');
              const date = new Date(
                `${today.getFullYear()}-${dateArray[1]}-${dateArray[0]}`,
              );
              const pointCodeAndComment = line[i].match(
                /^([А-ЯЁа-яё]+)(?:\s*\((.*?)\))?/,
              );
              if (pointCodeAndComment) {
                const pointCode = pointCodeAndComment[1];
                const point = await this.pointsService.findOne({
                  where: {
                    code: pointCode,
                  },
                });
                const comment = pointCodeAndComment[2];
                const timeMatch = line[i].match(
                  /\d{1,2}:\d{1,2}\s*-\s*\d{1,2}:\d{1,2}/,
                );
                if (point) {
                  let startTime: string;
                  let endTime: string;
                  if (timeMatch) {
                    const timeRange = timeMatch[0].split(' - ');
                    startTime = `${timeRange[0].split(':')[0].padStart(2, '0')}:${timeRange[0].split(':')[1].padStart(2, '0')}`;
                    endTime = `${timeRange[1].split(':')[0].padStart(2, '0')}:${timeRange[1].split(':')[1].padStart(2, '0')}`;
                  } else {
                    startTime = point.opening;
                    endTime = point.closing;
                  }
                  const schedule = await this.schedulesRepository.findOne({
                    where: {
                      date: date,
                      name: line[0],
                    },
                  });
                  if (schedule) {
                    schedule.point = point;
                    schedule.startTime = startTime;
                    schedule.endTime = endTime;
                    schedule.comment = comment;
                    schedule.textFromTable = line[i];
                    await this.schedulesRepository.save(schedule);
                  } else {
                    const newSchedule = new Schedule();
                    newSchedule.name = line[0];
                    newSchedule.point = point;
                    newSchedule.date = date;
                    newSchedule.startTime = startTime;
                    newSchedule.endTime = endTime;
                    newSchedule.comment = comment;
                    newSchedule.cell = `${listName}!${columnsNames[i]}${data.indexOf(line) + 1}`;
                    newSchedule.textFromTable = line[i];
                    await this.schedulesRepository.save(newSchedule);
                  }
                }
              }
            }
          }
        }
      } catch (e) {
        Logger.error(e);
      }
    }
  }

  async findOne(options: FindOneOptions<Schedule>): Promise<Schedule> {
    return await this.schedulesRepository.findOne(options);
  }

  async find(options?: FindManyOptions<Schedule>): Promise<Schedule[]> {
    return await this.schedulesRepository.find(options);
  }
}

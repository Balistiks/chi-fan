import { Injectable, Logger, OnApplicationBootstrap } from '@nestjs/common';
import { GoogleSheetsService } from '../google-sheets/google-sheets.service';
import { InjectRepository } from '@nestjs/typeorm';
import { Salary } from './entities/salary.entity';
import {FindManyOptions, FindOneOptions, Repository} from 'typeorm';
import { NamesService } from '../names/names.service';
import { Name } from '../names/entities/name.entity';
import { AdjustmentsService } from '../adjustments/adjustments.service';
import { Adjustment } from '../adjustments/entities/adjustment.entity';

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

@Injectable()
export class SalariesService implements OnApplicationBootstrap {
  constructor(
    @InjectRepository(Salary)
    private salaryRepository: Repository<Salary>,
    private readonly googleSheetsService: GoogleSheetsService,
    private readonly namesService: NamesService,
    private readonly adjustmentsService: AdjustmentsService,
  ) {}

  async onApplicationBootstrap() {
    // await this.fetchDataFromTables(allMonths);
  }

  async saveName(name: string) {
    const nameObj = await this.namesService.findOne({ where: { name } });
    if (nameObj != null) {
      nameObj.name = name;
      await this.namesService.save(nameObj);
    } else {
      const newName = new Name();
      newName.name = name;
      await this.namesService.save(newName);
    }
  }

  async saveAdjustment(month: string, data: any[], index: number, line: any[]) {
    if (index == 17 || index == 39) {
      const monthIndex = allMonths.indexOf(month);
      const period = data[0][index].split(' ')[1];
      const tableIndex = `${data.indexOf(line)}${index}`;
      let comment: string;
      let offZp: number;
      let fines: number;
      let awards: number;
      let advance: number;
      if (index == 17) {
        comment = line[18] ?? '';
        offZp = (line[19] != null || line[19] != undefined) && line[19] != '' ? line[19] : 0;
        fines = (line[20] != null || line[20] != undefined) && line[20] != '' ? line[20] : 0;
        awards = (line[21] != null || line[21] != undefined) && line[21] != '' ? line[21] : 0;
      } else if (index == 39) {
        comment = line[40] ?? '';
        offZp = (line[41] != null || line[41] != undefined) && line[41] != '' ? line[41] : 0;
        advance = (line[42] != null || line[42] != undefined) && line[42] != '' ? line[42] : 0;
        awards = (line[43] != null || line[43] != undefined) && line[43] != '' ? line[43] : 0;
      }
      const adjustment = await this.adjustmentsService.findOne({
        where: {
          monthIndex,
          period,
          tableIndex,
        },
      });
      if (adjustment != null) {
        adjustment.employeeName = line[1];
        adjustment.pointName = line[0];
        adjustment.comment = comment;
        adjustment.offZp = offZp;
        adjustment.fines = fines;
        adjustment.awards = awards;
        adjustment.advance = advance;
        await this.adjustmentsService.save(adjustment);
      } else {
        const newAdjustment = new Adjustment();
        newAdjustment.employeeName = line[1];
        newAdjustment.pointName = line[0];
        newAdjustment.monthIndex = monthIndex;
        newAdjustment.period = period;
        newAdjustment.comment = comment;
        newAdjustment.offZp = offZp;
        newAdjustment.fines = fines;
        newAdjustment.awards = awards;
        newAdjustment.tableIndex = tableIndex;
        newAdjustment.advance = advance;
        await this.adjustmentsService.save(newAdjustment);
      }
    }
  }

  async fetchDataFromTables(months: string[]) {
    const today = new Date();
    for (const month of months) {
      try {
        const data = await this.googleSheetsService.getSheetData(
          '1e6mtbH2xuXWK1deWG29YoNt8qzGO_qz4kAqO4_wEVWs',
          `${month} ${today.toLocaleDateString('ru', { year: '2-digit' })}`,
        );
        const slicedData = data.slice(5);
        for (const line of slicedData) {
          if (
            line.length != 0 &&
            !line[0].startsWith('Итого') &&
            line[0] != ''
          ) {
            await this.saveName(line[1]);
            for (let i = 2; i <= 44; i++) {
              if ((i < 17 || i > 22) && i < 39) {
                if (
                  line[i] != '' &&
                  line[i] != 0 &&
                  line[i] != '0' &&
                  (line[i] != undefined || line[i] != null)
                ) {
                  const dateArray = data[1][i].split('.');
                  const date = new Date(
                    `${today.getFullYear()}-${dateArray[1]}-${dateArray[0]}`,
                  );
                  const salary = await this.salaryRepository.findOne({
                    where: {
                      date,
                      pointName: line[0],
                      employeeName: line[1],
                    },
                  });
                  if (salary != null) {
                    salary.sum = line[i];
                    await this.salaryRepository.save(salary);
                  } else {
                    const newSalary = new Salary();
                    newSalary.pointName = line[0];
                    newSalary.employeeName = line[1];
                    newSalary.date = date;
                    newSalary.sum = line[i];
                    await this.salaryRepository.save(newSalary);
                  }
                }
              } else {
                await this.saveAdjustment(month, data, i, line);
              }
            }
          }
        }
      } catch (e) {
        Logger.error(e);
      }
    }
  }

  async findAll(options: FindManyOptions<Salary>): Promise<Salary[]> {
    return await this.salaryRepository.find(options);
  }

  async findOne(options: FindOneOptions<Salary>): Promise<Salary> {
    return await this.salaryRepository.findOne(options);
  }
}

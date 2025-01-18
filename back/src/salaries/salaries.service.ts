import { Injectable, Logger, OnApplicationBootstrap } from '@nestjs/common';
import { GoogleSheetsService } from '../google-sheets/google-sheets.service';
import { InjectRepository } from '@nestjs/typeorm';
import { Salary } from './entities/salary.entity';
import {FindManyOptions, FindOneOptions, Repository} from 'typeorm';

const months = [
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
  ) {}

  async onApplicationBootstrap() {
    const today = new Date();
    for (const month of months) {
      try {
        const data = await this.googleSheetsService.getSheetData(
          '1Z2fjnG3PZpg41jeKy1f3hQforJ7iTm9HP2JcAr6IzxE',
          `${month} ${today.toLocaleDateString('ru', { year: '2-digit' })}`,
        );
        const slicedData = data.slice(5);
        for (const line of slicedData) {
          if (
            line.length != 0 &&
            !line[0].startsWith('Итого') &&
            line[0] != ''
          ) {
            for (let i = 2; i <= 44; i++) {
              if ((i < 17 || i > 22) && i < 39) {
                if (line[i] != '') {
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

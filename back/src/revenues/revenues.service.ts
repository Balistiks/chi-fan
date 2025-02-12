import { Injectable, OnApplicationBootstrap } from '@nestjs/common';
import { GoogleSheetsService } from '../google-sheets/google-sheets.service';
import { PointsService } from '../points/points.service';
import { FindManyOptions, FindOneOptions, Repository } from "typeorm";
import { Revenue } from './entities/revenue.entity';
import { InjectRepository } from '@nestjs/typeorm';

@Injectable()
export class RevenuesService implements OnApplicationBootstrap {
  constructor(
    @InjectRepository(Revenue)
    private revenueRepository: Repository<Revenue>,
    private readonly googleSheetsService: GoogleSheetsService,
    private readonly pointsService: PointsService,
  ) {}

  async onApplicationBootstrap() {
    // await this.fetchDataFromTable();
  }

  async fetchDataFromTable() {
    const data = await this.googleSheetsService.getSheetData(
      '1EyXADWIjOFeYpPRxXD_UD51ZcIH0zvHE2m1e_oJc6Nw',
      'Аналитика',
    );
    const slicedData = data.slice(1);
    for (const line of slicedData) {
      if (line[0] != 'Итого по точке') {
        const dateArray = line[0].split('.');
        const date = new Date(dateArray[2], +dateArray[1] - 1, dateArray[0]);
        for (let i = 1; i < data[0].length - 2; i++) {
          if (data[0][i] != 'итого') {
            if (line[i] != '' && (line[i] != null || line[i] != undefined)) {
              const point = await this.pointsService.findOne({
                where: {
                  name: data[0][i],
                },
              });
              const revenue = await this.revenueRepository.findOne({
                where: {
                  point,
                  date,
                },
              });
              const amount = line[i].replace(/\s+/g, '').replace('₽', '');
              if (revenue != null) {
                revenue.amount = amount;
                await this.revenueRepository.save(revenue);
              } else {
                const newRevenue = new Revenue();
                newRevenue.point = point;
                newRevenue.date = date;
                newRevenue.amount = amount;
                await this.revenueRepository.save(newRevenue);
              }
            }
          }
        }
      }
    }
  }


  async getAll(options: FindManyOptions<Revenue>): Promise<Revenue[]> {
    return await this.revenueRepository.find(options);
  }

  async findOne(options: FindOneOptions<Revenue>): Promise<Revenue> {
    return await this.revenueRepository.findOne(options);
  }
}

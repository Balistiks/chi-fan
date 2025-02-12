import { Controller, Get, Param, Patch } from '@nestjs/common';
import { SalariesService } from './salaries.service';
import { Salary } from './entities/salary.entity';
import { endOfMonth, isWithinInterval, startOfMonth } from 'date-fns';
import { Between, FindOptionsWhere } from 'typeorm';

@Controller('salaries')
export class SalariesController {
  constructor(private readonly salariesService: SalariesService) {}

  @Get('months/:employeeName')
  async getMonthsSalaries(@Param('employeeName') employeeName: string) {
    const salaries = await this.salariesService.findAll({
      where: {
        employeeName,
      },
    });

    const salariesWithMonths = salaries.map((item) => {
      return {
        sum: item.sum,
        month: new Date(item.date).toLocaleDateString('ru', { month: 'long' }),
      };
    });
    return salariesWithMonths.reduce((r, a) => {
      r[a.month] = r[a.month] || [];
      r[a.month].push(a);
      return r;
    }, Object.create(null));
  }

  @Get('points/:month/:employeeName')
  async getPointsName(
    @Param('month') month: number,
    @Param('employeeName') employeeName: string,
  ): Promise<string[]> {
    const now = new Date();
    const startDate = startOfMonth(new Date(now.getFullYear(), month - 1, 1));
    const endDate = endOfMonth(startDate);

    const where: FindOptionsWhere<Salary> = {
      employeeName: employeeName,
      date: Between(startDate, endDate),
    };

    const salaries = (
      await this.salariesService.findAll({
        where,
        order: {
          date: 'ASC',
        },
      })
    ).map((salary) => salary.pointName);

    return Array.from(new Set(salaries));
  }

   @Get(':employeeName/:month')
    async findSalary(
        @Param('employeeName') employeeName: string,
        @Param('month') month: number,
    ): Promise<Salary[]> {
        const now = new Date();
        const startDate = startOfMonth(new Date(now.getFullYear(), month - 1, 1));
        const endDate = endOfMonth(startDate);

        const where: FindOptionsWhere<Salary> = {
            employeeName: employeeName,
            date: Between(startDate, endDate),
        };

        return await this.salariesService.findAll({
            where,
            order: {
              date: 'ASC',
            },
        });
    }


    @Get('sum/:namePoint/:employeeName/:month')
    async findSalarySum(
        @Param('namePoint') namePoint: string,
        @Param('employeeName') employeeName: string,
        @Param('month') month: number,
    ): Promise<{ sum1: number, sum2: number }> {
        const now = new Date();
        const startDate = startOfMonth(new Date(now.getFullYear(), month - 1, 1));
        const endDate = endOfMonth(startDate);
         const where: FindOptionsWhere<Salary> = {
              pointName: namePoint,
              employeeName: employeeName,
              date: Between(startDate, endDate)
          };
        const salaries = await this.salariesService.findAll({
            where,
            order: {
              date: 'ASC',
            },
        });
      let sum1 = 0;
      let sum2 = 0;

        const midMonth = new Date(startDate);
        midMonth.setDate(15)

        if(salaries && salaries.length > 0) {
             for (const salary of salaries) {
                if (isWithinInterval(salary.date, { start: startDate, end: midMonth })) {
                    sum1 += salary.sum;
                  }
                 else {
                     sum2 += salary.sum;
                   }
             }
        }



        return { sum1, sum2 };
    }


  @Get(':id')
  async getById(@Param('id') id: number): Promise<Salary> {
      return await this.salariesService.findOne({
          where: {
              id: id
          }
      })
  }

  @Patch(':month')
  async update(@Param('month') month: string) {
    await this.salariesService.fetchDataFromTables([month]);
  }
}

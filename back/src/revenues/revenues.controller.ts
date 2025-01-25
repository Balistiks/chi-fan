import { Controller, Get, Param } from "@nestjs/common";
import { RevenuesService } from './revenues.service';
import { Revenue } from './entities/revenue.entity';
import { Between } from "typeorm";

@Controller('revenues')
export class RevenuesController {
  constructor(private readonly revenuesService: RevenuesService) {}

  @Get('all')
  async getAllPoints(): Promise<Revenue[]> {
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth();
    const firstDayOfMonth = new Date(currentYear, currentMonth, 1);
    const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);


    return await this.revenuesService.getAll({
      relations: ['point'],
      where: {
        date: Between(firstDayOfMonth, lastDayOfMonth)
      }
    });
  }


  @Get(':pointId')
  async getByDays(@Param('pointId') pointId: number): Promise<Revenue[]> {
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth();
    const firstDayOfMonth = new Date(currentYear, currentMonth, 1);
    const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);

    return await this.revenuesService.getAll({
      relations: ['point'],
      where: {
        point: {
          id: pointId,
        },
        date: Between(firstDayOfMonth, lastDayOfMonth)
      },
      order: {
        date: 'ASC',
      },
    });
  }


  @Get('amount/:id')
  async getOne(@Param('id') id: number): Promise<Revenue> {
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth(); 
    const firstDayOfMonth = new Date(currentYear, currentMonth, 1);
    const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);
    return await this.revenuesService.findOne({
      where: {
        id: id,
        date: Between(firstDayOfMonth, lastDayOfMonth)
      },
      relations: ['point'],
    });
  }

}

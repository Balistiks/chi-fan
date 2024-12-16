import { Controller, Get, Param } from '@nestjs/common';
import { ShiftsService } from './shifts.service';
import { Shift } from './entities/shift.entity';
import { Between } from 'typeorm';
import { endOfMonth } from 'date-fns';

@Controller('shifts')
export class ShiftsController {
  constructor(private readonly shiftsService: ShiftsService) {}

  @Get(':year/:month')
  async getByYearAndMonth(
    @Param('year') year: number,
    @Param('month') month: number,
  ): Promise<Shift[]> {
    const date = new Date(year, month - 1, 0);
    return await this.shiftsService.find({
      where: {
        date: Between(date, endOfMonth(date)),
      },
    });
  }
}

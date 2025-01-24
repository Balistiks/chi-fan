import { Controller, Get, Param } from "@nestjs/common";
import { RevenuesService } from './revenues.service';
import { Revenue } from './entities/revenue.entity';

@Controller('revenues')
export class RevenuesController {
  constructor(private readonly revenuesService: RevenuesService) {}

  @Get('all')
  async getAllPoints(): Promise<Revenue[]> {
    return await this.revenuesService.getAll({
      relations: ['point'],
    });
  }

  @Get(':pointId')
  async getByDays(@Param('pointId') pointId: number): Promise<Revenue[]> {
    return await this.revenuesService.getAll({
      relations: ['point'],
      where: {
        point: {
          id: pointId,
        },
      },
      order: {
        date: 'ASC',
      },
    });
  }

  @Get('amount/:id')
  async getOne(@Param('id') id: number): Promise<Revenue> {
    return await this.revenuesService.findOne({
      where: {
        id: id,
      },
      relations: ['point'],
    });
  }
}

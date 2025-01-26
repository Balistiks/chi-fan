import { Controller, Get, Param } from '@nestjs/common';
import {PointsService} from "./points.service";
import {Point} from "./entities/point.entity";

@Controller('points')
export class PointsController {
  constructor(private readonly pointsService: PointsService) {}

  @Get('names')
  async getNames(): Promise<Point[]> {
    return await this.pointsService.getAll({
      select: { name: true },
      where: { cashReportUsage: true },
    });
  }

  @Get('all')
  async getPoints(): Promise<Point[]> {
    return await this.pointsService.getAll({
      relations: ['users', 'users.role', 'schedules'],
    });
  }

  @Get(':name')
  async getByName(@Param('name') name: string): Promise<Point> {
    return await this.pointsService.findOne({ where: { name } });
  }
}

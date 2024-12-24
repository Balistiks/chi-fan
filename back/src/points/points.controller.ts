import { Controller, Get, Param } from '@nestjs/common';
import {PointsService} from "./points.service";
import {Point} from "./entities/point.entity";

@Controller('points')
export class PointsController {
  constructor(private readonly pointsService: PointsService) {}

  @Get('all')
  async getPoints(): Promise<Point[]> {
    return await this.pointsService.getAll({
      relations: ['user', 'user.role'],
    });
  }
}

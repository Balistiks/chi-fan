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

  @Get(':id/:month')
  async getById(
      @Param('id') id: number,
      @Param('month') month: number,
  ): Promise<Point> {
    const point = await this.pointsService.findOne({
      where: { id },
      relations: ['check_lists', 'check_lists.photo'],
    });

    point.check_lists = point.check_lists.filter(checkList =>
        new Date(checkList.createdAt).getMonth() + 1 === month
    );

    return point;
  }

}

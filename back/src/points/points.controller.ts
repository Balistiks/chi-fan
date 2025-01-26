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

  @Get(':id/:month')
  async getById(
      @Param('id') id: number,
      @Param('month') month: number,
  ): Promise<Point> {
    const point = await this.pointsService.findOne({
      where: { id },
      relations: ['check_lists', 'check_lists.check_list_answers', 'check_lists.check_list_answers.photo'],
    });

    point.check_lists = point.check_lists
        .filter(checkList =>
            new Date(checkList.createdAt).getMonth() + 1 === month
        )
        .sort((a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime());

    return point;
  }


  @Get(':name')
  async getByName(@Param('name') name: string): Promise<Point> {
    return await this.pointsService.findOne({ where: { name } });
  }
}

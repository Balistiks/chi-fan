import { Injectable } from '@nestjs/common';
import {InjectRepository} from "@nestjs/typeorm";
import {FindManyOptions, Repository} from "typeorm";
import {Point} from "./entities/point.entity";

@Injectable()
export class PointsService {
    constructor(
        @InjectRepository(Point)
        private pointRepository: Repository<Point>,
    ) {}

    async getAll(options?: FindManyOptions<Point>): Promise<Point[]> {
        return await this.pointRepository.find(options);
  }
}
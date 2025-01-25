import { Module } from '@nestjs/common';
import { SchedulesController } from './schedules.controller';
import {Schedule} from "./entities/schedule.entity";
import {TypeOrmModule} from "@nestjs/typeorm";
import {SchedulesService} from "./schedules.service";
import {GoogleSheetsModule} from "../google-sheets/google-sheets.module";
import {PointsModule} from "../points/points.module";
import { UsersModule } from '../users/users.module';

@Module({
  imports: [
    TypeOrmModule.forFeature([Schedule]),
    GoogleSheetsModule,
    PointsModule,
    UsersModule,
  ],
  controllers: [SchedulesController],
  providers: [SchedulesService],
})
export class SchedulesModule {}

import { Module } from '@nestjs/common';
import { CashReportsController } from './cash-reports.controller';
import {TypeOrmModule} from "@nestjs/typeorm";
import {CashReport} from "./entitties/cash-report.entity";
import {CashReportsService} from "./cash-reports.service";

@Module({
  imports: [TypeOrmModule.forFeature([CashReport])],
  controllers: [CashReportsController],
  providers: [CashReportsService],
})
export class CashReportsModule {}

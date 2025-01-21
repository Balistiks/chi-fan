import { Injectable } from '@nestjs/common';
import {InjectRepository} from "@nestjs/typeorm";
import {FindManyOptions, FindOneOptions, Repository} from "typeorm";
import {CashReport} from "./entitties/cash-report.entity";
import {UpdateCashReportDto} from "./dto/update-cash-report.dto";
import {CreateCashReportDto} from "./dto/create-cash-report.dto";

@Injectable()
export class CashReportsService {
    constructor(
        @InjectRepository(CashReport)
        private cashReportRepository: Repository<CashReport>,
    ) {}

    async findAll(options?: FindManyOptions<CashReport>): Promise<CashReport[]> {
        return await this.cashReportRepository.find(options);
    }

    async save(cashReport?: UpdateCashReportDto | CreateCashReportDto): Promise<CashReport> {
        return await this.cashReportRepository.save(cashReport);
    }

    async find(options: FindOneOptions<CashReport>): Promise<CashReport> {
    return await this.cashReportRepository.findOne(options);
  }
}
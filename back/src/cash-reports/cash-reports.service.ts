import { Injectable } from '@nestjs/common';
import {InjectRepository} from "@nestjs/typeorm";
import {FindManyOptions, Repository} from "typeorm";
import {CashReport} from "./entitties/cash-report.entity";
import {UpdateCashReportDto} from "./dto/update-cash-report.dto";

@Injectable()
export class CashReportsService {
    constructor(
        @InjectRepository(CashReport)
        private cashReportRepository: Repository<CashReport>,
    ) {}

    async findAll(options?: FindManyOptions<CashReport>): Promise<CashReport[]> {
        return await this.cashReportRepository.find(options);
    }

    async save(cashReport: UpdateCashReportDto): Promise<CashReport> {
        return await this.cashReportRepository.save(cashReport);
    }
}
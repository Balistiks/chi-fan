import {Body, Controller, Get, Patch} from '@nestjs/common';
import {CashReportsService} from "./cash-reports.service";
import {CashReport} from "./entitties/cash-report.entity";
import {UpdateCashReportDto} from "./dto/update-cash-report.dto";

@Controller('cash-reports')
export class CashReportsController {
    constructor(
        private readonly cashReportsService: CashReportsService,
    ) {}

    @Get()
    async getAll(): Promise<CashReport[]> {
        return await this.cashReportsService.findAll()
    }

    @Patch()
    async save(@Body() cashReport: UpdateCashReportDto): Promise<CashReport> {
        return await this.cashReportsService.save(cashReport);
    }
}

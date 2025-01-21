import {Body, Controller, Get, Param, Patch, Post} from '@nestjs/common';
import {CashReportsService} from "./cash-reports.service";
import {CashReport} from "./entitties/cash-report.entity";
import {UpdateCashReportDto} from "./dto/update-cash-report.dto";
import {Between, FindOptionsWhere} from "typeorm";
import {CreateCashReportDto} from "./dto/create-cash-report.dto";

@Controller('cash-reports')
export class CashReportsController {
    private DateTime: any;
    constructor(
        private readonly cashReportsService: CashReportsService,
    ) {}

    @Get()
    async getAll(): Promise<CashReport[]> {
        return await this.cashReportsService.findAll()
    }

    @Post()
    async create(@Body() cashReport: CreateCashReportDto): Promise<CashReport> {
        return await this.cashReportsService.save(cashReport);
    }

    @Patch()
    async save(@Body() cashReport: UpdateCashReportDto): Promise<CashReport> {
        return await this.cashReportsService.save(cashReport);
    }

 @Get(':day/:month/:year/:namePoint')
    async getPointsName(
    @Param('day') day: number,
    @Param('month') month: number,
    @Param('year') year: number,
    @Param('namePoint') namePoint: string,
): Promise<CashReport[]> {
    const startDate = new Date(year, month - 1, day, 0, 0, 0);
    const endDate = new Date(year, month - 1, day, 23, 59, 59, 999);

    return await this.cashReportsService.findAll({
        where: {
            createAt: Between(startDate, endDate),
            point: { name: namePoint }
        },
        relations: ['point']
    });
}}
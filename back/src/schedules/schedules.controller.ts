import {Controller, Get, Param, Patch} from '@nestjs/common';
import {SalariesService} from "../salaries/salaries.service";
import {SchedulesService} from "./schedules.service";

@Controller('schedules')
export class SchedulesController {
    constructor(private readonly schedulesService: SchedulesService) {}

    @Patch(':month')
    async update(@Param('month') month: string) {
        const data = await this.schedulesService.fetchDataFromTablesSchedule([month]);
    }
}

import { Controller, Get, Param, Patch } from '@nestjs/common';
import { SalariesService } from '../salaries/salaries.service';
import { SchedulesService } from './schedules.service';
import { GoogleSheetsService } from '../google-sheets/google-sheets.service';

@Controller('schedules')
export class SchedulesController {
  constructor(
    private readonly schedulesService: SchedulesService,
    private readonly googleSheetsService: GoogleSheetsService,
  ) {}

  @Patch(':firstId/swap/:secondId')
  async swap(
    @Param('firstId') firstId: number,
    @Param('secondId') secondId: number,
  ) {
    const firstSchedule = await this.schedulesService.findOne({
      where: { id: firstId },
    });
    const secondSchedule = await this.schedulesService.findOne({
      where: { id: secondId },
    });
    const firstText = firstSchedule.textFromTable;
    const secondText = secondSchedule.textFromTable;
    await this.googleSheetsService.updateSheetData(
      '1Dipx58MDz-4UcWMncgr3N6NMn8_oUqFk3GaZpENNOXI',
      firstSchedule.cell,
      secondText,
    );
    await this.googleSheetsService.updateSheetData(
      '1Dipx58MDz-4UcWMncgr3N6NMn8_oUqFk3GaZpENNOXI',
      secondSchedule.cell,
      firstText,
    );
    firstSchedule.textFromTable = secondText;
    secondSchedule.textFromTable = firstText;
    await this.schedulesService.fetchDataFromTablesSchedule([
      firstSchedule.cell.split('!')[0],
    ]);
  }

  @Patch(':month')
  async update(@Param('month') month: string) {
    const data = await this.schedulesService.fetchDataFromTablesSchedule([
      month,
    ]);
  }
}

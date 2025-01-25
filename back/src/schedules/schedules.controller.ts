import { Body, Controller, Get, Param, Patch, Post, Query } from "@nestjs/common";
import { SchedulesService } from './schedules.service';
import { GoogleSheetsService } from '../google-sheets/google-sheets.service';
import { Schedule } from './entities/schedule.entity';
import { UsersService } from '../users/users.service';
import { User } from '../users/entities/user.entity';
import { Not } from 'typeorm';

@Controller('schedules')
export class SchedulesController {
  constructor(
    private readonly schedulesService: SchedulesService,
    private readonly googleSheetsService: GoogleSheetsService,
    private readonly usersService: UsersService,
  ) {}

  @Get('swap/:tgId/:date')
  async getForSwap(
    @Param('tgId') tgId: number,
    @Param('date') dateString: string,
  ) {
    const swapUsers = await this.usersService.find({
      where: {
        tgId: Not(tgId),
      },
    });
    const schedules: Schedule[] = [];
    const date = new Date(dateString);
    for (const swapUser of swapUsers) {
      const schedule = await this.schedulesService.findOne({
        where: {
          name: swapUser.name,
          date: date,
        },
        relations: ['point'],
      });
      if (schedule) {
        schedules.push(schedule);
      }
    }
    return schedules;
  }

  @Get()
  async get(
    @Query('tgId') tgId: number,
    @Query('date') dateString: string,
  ): Promise<Schedule[]> {
    let user: User;
    if (tgId) {
      user = await this.usersService.findOne({
        where: { tgId },
      });
    }
    const date = dateString ? new Date(dateString) : null;
    return await this.schedulesService.find({
      where: {
        name: user ? user.name : null,
        date,
      },
      relations: ['point'],
    });
  }

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

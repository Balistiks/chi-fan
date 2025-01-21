import { Module } from '@nestjs/common';
import { SalariesService } from './salaries.service';
import { GoogleSheetsModule } from '../google-sheets/google-sheets.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Salary } from './entities/salary.entity';
import { SalariesController } from './salaries.controller';
import { NamesModule } from '../names/names.module';

@Module({
  imports: [
    TypeOrmModule.forFeature([Salary]),
    GoogleSheetsModule,
    NamesModule,
  ],
  controllers: [SalariesController],
  providers: [SalariesService],
})
export class SalariesModule {}

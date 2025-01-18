import { Module } from '@nestjs/common';
import { SalariesService } from './salaries.service';
import { GoogleSheetsModule } from '../google-sheets/google-sheets.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Salary } from './entities/salary.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([Salary]),
    GoogleSheetsModule
  ],
  controllers: [],
  providers: [SalariesService],
})
export class SalariesModule {}

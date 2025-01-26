import { Module } from '@nestjs/common';
import { RevenuesService } from './revenues.service';
import { GoogleSheetsModule } from '../google-sheets/google-sheets.module';
import { PointsModule } from '../points/points.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Revenue } from './entities/revenue.entity';
import { RevenuesController } from './revenues.controller';

@Module({
  imports: [
    TypeOrmModule.forFeature([Revenue]),
    GoogleSheetsModule,
    PointsModule,
  ],
  providers: [RevenuesService],
  controllers: [RevenuesController],
})
export class RevenuesModule {}

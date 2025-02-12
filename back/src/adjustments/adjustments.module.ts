import { Module } from '@nestjs/common';
import { AdjustmentsService } from './adjustments.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Adjustment } from './entities/adjustment.entity';

@Module({
  imports: [TypeOrmModule.forFeature([Adjustment])],
  providers: [AdjustmentsService],
  exports: [AdjustmentsService],
})
export class AdjustmentsModule {}

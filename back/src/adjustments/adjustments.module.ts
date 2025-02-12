import { Module } from '@nestjs/common';
import { AdjustmentsService } from './adjustments.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Adjustment } from './entities/adjustment.entity';
import { AdjustmentsController } from './adjustments.controller';

@Module({
  imports: [TypeOrmModule.forFeature([Adjustment])],
  providers: [AdjustmentsService],
  exports: [AdjustmentsService],
  controllers: [AdjustmentsController],
})
export class AdjustmentsModule {}

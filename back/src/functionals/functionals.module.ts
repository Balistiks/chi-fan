import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Functional } from './entities/functional.entity';
import { FunctionalsService } from './functionals.service';

@Module({
  imports: [TypeOrmModule.forFeature([Functional])],
  providers: [FunctionalsService],
  exports: [FunctionalsService],
})
export class FunctionalsModule {}

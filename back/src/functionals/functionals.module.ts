import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Functional } from './entities/functional.entity';

@Module({
  imports: [TypeOrmModule.forFeature([Functional])],
})
export class FunctionalsModule {}

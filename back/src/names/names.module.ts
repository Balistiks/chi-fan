import { Module } from '@nestjs/common';
import { NamesService } from './names.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Name } from './entities/name.entity';
import { NamesController } from './names.controller';

@Module({
  imports: [TypeOrmModule.forFeature([Name])],
  providers: [NamesService],
  exports: [NamesService],
  controllers: [NamesController],
})
export class NamesModule {}

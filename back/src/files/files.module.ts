import { Module } from '@nestjs/common';
import { FilesService } from './files.service';
import { FilesController } from './files.controller';
import {TypeOrmModule} from "@nestjs/typeorm";
import {File} from "./entities/file.entity";

@Module({
  imports: [TypeOrmModule.forFeature([File])],
  providers: [FilesService],
  controllers: [FilesController],
  exports: [FilesService, TypeOrmModule],
})
export class FilesModule {}

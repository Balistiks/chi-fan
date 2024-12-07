import { Module } from '@nestjs/common';
import { PhotosController } from './photos.controller';
import { PhotosService } from './photos.service';
import {TypeOrmModule} from "@nestjs/typeorm";
import {Photo} from "./entities/photo.entity";

@Module({
  imports: [TypeOrmModule.forFeature([Photo])],
  controllers: [PhotosController],
  providers: [PhotosService],
  exports: [PhotosService, TypeOrmModule],
})
export class PhotosModule {}
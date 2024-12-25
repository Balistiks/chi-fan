import { Module } from '@nestjs/common';
import { CheckListsController } from './check_lists.controller';
import {TypeOrmModule} from "@nestjs/typeorm";
import {Check_list} from "./entities/check_list.entity";
import {PhotosModule} from "../photos/photos.module";
import {CheckListsService} from "./check_lists.service";

@Module({
  imports: [TypeOrmModule.forFeature([Check_list]), PhotosModule],
  controllers: [CheckListsController],
  providers: [CheckListsService]
})
export class CheckListsModule {}

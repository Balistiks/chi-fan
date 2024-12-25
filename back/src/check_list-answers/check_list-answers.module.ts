import { Module } from '@nestjs/common';
import { CheckListAnswersController } from './check_list-answers.controller';
import {CheckListAnswersService} from "./check_list-answers.service";
import {TypeOrmModule} from "@nestjs/typeorm";
import {Check_listAnswer} from "./entities/check_list-answer.entity";
import {PhotosModule} from "../photos/photos.module";

@Module({
  imports: [TypeOrmModule.forFeature([Check_listAnswer]), PhotosModule],
  controllers: [CheckListAnswersController],
  providers: [CheckListAnswersService],
})
export class CheckListAnswersModule {}

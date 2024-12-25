import {Body, Controller, Get, Param, Post, UploadedFile, UseInterceptors} from '@nestjs/common';
import {CheckListsService} from "./check_lists.service";
import {PhotosService} from "../photos/photos.service";
import {FileInterceptor} from "@nestjs/platform-express";
import {diskStorage} from "multer";
import {CreateCheckListDto} from "./dto/create-chech_list.dto";
import {Check_list} from "./entities/check_list.entity";
import {Photo} from "../photos/entities/photo.entity";

@Controller('check-lists')
export class CheckListsController {
    constructor(
        private readonly checkListsService: CheckListsService
    ) {}

    @Post()
    async create(@Body() check_list: CreateCheckListDto): Promise<Check_list> {
        return await this.checkListsService.save(check_list);
    }

    @Get(':id')
    async findOne(@Param('id') id: number): Promise<Check_list> {
        return await this.checkListsService.findOne(
            {
                where : { id },
                relations: ['check_list_answers', 'check_list_answers.photo']
            }
        )
    }
}

import {Body, Controller, Get, Param, Post, UploadedFile, UseInterceptors} from '@nestjs/common';
import {PhotosService} from "../photos/photos.service";
import {FileInterceptor} from "@nestjs/platform-express";
import {diskStorage} from "multer";
import {Photo} from "../photos/entities/photo.entity";
import {CheckListAnswersService} from "./check_list-answers.service";
import {Check_listAnswer} from "./entities/check_list-answer.entity";
import {CreateCheckListAnswerDto} from "./dto/create-check_list-answer.dto";

@Controller('check-list-answers')
export class CheckListAnswersController {
    constructor(
        private readonly checkListAnswersService: CheckListAnswersService,
        private readonly photosService: PhotosService,
    ) {}

    @Post()
    @UseInterceptors(
        FileInterceptor('photo', {
            limits: {
                fileSize: 50000000,
            },
            storage: diskStorage({
                destination: './files',
                filename(req, file, callback) {
                    const filename = `${file.fieldname}-${Date.now()}.png`;
                    callback(null, filename);
                },
            }),
        }),
    )
    async save(
        @Body() check_list_answer: CreateCheckListAnswerDto,
        @UploadedFile()
            photo: any,
    ): Promise<Check_listAnswer> {
        const newCheckListAnswer = await this.checkListAnswersService.save(check_list_answer);
        if (photo) {
            const newPhoto = new Photo();
            newPhoto.path = photo.filename;
            newPhoto.check_list_answer = newCheckListAnswer;
            await this.photosService.save(newPhoto);
        }
        return newCheckListAnswer;
    }

    @Get(':id')
    async findOne(@Param('id') id: number): Promise<Check_listAnswer> {
        return await this.checkListAnswersService.findOne({
            where: { id },
            relations: ['photo']
        })
    }
}

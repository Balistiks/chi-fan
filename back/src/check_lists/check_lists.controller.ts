import {Body, Controller, Post, UploadedFile, UseInterceptors} from '@nestjs/common';
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
        private readonly checkListsService: CheckListsService,
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
        @Body() check_list: CreateCheckListDto,
        @UploadedFile()
            photo: any,
    ): Promise<Check_list> {
        const newCheckList = await this.checkListsService.save(check_list);
        if (photo) {
            const newPhoto = new Photo();
            newPhoto.path = photo.filename;
            newPhoto.check_list = newCheckList;
            await this.photosService.save(newPhoto);
        }
        return newCheckList;
    }
}

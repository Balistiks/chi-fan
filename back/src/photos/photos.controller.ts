import {Body, Controller, Get, Header, Param, Post, Res, UploadedFile, UseInterceptors} from '@nestjs/common';
import { PhotosService } from './photos.service';
import { join } from 'path';
import { createReadStream } from 'fs';
import { Response } from 'express';


@Controller('photos')
export class PhotosController {
  constructor(private readonly photosService: PhotosService) {}

  @Get(':id')
  @Header('Content-type', 'image/*')
  async serveFile(@Param('id') id: number, @Res() res: Response) {
    const photo = await this.photosService.getFileById(id);
    const fileStream = createReadStream(
      join(process.cwd(), `./files/${photo.path}`),
    );
    res.set({
      'Content-type': 'image/*',
    });
    fileStream.pipe(res);
  }

}
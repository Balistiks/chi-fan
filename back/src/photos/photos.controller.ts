import { Controller, Get, Header, Param, Res } from '@nestjs/common';
import { PhotosService } from './photos.service';
import { join } from 'path';
import { createReadStream } from 'fs';
import { Response } from 'express';

@Controller('photos')
export class PhotosController {
  constructor(private readonly photosService: PhotosService) {}

  @Get(':filename')
  @Header('Content-type', 'image/png')
  async serveFile(@Param('filename') filename: string, @Res() res: Response) {
    const photo = await this.photosService.getFileByName(filename);
    const fileStream = createReadStream(
      join(process.cwd(), `./files/${photo.path}`),
    );
    res.set({
      'Content-type': 'image/png',
    });
    fileStream.pipe(res);
  }
}
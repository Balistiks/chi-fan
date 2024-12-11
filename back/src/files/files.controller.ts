import {Controller, Get, Header, Param, Res} from '@nestjs/common';
import {Response} from "express";
import {createReadStream} from "fs";
import {join} from "path";
import {FilesService} from "./files.service";

@Controller('files')
export class FilesController {
    constructor(private readonly filesService: FilesService) {}

    @Get(':id')
    async serveFile(@Param('id') id: number, @Res() res: Response) {
        const file = await this.filesService.getFileById(id);
        if (!file) {
            res.status(404).send('File not found');
            return;
        }

        const filePath = join(process.cwd(), `./files/${file.path}`);
        const fileStream = createReadStream(filePath);

        fileStream.on('error', () => {
            res.status(500).send('Error reading file');
        });

        fileStream.pipe(res);
    }
}

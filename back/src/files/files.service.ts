import { Injectable } from '@nestjs/common';
import {InjectRepository} from "@nestjs/typeorm";
import {Repository} from "typeorm";
import {File} from "./entities/file.entity";

@Injectable()
export class FilesService {
    constructor(
        @InjectRepository(File)
        private fileRepository: Repository<File>,
    ) {}

    async getFileByName(filename: string): Promise<File | undefined> {
    return this.fileRepository.findOne({ where: { path: filename } });
  }
}

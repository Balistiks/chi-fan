import { Injectable } from '@nestjs/common';
import {InjectRepository} from "@nestjs/typeorm";
import {Repository} from "typeorm";
import {File} from "./entities/file.entity";
import {Photo} from "../photos/entities/photo.entity";

@Injectable()
export class FilesService {
    constructor(
        @InjectRepository(File)
        private fileRepository: Repository<File>,
    ) {}

    async getFileById(id: number): Promise<File> {
    return await this.fileRepository.findOne({ where: { id } });
  }
}

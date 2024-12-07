import { Injectable } from '@nestjs/common';
import {InjectRepository} from "@nestjs/typeorm";
import {Photo} from "./entities/photo.entity";
import {Repository} from "typeorm";

@Injectable()
export class PhotosService {
    constructor(
        @InjectRepository(Photo)
        private photoRepository: Repository<Photo>,
    ) {}

    async getFileByName(filename: string): Promise<Photo> {
        return await this.photoRepository.findOne({ where: { path: filename } });
    }
}
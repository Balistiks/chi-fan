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

    async getFileById(id: number): Promise<Photo> {
    return await this.photoRepository.findOne({ where: { id } });
  }

    async save(photo: Photo): Promise<Photo> {
        return await this.photoRepository.save(photo);
    }

}
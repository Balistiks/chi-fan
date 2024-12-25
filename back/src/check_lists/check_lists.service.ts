import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import {FindOneOptions, Repository} from 'typeorm';
import {Check_list} from "./entities/check_list.entity";
import {CreateCheckListDto} from "./dto/create-chech_list.dto";

@Injectable()
export class CheckListsService {
    constructor(
        @InjectRepository(Check_list)
        private readonly checkListRepository: Repository<Check_list>
    ) {}

    async save(check_list: CreateCheckListDto): Promise<Check_list> {
        return await this.checkListRepository.save(check_list);
    }

    async findOne(options: FindOneOptions<Check_list>): Promise<Check_list> {
        return await this.checkListRepository.findOne(options);
    }
}
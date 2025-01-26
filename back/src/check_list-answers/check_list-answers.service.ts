import { Injectable } from '@nestjs/common';
import {InjectRepository} from "@nestjs/typeorm";
import {DeepPartial, FindManyOptions, FindOneOptions, Repository} from "typeorm";
import {Check_listAnswer} from "./entities/check_list-answer.entity";
import {CreateCheckListAnswerDto} from "./dto/create-check_list-answer.dto";

@Injectable()
export class CheckListAnswersService {
    constructor(
        @InjectRepository(Check_listAnswer)
        private checkListAnswersRepository: Repository<Check_listAnswer>,
    ) {}

    async findOne(options: FindOneOptions<Check_listAnswer>): Promise<Check_listAnswer> {
        return await this.checkListAnswersRepository.findOne(options);
    }

    async save(check_list_answer: CreateCheckListAnswerDto): Promise<Check_listAnswer> {
        return await this.checkListAnswersRepository.save(check_list_answer);
    }
}
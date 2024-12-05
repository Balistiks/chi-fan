import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Topic } from './entities/topic.entity';
import { FindManyOptions, FindOneOptions, Repository } from 'typeorm';

@Injectable()
export class TopicsService {
  constructor(
    @InjectRepository(Topic)
    private topicRepository: Repository<Topic>,
  ) {}

  async find(options?: FindManyOptions<Topic>): Promise<Topic[]> {
    return await this.topicRepository.find(options);
  }

  async findOne(options: FindOneOptions<Topic>): Promise<Topic> {
    return await this.topicRepository.findOne(options);
  }
}

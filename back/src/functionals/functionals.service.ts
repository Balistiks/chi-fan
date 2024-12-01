import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Functional } from './entities/functional.entity';
import { FindOneOptions, Repository } from 'typeorm';

@Injectable()
export class FunctionalsService {
  constructor(
    @InjectRepository(Functional)
    private functionalRepository: Repository<Functional>,
  ) {}

  async findOne(options: FindOneOptions<Functional>): Promise<Functional> {
    return await this.functionalRepository.findOne(options);
  }
}

import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Functional } from './entities/functional.entity';
import { FindManyOptions, Repository } from 'typeorm';

@Injectable()
export class FunctionalsService {
  constructor(
    @InjectRepository(Functional)
    private functionalRepository: Repository<Functional>,
  ) {}

  async findAll(options: FindManyOptions<Functional>): Promise<Functional[]> {
    return await this.functionalRepository.find(options);
  }
}

import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Name } from './entities/name.entity';
import { FindOneOptions, Repository } from 'typeorm';
import { CreateNameDto } from './dto/create-name.dto';

@Injectable()
export class NamesService {
  constructor(
    @InjectRepository(Name)
    private nameRepository: Repository<Name>,
  ) {}

  async findOne(options: FindOneOptions<Name>): Promise<Name> {
    return await this.nameRepository.findOne(options);
  }

  async save(name: CreateNameDto): Promise<Name> {
    return await this.nameRepository.save(name);
  }
}

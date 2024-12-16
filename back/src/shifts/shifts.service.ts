import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Shift } from './entities/shift.entity';
import { FindManyOptions, Repository } from 'typeorm';

@Injectable()
export class ShiftsService {
  constructor(
    @InjectRepository(Shift)
    private shiftRepository: Repository<Shift>,
  ) {}

  async find(options?: FindManyOptions<Shift>): Promise<Shift[]> {
    return await this.shiftRepository.find(options);
  }
}

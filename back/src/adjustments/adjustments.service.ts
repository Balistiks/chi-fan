import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Adjustment } from './entities/adjustment.entity';
import { FindOneOptions, Repository } from 'typeorm';

@Injectable()
export class AdjustmentsService {
  constructor(
    @InjectRepository(Adjustment)
    private adjustmentRepository: Repository<Adjustment>,
  ) {}

  async findOne(options: FindOneOptions<Adjustment>): Promise<Adjustment> {
    return await this.adjustmentRepository.findOne(options);
  }

  async save(adjustment: Adjustment): Promise<Adjustment> {
    return await this.adjustmentRepository.save(adjustment);
  }
}

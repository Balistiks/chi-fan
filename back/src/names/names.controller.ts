import { Controller, Get, Param } from '@nestjs/common';
import { NamesService } from './names.service';
import { Name } from './entities/name.entity';

@Controller('names')
export class NamesController {
  constructor(private readonly namesService: NamesService) {}

  @Get(':name')
  async getByName(@Param('name') name: string): Promise<Name> {
    return await this.namesService.findOne({ where: { name } });
  }
}

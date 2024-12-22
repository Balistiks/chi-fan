import { Controller, Get, Param } from '@nestjs/common';
import { UsersService } from './users.service';
import { Functional } from '../functionals/entities/functional.entity';
import { FunctionalsService } from '../functionals/functionals.service';
import {User} from "./entities/user.entity";

@Controller('users')
export class UsersController {
  constructor(
    private readonly usersService: UsersService,
    private readonly functionalsService: FunctionalsService,
  ) {}

  @Get(':tgId/isExist')
  async isExist(@Param('tgId') tgId: number): Promise<boolean> {
    return (await this.usersService.findOne({ where: { tgId } })) !== null;
  }

  @Get(':tgId/functionals')
  async getFunctionals(@Param('tgId') tgId: number): Promise<Functional[]> {
    return await this.functionalsService.findAll({
      where: { roles: { users: { tgId } } },
      relations: ['roles', 'roles.users'],
    });
  }
}

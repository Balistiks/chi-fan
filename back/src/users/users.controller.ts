import { Body, Controller, Get, Param, Patch, Post } from '@nestjs/common';
import { UsersService } from './users.service';
import { Functional } from '../functionals/entities/functional.entity';
import { FunctionalsService } from '../functionals/functionals.service';
import { User } from './entities/user.entity';
import { CreateUserDto } from './dto/create-user.dto';
import { UpdateUserDto } from "./dto/update-user.dto";

@Controller('users')
export class UsersController {
  constructor(
    private readonly usersService: UsersService,
    private readonly functionalsService: FunctionalsService,
  ) {}

  @Patch(':tgId')
  async update(
    @Param('tgId') tgId: number,
    @Body() userUpdate: UpdateUserDto,
  ): Promise<User> {
    const user = await this.usersService.findOne({ where: { tgId: tgId } });
    user.role = userUpdate.role;
    return await this.usersService.save(user);
  }

  @Post()
  async create(@Body() user: CreateUserDto): Promise<User> {
    return await this.usersService.save(user);
  }

  @Get('byName/:name')
  async getByName(@Param('name') name: string): Promise<User> {
    return await this.usersService.findOne({
      where: { name: name },
    });
  }

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

  @Get(':tgId')
  async getByTgId(@Param('tgId') tgId: number): Promise<User> {
    return await this.usersService.findOne({
      where: { tgId },
      relations: ['point', 'role'],
    });
  }
}

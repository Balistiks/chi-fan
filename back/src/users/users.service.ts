import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from './entities/user.entity';
import {FindManyOptions, FindOneOptions, Repository} from 'typeorm';
import {CreateUserDto} from "./dto/create-user.dto";

@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private userRepository: Repository<User>,
  ) {}

  async findOne(options: FindOneOptions<User>): Promise<User> {
    return await this.userRepository.findOne(options);
  }

  async save(user: CreateUserDto): Promise<User> {
    return await this.userRepository.save(user);
  }
}

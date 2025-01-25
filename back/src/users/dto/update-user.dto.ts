import { IsNotEmpty, IsNumber, IsOptional, IsString } from 'class-validator';
import { PartialType } from '@nestjs/mapped-types';
import { CreateUserDto } from './create-user.dto';
import { Role } from '../../roles/entities/role.entity';
import { Point } from '../../points/entities/point.entity';

export class UpdateUserDto extends PartialType(CreateUserDto) {
  @IsNumber()
  @IsNotEmpty()
  tgId: number;

  @IsOptional()
  role?: Role;

  @IsOptional()
  point?: Point;
}

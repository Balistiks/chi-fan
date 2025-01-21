import {IsNotEmpty, IsNumber, IsOptional, IsString} from 'class-validator';
import {Role} from "../../roles/entities/role.entity";

export class CreateUserDto {
    @IsNumber()
    @IsNotEmpty()
    tgId: number;

    @IsString()
    @IsNotEmpty()
    name: string;

    @IsNotEmpty()
    role: Role;
}
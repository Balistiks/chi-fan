import {IsBoolean, IsDate, IsNotEmpty, isNumber, IsNumber, IsOptional, IsString} from 'class-validator';
import {Point} from "../../points/entities/point.entity";

export class CreateCashReportDto {
    @IsNotEmpty()
    @IsString()
    name: string;

    @IsNotEmpty()
    @IsDate()
    createAt: Date;

    @IsNotEmpty()
    point: Point;
}
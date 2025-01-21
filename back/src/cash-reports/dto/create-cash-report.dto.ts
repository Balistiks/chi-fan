import {IsBoolean, IsNotEmpty, isNumber, IsNumber, IsOptional, IsString} from 'class-validator';
import {Point} from "../../points/entities/point.entity";

export class CreateCashReportDto {
    @IsNotEmpty()
    @IsString()
    name: string;

    @IsNotEmpty()
    point: Point;
}
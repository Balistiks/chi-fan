import { IsDate, IsNotEmpty, IsNumber, IsString } from 'class-validator';
import {Column, ManyToOne} from "typeorm";
import {Point} from "../../points/entities/point.entity";

export class CreateScheduleDto {
    @IsNotEmpty()
    @IsString()
    name: string;

    @IsNotEmpty()
    date: Date;

    @IsNotEmpty()
    point: Point;

    @IsNotEmpty()
    startTime: Date;

    @IsNotEmpty()
    endTime: Date;
}

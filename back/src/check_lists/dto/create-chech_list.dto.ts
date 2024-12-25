import {IsBoolean, IsNotEmpty, IsNumber, IsString} from 'class-validator';
import {Point} from "../../points/entities/point.entity";

export class CreateCheckListDto {
    @IsNotEmpty()
    @IsString()
    name: string;

    @IsNotEmpty()
    point: Point;
}
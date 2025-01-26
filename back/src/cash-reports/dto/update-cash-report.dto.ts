import {IsBoolean, IsNotEmpty, isNumber, IsNumber, IsOptional, IsString} from 'class-validator';

export class UpdateCashReportDto {
    @IsNumber()
    id: number;

    @IsOptional()
    @IsBoolean()
    done: boolean;
}
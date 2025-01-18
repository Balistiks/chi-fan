import { IsDate, IsNotEmpty, IsNumber, IsString } from 'class-validator';

export class CreateSalaryDto {
  @IsNotEmpty()
  @IsString()
  pointName: string;

  @IsNotEmpty()
  @IsString()
  employeeName: string;

  @IsNotEmpty()
  @IsDate()
  date: Date;

  @IsNotEmpty()
  @IsNumber()
  sum: number;
}

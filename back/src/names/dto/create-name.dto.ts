import { IsNotEmpty, IsString } from 'class-validator';

export class CreateNameDto {
  @IsNotEmpty()
  @IsString()
  name: string;
}

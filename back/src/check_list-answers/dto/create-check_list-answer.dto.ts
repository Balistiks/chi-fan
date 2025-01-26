import {IsBoolean, IsNotEmpty, IsNumber, IsString} from 'class-validator';
import {Check_list} from "../../check_lists/entities/check_list.entity";

export class CreateCheckListAnswerDto {
    @IsNotEmpty()
    @IsString()
    text: string;

    @IsNotEmpty()
    @IsBoolean()
    done: boolean;

    @IsNotEmpty()
    check_list: Check_list;
}
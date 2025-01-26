import { IsNotEmpty } from 'class-validator';
import {Check_list} from "../../check_lists/entities/check_list.entity";

export class CreatePhotoDto {
    @IsNotEmpty()
    check_list: Check_list;
}
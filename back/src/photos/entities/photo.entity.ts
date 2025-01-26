import {Column, Entity, ManyToOne, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import {Topic} from "../../topics/entities/topic.entity";
import {Check_list} from "../../check_lists/entities/check_list.entity";
import {Check_listAnswer} from "../../check_list-answers/entities/check_list-answer.entity";

@Entity()
export class Photo {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ nullable: false })
    path: string;

    @ManyToOne(() => Topic, (topic) => topic.photos)
    topic: Topic;

    @OneToOne(() => Check_listAnswer, (check_list_answer) => check_list_answer.photo)
    check_list_answer: Check_listAnswer;
}
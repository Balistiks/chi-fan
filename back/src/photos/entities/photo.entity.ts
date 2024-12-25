import {Column, Entity, ManyToOne, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import {Topic} from "../../topics/entities/topic.entity";
import {Check_list} from "../../check_lists/entities/check_list.entity";

@Entity()
export class Photo {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ nullable: false })
    path: string;

    @ManyToOne(() => Topic, (topic) => topic.photos)
    topic: Topic;

    @OneToOne(() => Check_list, (check_list) => check_list.photo)
    check_list: Check_list;
}
import {
    Column,
    CreateDateColumn,
    Entity,
    JoinColumn,
    ManyToOne,
    OneToMany,
    OneToOne,
    PrimaryGeneratedColumn
} from 'typeorm';
import {Photo} from "../../photos/entities/photo.entity";
import {Point} from "../../points/entities/point.entity";
import {Check_list} from "../../check_lists/entities/check_list.entity";

@Entity()
export class Check_listAnswer {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ nullable: false })
    text: string;

    @Column("boolean", { nullable: false, default: false })
    done: boolean;

    @ManyToOne(() => Check_list, (check_list: Check_list) => check_list.check_list_answers)
    check_list: Check_list;

    @OneToOne(() => Photo, (photo) => photo.check_list_answer)
    @JoinColumn()
    photo: Photo;
}

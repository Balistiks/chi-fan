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
import {Point} from "../../points/entities/point.entity";
import {Check_listAnswer} from "../../check_list-answers/entities/check_list-answer.entity";

@Entity()
export class Check_list {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ nullable: false })
    name: string;

    @CreateDateColumn()
    createdAt: Date;

    @ManyToOne(() => Point, (point: Point) => point.check_lists)
    point: Point;

    @OneToMany(() => Check_listAnswer, (check_listAnswer: Check_listAnswer) => check_listAnswer.check_list)
    check_list_answers: Check_listAnswer[];
}

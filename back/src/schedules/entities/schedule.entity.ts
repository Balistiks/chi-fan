import {Column, Entity, ManyToOne, PrimaryGeneratedColumn} from 'typeorm';
import {Point} from "../../points/entities/point.entity";

@Entity()
export class Schedule {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    name: string;

    @Column('date')
    date: Date;

    @Column()
    point: string;

    @Column('time')
    startTime: Date;

    @Column('time')
    endTime: Date;
}

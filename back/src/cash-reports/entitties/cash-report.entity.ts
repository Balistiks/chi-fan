import {Column, CreateDateColumn, Entity, ManyToOne, PrimaryColumn, PrimaryGeneratedColumn} from 'typeorm';
import {Point} from "../../points/entities/point.entity";

@Entity()
export class CashReport {
    @PrimaryGeneratedColumn()
    id: number;

    @Column('varchar', { nullable: false })
    name: string;

    @CreateDateColumn()
    createAt: Date;

    @Column('boolean', { default: true })
    done: boolean;

    @ManyToOne(() => Point, (point: Point)=> point.cashReport)
    point: Point;
}

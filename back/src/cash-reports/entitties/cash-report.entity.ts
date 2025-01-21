import {Column, Entity, ManyToOne, PrimaryColumn, PrimaryGeneratedColumn} from 'typeorm';

@Entity()
export class CashReport {
    @PrimaryGeneratedColumn()
    id: number;

    @Column('varchar', { nullable: false })
    name: string;

    @Column('varchar', { nullable: false })
    callback: string;

    @Column('boolean', { default: false })
    done: boolean;
}

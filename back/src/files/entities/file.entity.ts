import {Column, Entity, JoinColumn, ManyToOne, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import {Topic} from "../../topics/entities/topic.entity";

@Entity()
export class File {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ nullable: false })
    path: string;

    @OneToOne(() => Topic, (topic) => topic.file)
    topic: Topic;
}
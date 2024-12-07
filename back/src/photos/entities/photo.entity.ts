import {Column, Entity, ManyToOne, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import {Topic} from "../../topics/entities/topic.entity";

@Entity()
export class Photo {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ nullable: false })
    path: string;

    @ManyToOne(() => Topic, (topic) => topic.photos)
    topic: Topic;
}
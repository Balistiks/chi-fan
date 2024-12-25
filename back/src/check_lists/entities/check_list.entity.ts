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

@Entity()
export class Check_list {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ nullable: false })
    name: string;

    @Column("boolean", { nullable: false, default: false })
    done: boolean;

    @CreateDateColumn()
    createdAt: Date;

    @ManyToOne(() => Point, (point: Point) => point.check_lists)
    point: Point;

    @OneToOne(() => Photo, (photo) => photo.check_list)
    @JoinColumn()
    photo: Photo;
}

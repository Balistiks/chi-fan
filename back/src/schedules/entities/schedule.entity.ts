import { Column, Entity, ManyToOne, PrimaryGeneratedColumn } from 'typeorm';
import { Point } from '../../points/entities/point.entity';

@Entity()
export class Schedule {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: false })
  name: string;

  @Column('date', { nullable: false })
  date: Date;

  @Column({ nullable: true })
  comment: string;

  @Column('time', { nullable: false })
  startTime: string;

  @Column('time', { nullable: false })
  endTime: string;

  @Column({ nullable: false })
  cell: string;

  @Column({ nullable: false })
  textFromTable: string;

  @ManyToOne(() => Point, (point: Point) => point.schedules)
  point: Point;
}

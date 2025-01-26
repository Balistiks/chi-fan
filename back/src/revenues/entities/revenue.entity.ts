import { Column, Entity, ManyToOne, PrimaryGeneratedColumn } from 'typeorm';
import { Point } from '../../points/entities/point.entity';

@Entity()
export class Revenue {
  @PrimaryGeneratedColumn()
  id: number;

  @Column('date', { nullable: false })
  date: Date;

  @Column({ nullable: false })
  amount: number;

  @ManyToOne(() => Point, (point: Point) => point.revenues)
  point: Point;
}

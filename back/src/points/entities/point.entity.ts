import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from 'typeorm';
import { Shift } from '../../shifts/entities/shift.entity';

@Entity()
export class Point {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: false })
  name: string;

  @OneToMany(() => Shift, (shift: Shift) => shift.point)
  shifts: Shift[];
}

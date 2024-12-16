import { Column, Entity, ManyToOne, PrimaryGeneratedColumn } from 'typeorm';
import { Employee } from '../../employees/entities/employee.entity';
import { Point } from '../../points/entities/point.entity';

@Entity()
export class Shift {
  @PrimaryGeneratedColumn()
  id: number;

  @Column('date', { nullable: false })
  date: Date;

  @ManyToOne(() => Employee, (employee: Employee) => employee.shifts)
  employee: Employee;

  @ManyToOne(() => Point, (point: Point) => point.shifts)
  point: Point;
}

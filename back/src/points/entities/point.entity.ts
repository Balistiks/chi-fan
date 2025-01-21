import {Column, Entity, ManyToOne, OneToMany, PrimaryGeneratedColumn} from 'typeorm';
import { Shift } from '../../shifts/entities/shift.entity';
import { User } from '../../users/entities/user.entity';
import {CashReport} from "../../cash-reports/entitties/cash-report.entity";

@Entity()
export class Point {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: false })
  name: string;

  @Column({ type: 'time', nullable: false })
  opening: Date;

  @Column({ type: 'time', nullable: false })
  closing: Date;

  @OneToMany(() => Shift, (shift: Shift) => shift.point)
  shifts: Shift[];

  @OneToMany(() => User, (user: User) => user.point)
  users: User[];

  @OneToMany(() => CashReport, (cashReport: CashReport)=> cashReport.point)
  cashReport: CashReport[];
}

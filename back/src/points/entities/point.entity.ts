import {Column, Entity, OneToMany, PrimaryGeneratedColumn} from 'typeorm';
import { Shift } from '../../shifts/entities/shift.entity';
import { User } from '../../users/entities/user.entity';
import {CashReport} from "../../cash-reports/entitties/cash-report.entity";
import { Revenue } from '../../revenues/entities/revenue.entity';
import { Schedule } from '../../schedules/entities/schedule.entity';

@Entity()
export class Point {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: false })
  name: string;

  @Column({ nullable: true })
  code: string;

  @Column({ nullable: false, default: false })
  cashReportUsage: boolean;

  @Column({ type: 'time', nullable: false })
  opening: string;

  @Column({ type: 'time', nullable: false })
  closing: string;

  @OneToMany(() => Shift, (shift: Shift) => shift.point)
  shifts: Shift[];

  @OneToMany(() => User, (user: User) => user.point)
  users: User[];

  @OneToMany(() => CashReport, (cashReport: CashReport) => cashReport.point)
  cashReport: CashReport[];

  @OneToMany(() => Revenue, (revenue: Revenue) => revenue.point)
  revenues: Revenue[];

  @OneToMany(() => Schedule, (schedule: Schedule) => schedule.point)
  schedules: Schedule[];
}

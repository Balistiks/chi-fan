import {Column, Entity, JoinColumn, JoinTable, OneToMany, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import { Shift } from '../../shifts/entities/shift.entity';
import {User} from "../../users/entities/user.entity";
import {Check_list} from "../../check_lists/entities/check_list.entity";

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

  @OneToMany(() => Check_list, (check_list: Check_list) => check_list.point)
  check_lists: Check_list[];

  @OneToOne(() => User, (user: User) => user.point)
  @JoinColumn()
  user: User;
}

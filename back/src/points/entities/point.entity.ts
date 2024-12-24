import {Column, Entity, JoinColumn, JoinTable, OneToMany, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import { Shift } from '../../shifts/entities/shift.entity';
import {User} from "../../users/entities/user.entity";

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

  @OneToOne(() => User, (user: User) => user.point)
  @JoinColumn()
  user: User;
}

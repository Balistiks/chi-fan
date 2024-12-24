import {Column, Entity, ManyToOne, OneToOne, PrimaryColumn} from 'typeorm';
import { Role } from '../../roles/entities/role.entity';
import {Point} from "../../points/entities/point.entity";

@Entity()
export class User {
  @PrimaryColumn('bigint')
  tgId: number;

  @Column({ nullable: false })
  name: string;

  @ManyToOne(() => Role, (role: Role) => role.users)
  role: Role;

  @OneToOne(() => Point, (point: Point) => point.user)
  point: Point;
}

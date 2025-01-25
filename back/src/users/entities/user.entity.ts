import { Column, Entity, ManyToOne, PrimaryColumn } from 'typeorm';
import { Role } from '../../roles/entities/role.entity';
import { Point } from '../../points/entities/point.entity';

@Entity()
export class User {
  @PrimaryColumn('bigint')
  tgId: number;

  @Column()
  name: string;

  @ManyToOne(() => Role, (role: Role) => role.users)
  role: Role;

  @ManyToOne(() => Point, (point: Point) => point.users)
  point: Point;
}

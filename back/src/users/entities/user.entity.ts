import { Column, Entity, ManyToOne, PrimaryColumn } from 'typeorm';
import { Role } from '../../roles/entities/role.entity';

@Entity()
export class User {
  @PrimaryColumn('bigint')
  tgId: number;

  @Column({ nullable: false })
  name: string;

  @ManyToOne(() => Role, (role: Role) => role.users)
  role: Role;
}

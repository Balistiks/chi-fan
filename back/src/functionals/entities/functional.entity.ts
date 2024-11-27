import { Column, Entity, ManyToMany, PrimaryGeneratedColumn } from 'typeorm';
import { Role } from '../../roles/entities/role.entity';

@Entity()
export class Functional {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: false })
  name: string;

  @Column({ nullable: false })
  callbackData: string;

  @ManyToMany(() => Role, (role: Role) => role.functionals)
  roles: Role[];
}

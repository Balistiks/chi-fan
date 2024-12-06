import { Column, Entity, ManyToMany, OneToMany, PrimaryGeneratedColumn, JoinTable } from 'typeorm';
import { User } from '../../users/entities/user.entity';
import { Functional } from '../../functionals/entities/functional.entity';

@Entity()
export class Role {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: false })
  name: string;

  @OneToMany(() => User, (user: User) => user.role)
  users: User[];

  @ManyToMany(() => Functional, (functional: Functional) => functional.roles)
  @JoinTable()
  functionals: Functional[];
}

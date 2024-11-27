import { Column, Entity, ManyToMany, OneToMany, PrimaryGeneratedColumn } from 'typeorm';
import { User } from '../../users/entities/user.entity';
import { Functional } from '../../functionals/entities/functional.entity';
import { JoinTable } from 'typeorm/browser';

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

import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Salary {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: false })
  pointName: string;

  @Column({ nullable: false })
  employeeName: string;

  @Column('date', { nullable: false })
  date: Date;

  @Column({ nullable: false })
  sum: number;
}

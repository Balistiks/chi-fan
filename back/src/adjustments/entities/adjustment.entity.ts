import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Adjustment {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: false })
  employeeName: string;

  @Column({ nullable: false })
  pointName: string;

  @Column({ nullable: false })
  monthIndex: number;

  @Column({ nullable: false })
  period: string;

  @Column({ nullable: true })
  comment: string;

  @Column({ nullable: true })
  offZp: number;

  @Column({ nullable: true })
  fines: number;

  @Column({ nullable: true })
  advance: number;

  @Column({ nullable: true })
  awards: number;

  @Column({ nullable: false })
  tableIndex: string;
}

import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Topic {
  subTopics: Topic[] = null;

  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: false, enum: ['topic, sub-topic'] })
  type: string;

  @Column({ nullable: false })
  name: string;

  @Column({ nullable: false })
  text: string;

  @Column({ nullable: true })
  parentId: number;
}

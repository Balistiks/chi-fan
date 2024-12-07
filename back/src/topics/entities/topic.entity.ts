import {Column, Entity, JoinColumn, OneToMany, OneToOne, PrimaryGeneratedColumn} from 'typeorm';
import {Photo} from "../../photos/entities/photo.entity";
import {File} from "../../files/entities/file.entity";

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

  @OneToMany(() => Photo, (photo) => photo.topic, { cascade: true })
  @JoinColumn()
  photos: Photo[];

  @OneToOne(() => File, (file) => file.topic)
  @JoinColumn()
  file: File;
}

import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './users/users.module';
import { RolesModule } from './roles/roles.module';
import { FunctionalsModule } from './functionals/functionals.module';
import * as process from 'process';
import { Role } from './roles/entities/role.entity';
import { Functional } from './functionals/entities/functional.entity';
import { User } from './users/entities/user.entity';
import { TopicsModule } from './topics/topics.module';
import { Topic } from './topics/entities/topic.entity';
import { PhotosModule } from './photos/photos.module';
import { Photo } from './photos/entities/photo.entity';
import { FilesModule } from './files/files.module';
import { File } from './files/entities/file.entity';

@Module({
  imports: [
    TypeOrmModule.forRootAsync({
      useFactory: async () => {
        return {
          type: 'postgres',
          host: 'db',
          port: 5432,
          username: process.env.POSTGRES_USER,
          password: process.env.POSTGRES_PASSWORD,
          database: process.env.POSTGRES_DB,
          entities: [Role, Functional, User, Topic, Photo, File],
          synchronize: true,
        };
      },
    }),
    AuthModule,
    UsersModule,
    RolesModule,
    FunctionalsModule,
    TopicsModule,
    PhotosModule,
    FilesModule,
  ],
  controllers: [],
  providers: [],
})
export class AppModule {}

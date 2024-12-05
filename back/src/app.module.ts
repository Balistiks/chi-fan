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
          entities: [Role, Functional, User, Topic],
          synchronize: true,
        };
      },
    }),
    AuthModule,
    UsersModule,
    RolesModule,
    FunctionalsModule,
    TopicsModule,
  ],
  controllers: [],
  providers: [],
})
export class AppModule {}

import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './users/users.module';
import { RolesModule } from './roles/roles.module';
import { FunctionalsModule } from './functionals/functionals.module';
import { TopicsModule } from './topics/topics.module';
import { PhotosModule } from './photos/photos.module';
import { FilesModule } from './files/files.module';
import { dataSourceOptions } from '../db/data-source';
import { PointsModule } from './points/points.module';
import { EmployeesModule } from './employees/employees.module';
import { ShiftsModule } from './shifts/shifts.module';
import { CheckListsModule } from './check_lists/check_lists.module';
import { CheckListAnswersModule } from './check_list-answers/check_list-answers.module';

@Module({
  imports: [
    TypeOrmModule.forRootAsync({
      useFactory: async () => {
        return dataSourceOptions;
      },
    }),
    AuthModule,
    UsersModule,
    RolesModule,
    FunctionalsModule,
    TopicsModule,
    PhotosModule,
    FilesModule,
    PointsModule,
    EmployeesModule,
    ShiftsModule,
    CheckListsModule,
    CheckListAnswersModule,
  ],
  controllers: [],
  providers: [],
})
export class AppModule {}

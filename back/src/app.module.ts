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
import { GoogleSheetsModule } from './google-sheets/google-sheets.module';
import { SalariesModule } from './salaries/salaries.module';
// import { AdjustmentsModule } from './adjustments/adjustments.module';
import { NamesModule } from './names/names.module';
import { CashReportsModule } from './cash-reports/cash-reports.module';
import { RevenuesModule } from './revenues/revenues.module';
import { AnalyticsModule } from './analytics/analytics.module';

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
    GoogleSheetsModule,
    SalariesModule,
    NamesModule,
    CashReportsModule,
    RevenuesModule,
    AnalyticsModule,
    // AdjustmentsModule,
  ],
  controllers: [],
  providers: [],
})
export class AppModule {}

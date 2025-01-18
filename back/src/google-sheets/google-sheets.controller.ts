import { Controller, Get } from '@nestjs/common';
import { GoogleSheetsService } from './google-sheets.service';

@Controller('google-sheets')
export class GoogleSheetsController {
  constructor(private readonly googleSheetsService: GoogleSheetsService) {}

  @Get()
  async getData() {
    return await this.googleSheetsService.getSheetData(
      '1Z2fjnG3PZpg41jeKy1f3hQforJ7iTm9HP2JcAr6IzxE',
      'Январь 25',
    );
  }
}

import { Injectable } from '@nestjs/common';
import * as path from 'path';
import * as fs from 'fs';
import { google } from 'googleapis';

@Injectable()
export class GoogleSheetsService {
  private sheets: any;
  private authClient: any;

  constructor() {
    const tokenPath = path.join(process.cwd(), './files/token.json');

    const credentials = JSON.parse(fs.readFileSync(tokenPath, 'utf-8'));
    const { client_email, private_key } = credentials;

    this.authClient = new google.auth.JWT(client_email, null, private_key, [
      'https://www.googleapis.com/auth/spreadsheets',
    ]);
    this.sheets = google.sheets({ version: 'v4', auth: this.authClient });
  }

  async getSheetData(spreadsheetId: string, range: string) {
    const response = await this.sheets.spreadsheets.values.get({
      spreadsheetId,
      range,
    });
    return response.data.values;
  }

  async updateSheetData(spreadsheetId: string, range: string, value: string) {
    return await this.sheets.spreadsheets.values.update({
      spreadsheetId,
      range,
      valueInputOption: 'USER_ENTERED',
      requestBody: { majorDimension: 'ROWS', values: [[value]] },
    });
  }
}

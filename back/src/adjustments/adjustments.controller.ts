import { Controller, Get, Param } from "@nestjs/common";
import { AdjustmentsService } from "./adjustments.service";
import { Adjustment } from "./entities/adjustment.entity";

@Controller('adjustments')
export class AdjustmentsController {
  constructor(private readonly adjustmentsService: AdjustmentsService) {}

  @Get(':pointName/:employeeName/:indexMonth')
  async getByName(@Param('pointName') pointName: string,
                  @Param('employeeName') employeeName: string,
                  @Param('indexMonth') indexMonth: number,
                  ): Promise<Adjustment[]> {
    return await this.adjustmentsService.find({
      where: { employeeName: employeeName, pointName: pointName, monthIndex: indexMonth },
    });
  }
}

import { Controller, Get, Param } from '@nestjs/common';
import { TopicsService } from './topics.service';
import { Topic } from './entities/topic.entity';

@Controller('topics')
export class TopicsController {
  constructor(private readonly topicsService: TopicsService) {}

  @Get('first')
  async getFirst(): Promise<Topic[]> {
    return await this.topicsService.find({
      where: { type: 'topic' },
    });
  }

  @Get(':id')
  async getById(@Param('id') id: number): Promise<Topic> {
    const topic = await this.topicsService.findOne({ where: { id } });
    topic.subTopics = await this.topicsService.find({
      where: { parentId: id },
    });
    return topic;
  }
}

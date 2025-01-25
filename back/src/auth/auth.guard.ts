import {
  CanActivate,
  ExecutionContext,
  Injectable,
  UnauthorizedException,
} from '@nestjs/common';
import { Observable } from 'rxjs';
import * as process from 'process';

@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(
    context: ExecutionContext,
  ): boolean | Promise<boolean> | Observable<boolean> {
    const req = context.switchToHttp().getRequest();
    console.log(req)
    try {
      const authHeader = req.headers.authorization;
      const bearer = authHeader.split(' ')[0];
      const token = authHeader.split(' ')[1];
      console.log(bearer)
      console.log(token)

      if (bearer !== 'Bearer' || !token) {
        throw new UnauthorizedException({ message: 'Ошибка авторизации' });
      }

      if (process.env.SECRET_TOKEN == token) {
        return true;
      }
    } catch (e) {
      throw new UnauthorizedException({ message: 'Ошибка авторизации' });
    }
  }
}

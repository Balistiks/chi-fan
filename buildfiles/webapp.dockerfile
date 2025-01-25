FROM node:20-alpine as build

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn

FROM node:20-alpine as development

ENV TZ='Asia/Vladivostok'

WORKDIR /app

COPY --from=build /app/node_modules ./node_modules

COPY . .

CMD ["yarn", "start"]

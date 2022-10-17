FROM node:16-alpine AS build

ENV NODE_ENV=production

RUN mkdir -p /usr/src/app && chown node:node /usr/src/app
WORKDIR /usr/src/app
USER node

COPY --chown=node:node package*.json ./
RUN npm install --omit=dev
COPY --chown=node:node . .
RUN npm run build


FROM nginx:alpine as deploy

COPY --from=build /usr/src/app/build /usr/share/nginx/html

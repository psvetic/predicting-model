FROM node:18-alpine

WORKDIR /my-app

COPY package.json .
RUN npm install package.json

COPY . ./

EXPOSE 3000

CMD npm run dev

FROM node:16

WORKDIR /front

ENV PATH "/front/node_modules/.bin:$PATH"

COPY frontend/ /front/
RUN npm install

CMD ["npm", "start"]
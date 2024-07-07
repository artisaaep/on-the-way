FROM harbor.pg.innopolis.university/docker-hub-cache/debian:11-slim

RUN apt update && apt install --no-install-recommends -y nginx && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["nginx", "-g", "daemon off;"]

FROM python:3.11-slim as python-base
WORKDIR /on-the-way
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#FROM node:20-slim as node-build
#WORKDIR /on-the-way/web/wront/OnTheWay
#COPY web/wront/OnTheWay/package*.json ./
#RUN npm install
#COPY web/wront/OnTheWay .
#RUN npm run build
#FROM python:3.11-slim
#WORKDIR /on-the-way

COPY --from=python-base /on-the-way /on-the-way
#COPY --from=node-build /on-the-way/web/wront/OnTheWay/build /on-the-way/web/wront/OnTheWay/build

EXPOSE 8000
ENV PYTHONUNBUFFERED=1
CMD ["sh", "-c", "python main.py & python server_main.py"]

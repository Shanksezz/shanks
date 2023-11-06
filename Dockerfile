FROM python:3.11-slim
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo gcc
COPY . .
RUN pip3 install -U -r requirements.txt
CMD ["bash","run.sh"]

# check for use environment variables in the Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY config/dev-requirements.txt config/dev-requirements.txt
COPY app/ .

RUN pip install --no-cache-dir -r config/dev-requirements.txt

EXPOSE 5000

COPY config/docker/start-app.sh /start-app.sh
RUN chmod +x /start-app.sh

ENTRYPOINT ["/start-app.sh"]

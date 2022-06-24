ARG ENV_CONTAINER
FROM $ENV_CONTAINER

WORKDIR /code

COPY requirements.txt /

RUN pip install -r /requirements.txt \
	&& rm -rf /root/.cache

COPY ./ ./

ENV ENVIRONMENT_FILE=".env"

EXPOSE 8085

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "index:server"]
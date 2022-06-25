ARG ENV_CONTAINER
FROM $ENV_CONTAINER
WORKDIR /code

COPY requirements.txt /

RUN pip install -r /requirements.txt \
	&& rm -rf /root/.cache

COPY ./ ./

ENV ENVIRONMENT_FILE=".env"


ENTRYPOINT ["gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:80", "index:server"]
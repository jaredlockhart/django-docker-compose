FROM python:3.5
WORKDIR /app
EXPOSE 7001
COPY ./requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir --disable-pip-version-check
COPY . /app

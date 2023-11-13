# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
#RUN apt-get update
# for mysqlclient
RUN apt-get update && apt-get -y install libssl-dev
#RUN apt-get install -y python3-dev
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# copy entrypoint.sh
#COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
#RUN chmod +x /usr/src/app/entrypoint.sh
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
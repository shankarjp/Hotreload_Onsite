FROM httpd:latest

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update

COPY login.local.conf /etc/apache2/sites-available/login.local.conf
COPY hosts /etc/hosts

FROM ubuntu:20.04

LABEL \
    name="Community Library" \
    author="Paulo Roberto Júnior <paulojrbeserra@gmail.com>" \
    maintainer="Paulo Roberto <paulojrbeserra@gmail.com>" \
    description="Livraria cominitária"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y -qq && \
    apt-get install -y -qq --no-install-recommends \
        vim \
        curl \
        build-essential \
        libssl-dev \
        libffi-dev \
        locales \
        sudo \
        software-properties-common \
        make gcc \
        zlib1g zlib1g-dev

RUN curl -O https://www.python.org/ftp/python/3.8.6/Python-3.8.6.tgz
RUN tar -xvf Python-3.8.6.tgz
WORKDIR /Python-3.8.6
RUN ./configure --enable-optimizations
RUN make altinstall

RUN apt-get install -y -qq --no-install-recommends \
    python3-pip \
    libsasl2-dev \
    libldap2-dev \
    python3-dev \
    libmysqlclient-dev \
    mysql-client \
    default-libmysqlclient-dev \
    apache2 \
    libapache2-mod-security2 \
    libapache2-mod-wsgi-py3

RUN a2enmod wsgi

RUN sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen

ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt:en
ENV LC_ALL pt_BR.UTF-8

RUN rm -rf /etc/localtime
RUN echo "America/Sao_Paulo" > /etc/timezone
RUN ln -s /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

RUN apt remove -y && apt clean apt autoclean apt autoremove -y
RUN mkdir /var/www/libc/
WORKDIR /var/www/libc
COPY ./web/ /var/www/libc/

COPY ./entry-point.sh /

RUN sed -i -e 's/\r$//' /entry-point.sh
RUN chmod u+x /entry-point.sh

COPY ./requirements.txt /tmp
RUN pip3 install --quiet --no-cache-dir -r /tmp/requirements.txt

EXPOSE 80
EXPOSE 8000
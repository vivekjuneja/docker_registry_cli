FROM ubuntu
MAINTAINER vivekjuneja@gmail.com

# Add the application resources URL
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

RUN apt-get update

RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

RUN apt-get install -y python python-dev python-distribute python-pip

WORKDIR /data
COPY * /data/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "browser.py"]



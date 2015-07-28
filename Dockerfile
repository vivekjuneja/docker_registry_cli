FROM python:latest

MAINTAINER vivekjuneja@gmail.com


WORKDIR /data
COPY * /data/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "browser.py"]



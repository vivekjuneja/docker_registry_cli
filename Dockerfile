FROM python:2.7-slim
MAINTAINER vivekjuneja@gmail.com

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY browser.py /usr/src/app/browser.py
CMD [ "python", "./browser.py" ]

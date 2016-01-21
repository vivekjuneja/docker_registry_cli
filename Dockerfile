FROM python:2.7-slim
MAINTAINER vivekjuneja@gmail.com

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org -r requirements.txt

COPY ./ /usr/src/app/
ENTRYPOINT [ "python", "./browser_web.py" ]

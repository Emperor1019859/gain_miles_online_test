FROM python:3.11.7-slim

WORKDIR /src
COPY src/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD src /src

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --reload

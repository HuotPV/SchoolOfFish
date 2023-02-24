FROM python:3.8
VOLUME /app/outputs

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt
COPY . /app 

CMD ["python3", "/app/main.py"]

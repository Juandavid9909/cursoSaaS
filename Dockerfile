FROM python:3.10.0

COPY . /app

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

CMD python app.py
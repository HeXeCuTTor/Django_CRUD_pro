
FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt 

COPY . .

COPY ./.nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 8000

CMD gunicorn stocks_products.wsgi -b 0.0.0.0:8000


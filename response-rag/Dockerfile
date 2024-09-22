FROM python:3.10-slim

WORKDIR /app

EXPOSE 5001

ADD req.txt req.txt

RUN pip install --upgrade pip
RUN pip install -r req.txt

CMD ["python", "app.py"]
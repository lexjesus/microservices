FROM python:3.7.0
RUN pip install --upgrade pip
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python" ,"run.py"]
FROM python:3.7.0
RUN pip install --upgrade pip
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python" ,"run.py"]
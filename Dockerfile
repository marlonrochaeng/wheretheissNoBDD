FROM python:3.7.6 as apiautomation

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "--html=report.html"]

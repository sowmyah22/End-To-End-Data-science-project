FROM python:3.8
COPY . /application
WORKDIR /application
EXPOSE 5000
RUN pip install -r requirements.txt
CMD python application.py
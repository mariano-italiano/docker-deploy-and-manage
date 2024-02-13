FROM python:3.6-alpine
COPY . /app
WORKDIR /app
RUN \
 apk add --no-cache bash && \
 apk add --no-cache postgresql-client 
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM python:3

COPY proxy_service.py /

COPY config.py /

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python", "./proxy_service.py" ]

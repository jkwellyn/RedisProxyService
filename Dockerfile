FROM python:3

ADD proxy_service.py /

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python", "./proxy_service.py" ]
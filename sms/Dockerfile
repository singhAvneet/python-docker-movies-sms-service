FROM python:3.8.1-alpine

ADD sns.py /

RUN pip install boto3
RUN pip install requests

CMD [ "python", "./sns.py" ]




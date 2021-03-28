FROM python:3.9.2-slim
WORKDIR /home/dtlab-chat
COPY *.py /home/dtlab-chat/
COPY requirements.txt /home/dtlab-chat/
RUN pip install -r requirements.txt
CMD python3 server.py
EXPOSE 5000
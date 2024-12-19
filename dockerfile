FROM python:3.9

WORKDIR /app

COPY process_wav.py /app/

ENTRYPOINT ["python", "process_wav.py"]
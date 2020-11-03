FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
EXPOSE 80
CMD ["python", "api.py"]
FROM python:3-alpine
RUN pip install Flask
COPY app.py /
COPY template/ /template/
CMD ["python", "app.py"]
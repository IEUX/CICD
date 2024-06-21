FROM python:3.9-alpine

COPY *.py .
RUN pip install pytest

CMD ["pytest", "-q", "test_maths.py"]



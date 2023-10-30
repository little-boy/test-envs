FROM python:3

WORKDIR /app

COPY . .

CMD ["python", "-m", "unittest", "tests/test_file_viewer.py"]

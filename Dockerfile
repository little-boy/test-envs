FROM python:3

WORKDIR /src/

COPY . .

# /!\ layer caching
RUN pip install --no-cache-dir -r requirements.txt

# Bind 0.0.0.0 to expose to the whole world
CMD [ "uvicorn", "--host", "0.0.0.0", "--app-dir", "./src", "main:app", "--reload" ]

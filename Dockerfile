
FROM python:3


WORKDIR /usr/src/app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

EXPOSE 80
# Specify the command to run your app
CMD ["fastapi", "run", "main.py", "--port", "80"]

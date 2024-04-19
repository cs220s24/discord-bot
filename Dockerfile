FROM amazonlinux

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

COPY app.py .
COPY db.py .
COPY quotes.py .

CMD [".venv/bin/python", "app.py"]
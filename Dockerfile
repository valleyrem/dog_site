FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# SECRET_KEY is required to import settings; the value is not used at build
# time, the real one is injected at runtime.
RUN SECRET_KEY=build-time-placeholder python manage.py collectstatic --noinput \
    && useradd --create-home --uid 10001 app \
    && chown -R app:app /app

# Run as an unprivileged user; the cache dir must stay writable.
USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD python -c "import urllib.request,sys; \
sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/', timeout=4).status == 200 else 1)"

# --max-requests recycles workers (leaks in C libraries, growing heaps);
# --timeout keeps a stuck request from pinning a worker forever.
CMD ["gunicorn", "config.wsgi:application", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "3", \
     "--timeout", "60", \
     "--max-requests", "1000", \
     "--max-requests-jitter", "100", \
     "--access-logfile", "-", \
     "--error-logfile", "-"]

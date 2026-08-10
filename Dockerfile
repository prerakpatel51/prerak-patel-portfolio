FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN groupadd --system portfolio \
    && useradd --system --gid portfolio --home-dir /app portfolio

COPY requirements.txt ./
RUN pip install --no-cache-dir --requirement requirements.txt

COPY --chown=portfolio:portfolio . .

RUN DJANGO_SECRET_KEY=build-only-static-key python manage.py collectstatic --noinput

USER portfolio

EXPOSE 8000

HEALTHCHECK --interval=20s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import os, urllib.request; urllib.request.urlopen('http://127.0.0.1:' + os.environ.get('PORT', '8000') + '/', timeout=3)" || exit 1

CMD ["sh", "-c", "gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --threads 4 --timeout 30 --access-logfile - --error-logfile -"]

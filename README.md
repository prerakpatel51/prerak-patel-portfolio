# Prerak Patel Portfolio

A modern multi-page portfolio built with Python, Django, Bootstrap 5, and custom CSS. It includes seven detailed GitHub case studies, the AMS 2026 conference publication, a professional experience timeline, and a focused repository comparison page.

**Live site:** [prerak-portfolio.up.railway.app](https://prerak-portfolio.up.railway.app/)

Everything runs through Docker. A host Python installation or virtual environment is not required.

## Start locally

```bash
docker compose up --build --detach
```

Open [http://localhost:8000](http://localhost:8000). The container includes Gunicorn, collected static assets, and a health check.

Follow logs or stop the site with:

```bash
docker compose logs --follow web
docker compose down
```

## Validate in Docker

```bash
docker compose run --rm --no-deps web python manage.py check
docker compose run --rm --no-deps web python manage.py test
```

Convenience targets are also available:

```bash
make up
make test
make logs
make down
```

## Configuration

The Compose file supplies local values for:

- `DJANGO_DEBUG`
- `DJANGO_SECRET_KEY`
- `DJANGO_ALLOWED_HOSTS`

Replace the local secret before any public deployment. The portfolio does not require an external database or API key; project content is a curated dataset in `portfolio/views.py`, avoiding live GitHub dependencies at request time.

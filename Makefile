.PHONY: build up down restart logs test check static shell

build:
	docker compose build

up:
	docker compose up --build --detach

down:
	docker compose down --remove-orphans

restart:
	docker compose restart web

logs:
	docker compose logs --follow web

test:
	docker compose run --rm --no-deps web python manage.py test

check:
	docker compose run --rm --no-deps web python manage.py check

static:
	docker compose run --rm --no-deps web python manage.py collectstatic --noinput

shell:
	docker compose run --rm --no-deps web python manage.py shell

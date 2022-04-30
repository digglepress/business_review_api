COMPOSE_ENV:="local.yml"
CONTAINER_NAME:="django"
PYTHON:="venv/bin/python"
MANAGE_PY:="venv/bin/python"
RUN_DJANGO_SVR_CMD:="$(docker-compose) -f $(COMPOSE_ENV) run --rm $(CONTAINER_NAME)"

docker-down:
	@docker-compose -f $(COMPOSE_ENV) down

docker-run-build:
	@docker-compose -f $(COMPOSE_ENV) up  --build

docker-run:
	@docker-compose -f $(COMPOSE_ENV) up

docker-migrations:
	@docker-compose -f $(COMPOSE_ENV) run --rm $(CONTAINER_NAME) python manage.py makemigrations
	@docker-compose -f $(COMPOSE_ENV) run --rm $(CONTAINER_NAME) python manage.py migrate

docker-createsuperuser:
	@docker-compose -f $(COMPOSE_ENV) run --rm $(CONTAINER_NAME) python manage.py createsuperuser

docker-collectstatic:
	@docker-compose -f $(COMPOSE_ENV) run --rm $(CONTAINER_NAME) python manage.py collectstatic --no-input

docker-shell:
	@docker-compose -f $(COMPOSE_ENV) run --rm $(CONTAINER_NAME) python manage.py shell_plus

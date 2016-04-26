build: 
	docker-compose build

up: build
	docker-compose up

dev: build
	docker-compose up -d;docker attach djangodockercompose_app_1

test: build
	docker-compose run app sh -c "pip install coverage flake8 && flake8 . && python /app/manage.py test"

migrate: build
	docker-compose run app python manage.py migrate

shell: build
	docker-compose run app python manage.py shell 

# If a file named ".env" exists in the current directory, include its content in the makefile
# Export all variables defined in the included ".env" file, making them available to the makefile
# Normally is used in a dev environment to simulate gitlab environment variables
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

## Build image
build:
	docker stop ${APP_IDENTIFIER} | true
	docker rm ${APP_IDENTIFIER} | true
	docker rmi ${APP_IDENTIFIER} | true
	docker build -t ${APP_IDENTIFIER} -f ./Dockerfile .

## Build image with no-cache parameter
build-nc:
	docker stop ${APP_IDENTIFIER} | true
	docker rm ${APP_IDENTIFIER} | true
	docker rmi ${APP_IDENTIFIER} | true
	docker build --no-cache -t ${APP_IDENTIFIER} -f ./Dockerfile .

## Run a Docker container in detached mode (-d)
run:
	docker stop ${APP_IDENTIFIER} | true
	docker rm ${APP_IDENTIFIER} | true
	docker run --restart=always -d -i -v "${APP_CONFIG_PATH}":/app/configs -v "${APP_LOG_PATH}":/app/logs -e CONFIG_FILE=${CONFIG_FILE} -t -p ${APP_PORT}:5004 --name="${APP_IDENTIFIER}" ${APP_IDENTIFIER}

## Remove Docker images that are not associated with any containers (dangling images)
clean:
	docker rmi $(docker images -f dangling=true -q)

## This command will stop and then start the $APP_IDENTIFIER container, effectively restarting any processes running inside it
restart:
	docker restart ${APP_IDENTIFIER}

## Format the code using isort and black
format:
	isort --profile black .
	black .

## Check the code formatting using isort and black
check:
	isort -c .
	black --check .

## Run the linter on the code using ruff
lint:
	ruff check .

up: build run

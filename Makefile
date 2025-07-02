################################################################################
## Variables
################################################################################
APPLICATION_NAME ?= python-mcp-server-template
COBERTURA_FILE ?= cobertura.xml

################################################################################
## Commands
################################################################################

.PHONY: init
init:  # Install dependencies
	uv sync --no-cache-dir

.PHONY: run
run:  # Run the app locally
	uv run python -m uvicorn main:app --app-dir ./src

.PHONY: test
test:  # Run tests
	uv run pytest ${ARGS}

.PHONY: coverage-test
coverage-test:  # Run tests with coverage
	uv run pytest --cov=src --cov-report=xml:${COBERTURA_FILE}

.PHONY: integration-test
integration-test:  # Run integration tests
	./test/docker/run-preintegration.sh
	uv run pytest -m integration
	./test/docker/run-postintegration.sh

# Building binary and moving it to target directory
.PHONY: run_local
run_local:  # Build and run the app in Docker
	-docker rmi $(APPLICATION_NAME)
	docker-compose build
	docker-compose up -d

# Kill and remove all internal docker containers running app locally
.PHONY: tear_down_containers
tear_down_containers:  # Stop and remove Docker containers
	echo "Killing docker containers"
	docker-compose kill || echo "No containers to kill"
	echo "Removing docker containers"
	docker-compose rm -f || echo "No containers to remove"

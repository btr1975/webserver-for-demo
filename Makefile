# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.6
#

.PHONY: info build build-container coverage pylint pytest gh-pages build dev-run start-container \
	stop-container remove-container

info:
	@echo "make options"
	@echo "    build               To build a distribution"
	@echo "    build-container     To build a container image"
	@echo "    coverage            To run coverage and display ASCII and output to htmlcov"
	@echo "    dev-run             To run the app"
	@echo "    pylint              To run pylint"
	@echo "    pytest              To run pytest with verbose option"
	@echo "    start-container     To start the container"
	@echo "    stop-container      To stop the container"
	@echo "    remove-container    To remove the container"
	@echo "    gh-pages           To create the GitHub pages"

build:
	@python -m build


build-container:
	@cd containers && podman build --ssh=default --build-arg=build_branch=main -t webserver-for-demo:latest -f Containerfile




coverage:
	@pytest --cov --cov-report=html -vvv

pylint:
	@pylint webserver_for_demo/

pytest:
	@pytest --cov -vvv

dev-run:
	@python -c "from webserver_for_demo import cli;cli()" start -p 8080 -r


gh-pages:
	@rm -rf ./docs/source/code
	@sphinx-apidoc -o ./docs/source/code ./webserver_for_demo
	@sphinx-build ./docs ./docs/gh-pages



start-container:
	@podman run -itd --name webserver-for-demo -p 8080:8080 localhost/webserver-for-demo:latest

stop-container:
	@podman stop webserver-for-demo

remove-container:
	@podman rm webserver-for-demo




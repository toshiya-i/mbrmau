SHELL=/bin/bash
TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
DEV_DEPS="requirements-dev.txt"

test: init
	@echo -e $(TAG)$@$(END)
	flake8
	py.test tests --cov mbrmau --verbose

test-all: uninstall-all test
	@:

init: uninstall-mbrmau
	@echo -e $(TAG)$@$(END)
	pip install --upgrade -r $(DEV_DEPS)
	pip install --upgrade --editable .

uninstall-all: uninstall-mbrmau
	@echo -e $(TAG)$@$(END)
	- pip uninstall --yes -r $(DEV_DEPS) 2>/dev/null

uninstall-mbrmau:
	@echo -e $(TAG)$@$(END)
	- pip uninstall --yes mbrmau 2>/dev/null

.PHONY: run makemigrations migrate update shell test superuser install clean

# Variables to keep commands DRY
PYTHON = python
MANAGE = $(PYTHON) manage.py

# Starts the development server
run:
	$(MANAGE) runserver

# Creates new migrations based on models changes
makemigrations:
	$(MANAGE) makemigrations

# Applies database migrations
migrate:
	$(MANAGE) migrate

# Generates and applies migrations in one step
update: makemigrations migrate

# Opens the interactive Django shell
shell:
	$(MANAGE) shell

# Runs the test suite
test:
	$(MANAGE) test

# Creates a new superuser
superuser:
	$(MANAGE) createsuperuser

# Installs project dependencies
install:
	$(PYTHON) -m pip install -r requirements.txt

# Removes cached python files
clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
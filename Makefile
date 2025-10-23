# =========================
#  Assignment 2 Makefile
#  (UML excluded)
# =========================

# ---- Project Settings ----
PKG := Pigdicegame
PYTHON := python

# If your entrypoint differs, run:  make run RUN_MODULE=YourModule
RUN_MODULE ?= $(PKG).main

.PHONY: install run test coverage lint format doc clean clean-doc

# ---- Dependency setup ----
install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

# ---- Run the program ----
run:
	$(PYTHON) -m $(RUN_MODULE)

# ---- Tests & Coverage (uses unittest, matching your suite) ----
test:
	$(PYTHON) -m unittest discover -s $(PKG) -p "Test*.py" -v

coverage:
	coverage erase
	coverage run -m unittest discover -s $(PKG) -p "Test*.py"
	coverage report -m
	coverage html -d doc/coverage

# ---- Linters & Formatter ----
lint:
	flake8 $(PKG)
	pylint $(PKG)

format:
	black $(PKG)

# ---- Docs (pdoc) ----
# pdoc imports your package; we add PKG to PYTHONPATH so bare imports like "import player" work
# without changing any game files.
ifeq ($(OS),Windows_NT)
  PATHSEP := ;
else
  PATHSEP := :
endif

doc:
	mkdir -p doc/api
	PYTHONPATH="$(PKG)$(PATHSEP)$$PYTHONPATH" pdoc -o doc/api $(PKG)

.PHONY: uml
uml:
	@mkdir -p docs/uml
	@python -m pylint.pyreverse.main -o png -p Pigdicegame -d docs/uml Pigdicegame || ( \
		echo "Graphviz missing, falling back to Mermaid…"; \
		python -m pylint.pyreverse.main -o mmd -p Pigdicegame -d docs/uml Pigdicegame )
	@echo "Done. Check docs/uml/"

# ---- Cleanup ----
clean-doc:
	-rm -rf doc/api
	-rm -rf doc/coverage

clean: clean-doc
	-find . -type d -name "__pycache__" -exec rm -rf {} + 2> NUL || true
	-rm -f .coverage

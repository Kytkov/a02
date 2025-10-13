# ----- config -----
PY=python
PKG=Pigdicegame
TESTPAT=Test*.py

# ----- install development tools -----
install:
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements.txt

# ----- optional convenience targets -----
run:
	$(PY) -m $(PKG).main

test:
	$(PY) -m unittest discover -s $(PKG) -p "$(TESTPAT)" -v

coverage:
	coverage run -m unittest discover -s $(PKG) -p "$(TESTPAT)"
	coverage report -m

lint:
	flake8 $(PKG)
	pylint $(PKG)

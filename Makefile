install:
	cp novaterm-apt-repo $(PREFIX)/bin/novaterm-apt-repo

pypi:
	rm -Rf dist/ build/ novaterm_apt_repo.egg-info/
	python3 setup.py sdist bdist_wheel egg_info
	twine upload dist/*

.PHONY: install pypi

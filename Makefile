publish:
	python setup.py register
	python setup.py sdist bdist_wininst upload

docs-init:
	pip install -r docs/requirements.txt

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"

clean:
	rm -R -f ./build
	rm -R -f ./dist
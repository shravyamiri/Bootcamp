.PHONY: build-docker run-docker build-package publish-package clean

build-docker:
	docker build -t dataflow-framework .

run-docker:
	docker run --rm -p 8000:8000 -v $(PWD)/watch_dir:/app/watch_dir dataflow-framework

build-package:
	python setup.py sdist bdist_wheel

publish-package:
	twine upload dist/*

clean:
	rm -rf dist build *.egg-info

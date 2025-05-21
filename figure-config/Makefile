.PHONY: build run test

build:
	docker build -t figure-caption-system .

run:
	docker run -p 8000:8000 -v $(PWD)/data:/app/data -v $(PWD)/input:/app/input figure-caption-system

test:
	pytest tests/
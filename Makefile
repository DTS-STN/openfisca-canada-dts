clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

build-run-dev:
	docker-compose up --build --detach --force-recreate

test:
	docker exec openfisca_dev openfisca test -c openfisca_canada openfisca_canada/tests

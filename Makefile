clean:
	rm -rf build dist
	sudo find . -name '*.pyc' -exec rm \{\} \;

build-run-dev:
	docker-compose -f docker-compose.yml up --build --detach

docker-start:
	docker-compose start

test:
	docker exec openfisca_dev openfisca test -c openfisca_canada openfisca_canada/tests/individual_income

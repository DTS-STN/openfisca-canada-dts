clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

build-run-dev:
	docker-compose -f docker-compose.yml up --build --detach

test:
	docker exec openfisca_dev openfisca test -c openfisca_canada openfisca_canada/tests


marcoBuild:
  docker build . -t openfisca_canada

marcoRun:
  docker run -it --name openfisca_dev  openfisca_canada:latest

marcoTest: 
  docker exec openfisca_dev openfisca test -c openfisca_canada openfisca_canada/tests/mortgage_deferral


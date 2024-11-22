# todo-app

Start project

dev: rye run dev
prd: rye run prd

test container: docker run -it --rm postgres psql -h host.docker.internal -p 60742 -U test -d test

## Tests

Om de API te testen wordt er gebruik gemaakt van de FastAPI Testclient om de app te mocken. De database wordt gesimuleert via Testcontainers en de data wordt gegenereerd door middel van een factory.
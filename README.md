# be-test-1
Template for backend take home test #1

## Pre-Requisites

1/ You will need to have `docker compose` v2: https://docs.docker.com/compose/install/

2/ You will need to have installed `sqd` cli: https://docs.subsquid.io/squid-cli/installation/#0-install-and-setup-squid-cli

## Development

To start all the services, simply run:

`docker compose up --build`

This will start the following services:

- `anvil`
- `db`
- `api`

`api` depends on `anvil` and `db`


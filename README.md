# be-test-1

Template for backend take home test #1

## Pre-Requisites

1/ You will need to have `docker compose` v2:
https://docs.docker.com/compose/install/

2/ You will need to have installed `sqd` cli:
https://docs.subsquid.io/squid-cli/installation/#0-install-and-setup-squid-cli

3/ `indexer` folder in this repo is a typescript codebase. We recommend you use
node v18.6.0. You can use [`nvm`](https://github.com/nvm-sh/nvm) to manage node
versions. `cd` into this folder and `npm` install deps. It's crucial that you
use `npm`!

4/ `poetry` to manage python dependencies. You can install it here:
https://python-poetry.org/docs/#installation

## Repo Overview

- `indexer` - subsquid boilerplate for your indexing needs
- `api` - your python graphql server boilerplate

To install python dependencies, run `poetry install`. This will create a virtual
environment in `.venv` in current workspace directory. Now you can run
`poetry shell` and it will activate this virtual environment for you. Note, you
will need to use python `^3.11` for this assignment. A neat way to manage
multiple python versions at the same time is with
[`pyenv`](https://github.com/pyenv/pyenv).

## Development

To start all the services, simply run:

`docker compose up --build`

This will start the following services:

- `db`
- `api`

## Notes

You will have noticed that subsquid is serving indexed data via its very own
GraphQL API server. Proxying into it from Python will be considered a fail. You
must write your own Python GraphQL server over postgresql db tables.

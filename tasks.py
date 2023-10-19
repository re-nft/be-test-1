from invoke import task


@task
def start(c):
    # starts api server
    c.run("poetry run strawberry server api.schema")

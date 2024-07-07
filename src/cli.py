import typer
from dotenv import dotenv_values

from factories import create_databricks_client

env_vars = dotenv_values(".env.local")


app = typer.Typer()


@app.command("app:test-dtb-connection")
def app_test_dtb_connection() -> None:
    create_databricks_client()


if __name__ == "__main__":
    app()

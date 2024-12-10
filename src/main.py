from uvicorn import run
from app.builders.app_builder import AppBuilder
from common.database.strategies import DatabaseStrategy
from common.env.env_config import get_env_variables

app_env_variables = get_env_variables().app
db_env_variables = get_env_variables().pg

app = (
    AppBuilder()
    .set_open_api()
    .set_http_logging_middleware()
    .set_exception_handlers()
    .set_router()
    .set_database()
    .build()
)



if __name__ == "__main__":
    run(
        "main:app",
        host=app_env_variables.host,
        port=app_env_variables.port,
        reload=True,
        log_level="debug",
    )

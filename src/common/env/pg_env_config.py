from pydantic import BaseModel, Field


class PgEnvVariables(BaseModel):
    host: str = Field(default="localhost", description="PG host")
    port: int = Field(
        ge=0, default=5432, description="PG Port"
    )
    username: str = Field(default="root", description="PG user")
    password: str = Field(default="example", description="PG password")
    database: str = Field(default="example", description="PG database")

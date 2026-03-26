from dataclasses import dataclass
from enum import Enum


class PackageManager(Enum):
    PIP = "pip"
    UV = "uv"


class Database(Enum):
    NONE = "none"
    SQLITE = "sqlite"
    POSTGRES = "postgres"
    POSTGRES_POOL = "postgres_pool"
    POSTGRES_VECTOR = "postgres_vector"


class Orm(Enum):
    NONE = "none"
    SQLALCHEMY = "sqlalchemy"
    SQLMODEL = "sqlmodel"


class AsyncTask(Enum):
    NONE = "none"
    BACKGROUND = "background"
    CELERY = "celery"
    ARQ = "arq"


@dataclass
class Project:
    project_name: str
    package_manager: PackageManager
    database: Database
    orm: Orm
    async_task: AsyncTask
    rate_limiting: bool
    config: bool
    git: bool
    git_z: bool
    run_install: bool

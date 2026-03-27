import click
import questionary

from create_fastapi_app.models import (
    Database,
    Orm,
    PackageManager,
    Project,
    StructureChoice,
)


def ask_questions() -> Project:
    project_name = questionary.text("What will your project be called ?").unsafe_ask()

    if not project_name:
        project_name = "my_fastapi_app"

    raw_structure: str = questionary.select(
        "Which project structure do you want?",
        choices=[e.value for e in StructureChoice],
    ).unsafe_ask()

    raw_package_manager: str = questionary.select(
        "Which package manager do you want to use ?",
        choices=[e.value for e in PackageManager],
    ).unsafe_ask()

    raw_typing: bool = questionary.confirm(
        "Enable strict typing (type hints)?"
    ).unsafe_ask()

    raw_ruff: bool = questionary.confirm("Use Ruff for linting?").unsafe_ask()

    raw_cors: bool = questionary.confirm(
        "Enable CORS (Cross-Origin Resource Sharing) ?"
    ).unsafe_ask()

    allowed_origins: list[str] = []

    if raw_cors:
        raw_allowed_origins: str = questionary.text(
            "Enter allowed origins (comma-separated, e.g. http://localhost:3000,https://myapp.com)"
        ).unsafe_ask()
        allowed_origins = raw_allowed_origins.split(",")

    raw_database: str = questionary.select(
        "Which database do you want to use ?", choices=[e.value for e in Database]
    ).unsafe_ask()

    if raw_database != "none":
        raw_orm: str = questionary.select(
            "Which ORM do you want to use ?", choices=[e.value for e in Orm]
        ).unsafe_ask()
    else:
        raw_orm = "none"

    rate_limiting: bool = questionary.confirm("Enable rate limiting ?").unsafe_ask()

    config: bool = questionary.confirm(
        "Use environment configuration (.env) ?"
    ).unsafe_ask()

    git: bool = questionary.confirm("Initialize a git repository?").unsafe_ask()

    if git:
        git_z: bool = questionary.confirm("Use Git-z ?").unsafe_ask()
    else:
        git_z = False

    run_install: bool = questionary.confirm(
        "Would you like us to run install ?"
    ).unsafe_ask()

    project_structure = StructureChoice(raw_structure)
    package_manager = PackageManager(raw_package_manager)
    database = Database(raw_database)
    orm = Orm(raw_orm)

    project = Project(
        project_name=project_name,
        project_structure=project_structure,
        package_manager=package_manager,
        use_typing=raw_typing,
        use_ruff=raw_ruff,
        enable_cors=raw_cors,
        allowed_origins=allowed_origins,
        database=database,
        orm=orm,
        rate_limiting=rate_limiting,
        config=config,
        git=git,
        git_z=git_z,
        run_install=run_install,
    )

    return project


def show_summary(project: Project) -> None:
    click.echo()
    click.echo(f"Project : {project.project_name}")
    click.echo(f"Project structure : {project.project_structure.value}")
    click.echo(f"Package Manager : {project.package_manager.value}")
    click.echo(f"Use typing : {'yes' if project.use_typing else 'no'}")
    click.echo(f"Use Ruff : {'yes' if project.use_ruff else 'no'}")
    click.echo(f"Enable CORS : {'yes' if project.enable_cors else 'no'}")
    if project.enable_cors:
        click.echo(f"Allowed origins : {project.allowed_origins}")
    click.echo(f"Database : {project.database.value}")
    click.echo(f"ORM : {project.orm.value}")
    click.echo(f"Enable rate limiting : {'yes' if project.rate_limiting else 'no'}")
    click.echo(f"Use environment configuration : {'yes' if project.config else 'no'}")
    click.echo(f"Initialize a git repository : {'yes' if project.git else 'no'}")
    click.echo(f"Use Git-z : {'yes' if project.git_z else 'no'}")
    click.echo(
        f"Would you like us to run install ? : {'yes' if project.run_install else 'no'}"
    )
    click.echo()

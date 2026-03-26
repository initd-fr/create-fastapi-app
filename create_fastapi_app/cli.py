import os

import click
import questionary
from banner import display_banner
from models import Project
from prompts import ask_questions, show_summary


@click.command()
def main():
    try:
        display_banner()
        while True:
            project = ask_questions()
            show_summary(project)
            if questionary.confirm("Proceed with project setup ?").unsafe_ask():
                break
        # setup_project(project)
    except KeyboardInterrupt:
        click.echo("\nAborted.")


def setup_project(project: Project) -> None:
    directory_name = project.project_name.value

    try:
        os.makedirs(directory_name)
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

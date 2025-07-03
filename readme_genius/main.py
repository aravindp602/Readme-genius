# readme_genius/main.py
import sys
import typer
from rich.console import Console
from rich.markdown import Markdown
from .core import questions, generator

# Create a Typer app
app = typer.Typer(add_completion=False)
console = Console()

@app.command()
def main(
    version: bool = typer.Option(
        None, "--version", "-v", help="Show the application's version and exit."
    )
):
    """
    Generate a professional README.md for your project. ✨
    """
    if version:
        console.print("[bold cyan]Readme-Genius[/bold cyan] version: 0.1.0")
        raise typer.Exit()

    try:
        # 1. Ask questions
        project_data = questions.get_project_info()

        # 2. Generate the LICENSE file
        license_path, license_message = generator.create_license_file(project_data)
        if license_path:
            console.print(f"\n[bold green]✓ {license_message}[/bold green]")
        elif license_message:
            console.print(f"\n[bold red]x {license_message}[/bold red]")

        # 3. Generate the README content
        console.print("\n[bold yellow]Generating your README...[/bold yellow]")
        readme_content = generator.generate_readme(project_data)

        # 4. Save the README file
        file_path = generator.save_readme(readme_content)
        console.print(f"\n[bold green]✓ '{file_path}' has been successfully generated![/bold green]")

        # 5. Print a preview
        console.print("\n--- [bold]Preview[/bold] ---")
        console.print(Markdown(readme_content))
        console.print("--- [bold]End of Preview[/bold] ---\n")

    except (KeyboardInterrupt, EOFError):
        console.print("\n\n[bold red]Operation cancelled by user.[/bold red]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]An unexpected error occurred: {e}[/bold red]")
        sys.exit(1)

# The run function that will be called by the pyproject.toml script
def run():
    app()

if __name__ == "__main__":
    run()
import click
from cli import progress, vocabulary, grammar, exercises

@click.group()
def main():
    pass

@main.command()
@click.option("--name", prompt="Enter your name", help="The user's name")
def start(name):
    click.echo(f"Hi {name}, welcome to the Language Learning CLI Application!")
    click.echo("Please choose an option to continue:")
    click.echo("Press 1 to start learning vocabulary.")
    click.echo("Press 2 to explore grammar rules.")
    click.echo("Press 3 to practice exercises.")
    click.echo("Press 4 to check your progress.")
    click.echo("Press 5 to exit.")

main.add_command(vocabulary)
main.add_command(grammar)
main.add_command(exercises)
main.add_command(progress)

if __name__ == "__main__":
    main()

import click
from cli import progress, vocabulary, translate, synonyms
from user import User

@click.command()
def user():
    click.echo("Press 1 to Register.")
    click.echo("Press 2 to Login.")
    choice = click.prompt("Login or Register if you do not have an account", type=int)

    if choice == 1:
        click.echo("Register")
        click.prompt("Username:", type=str)
        click.prompt("Password:", type=str)
    elif choice == 2:
        click.echo("Login")
        click.prompt("Username:", type=str)
        click.prompt("Password:", type=str)
    else:
        click.echo("Invalid choice. Please choose a valid option.")

@click.command()
@click.option("--name", prompt="Enter your name", help="The user's name")
def main(name):
    click.echo(f"Hi {name}, welcome to the Language Learning CLI Application!")
    click.echo("Please choose an option to continue:")
    click.echo("Press 1 to start learning vocabulary.")
    click.echo("Press 2 to translate words.")
    click.echo("Press 3 to search for synonyms.")
    click.echo("Press 4 to check your progress.")
    click.echo("Press 5 to exit.")
    
    choice = click.prompt("Enter your choice", type=int)
    
    if choice == 1:
        vocabulary()
    elif choice == 2:
        translate()
    elif choice == 3:
        synonyms()
    elif choice == 4:
        progress()
    elif choice == 5:
        click.echo("Exiting...")
    else:
        click.echo("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    user()
    main()

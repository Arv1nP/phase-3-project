import click
from cli import progress, vocabulary, translate, synonyms
from user import UserHandler
from data_structures import create_session, close_session,engine

@click.command()
def user():
    click.echo("Press 1 to Register.")
    click.echo("Press 2 to Login.")
    choice = click.prompt("Login or Register if you do not have an account", type=int)

    session = create_session(engine)
    
    if choice == 1:
        click.echo("Register")
        username = click.prompt("Username:", type=str)
        password = click.prompt("Password:", type=str, hide_input=False)
        if UserHandler.register(session, username, password):
            click.echo("Registration successful!")
    elif choice == 2:
        click.echo("Login")
        username = click.prompt("Username:", type=str)
        password = click.prompt("Password:", type=str, hide_input=False)
        if UserHandler.login(session, username, password):
            click.echo("Login successful!")
        else:
            click.echo("Invalid username or password.")
    else:
        click.echo("Invalid choice. Please choose a valid option.")
    session.close()

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
    # Create session
    session = create_session(engine)
    
    # Call user command
    user()
    
    # Call main command
    main()
    
    # Close session
    close_session(session)

import click
from cli import translate, synonyms, vocabulary, progress
from user import UserHandler
from data_structures import create_session, close_session, engine


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
        if UserHandler(session, username, password).register(): #If returned true then echo following
            click.echo("Registration successful!")
            click.echo("Try and login now.")
            return user() #Return to login menu so they can login
    elif choice == 2:
        click.echo("Login")
        username = click.prompt("Username:", type=str)
        password = click.prompt("Password:", type=str, hide_input=False)
        if UserHandler(session, username, password).login(): #If returned true then main
            click.echo("Login successful!")
            return menu()  
        else:
            click.echo("Invalid username or password. Please try again.")
    else:
        click.echo("Invalid choice. Please choose a valid option.")    

@click.command()
def menu():  
    click.echo("Hi there, welcome to the Language Learning CLI Application!")
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
        close_session(session)
        click.echo("Logging out...")
    else:
        click.echo("Invalid choice. Please choose a valid option.")

    

if __name__ == "__main__":
    # Create session
    session = create_session(engine)
    
    # If user is logged in then
    if user():
      # Call main command
      menu()  

    

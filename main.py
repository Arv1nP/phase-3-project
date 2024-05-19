import click
from user import UserHandler
from data_structures import create_session, close_session, engine
from language_api import Fetch_from_api


@click.command()
def user():
    global session #make global with caution for acess by all function scopes in this module
    global username
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
        if UserHandler(session, username, password).login(): #If returned true then main.py
            click.echo("Login successful!")
            return menu()  
        else:
            click.echo("Invalid username or password. Please try again.")
    else:
        click.echo("Invalid choice. Please choose a valid option.")    

@click.command()
def menu():  
    click.echo(f"Hi {username}, welcome to the Language Learning CLI Application!")
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
        close_session(session) #Close session on logging out
        click.echo("Logging out...")
    else:
        click.echo("Invalid choice. Please choose a valid option.")

@click.group() #group the following functions together and call at once in the main block
def cli():
    pass   

@cli.command()
def vocabulary():
        click.echo("Please choose a language:")
        click.echo("Press 1 for English.")
        click.echo("Press 2 for French.")
        click.echo("Press 3 for Italian.")
        click.echo("Press 4 to go back.")

        choice = click.prompt("Enter your choice", type=int)
        lang = ("en" if choice == 1 else ("fr" if choice == 2 else "it"))
        api = Fetch_from_api(lang)  # Instantiate the Fetch_from_api class with the chosen language

        if choice in [1, 2, 3]:
            vocabulary_data = api.fetch_vocabulary()  # Fetch vocabulary for the chosen language
            update = UserHandler(session, username)
            update.progress(lang)
            click.echo(f"{vocabulary_data}, Now write them down")  # Display the fetched vocabulary data
            
            click.echo("Press 1 to go back.")
            btn = click.prompt("Press 2 to grab some more words", type=int)
            
            if btn == 1:
                 click.echo("Returning back to the main menu...")
                 return menu()
            elif btn ==2:
                vocabulary()
            else: 
                 click.echo("Invalid choice. Please choose a valid option.")

        elif choice == 4:
            click.echo("Returning back...")
            return menu()
        else:
            click.echo("Invalid choice. Please choose a valid option.")


@cli.command()
def translate():
    click.echo("Please choose a language you want to serach from:")
    click.echo("Press 1 for English.")
    click.echo("Press 2 for French.")
    click.echo("Press 3 for Italian.")
    click.echo("Press 4 to go back.")

    choice_from = click.prompt("Enter your choice", type=int)
    if choice_from in [1,2,3]:
        lang_from = "eng" if choice_from == 1 else ("fra" if choice_from == 2 else "ita")
    elif choice_from == 4:
            click.echo("Returning back...")
            return menu()
    else:
        click.echo("Invalid choice. Please choose a valid option.")


    click.echo("Please choose a language you want to serach to:")
    click.echo("Press 1 for English.")
    click.echo("Press 2 for French.")
    click.echo("Press 3 for Italian.")
    click.echo("Press 4 to go back.")

    choice_to = click.prompt("Enter your choice", type=int)
    if choice_to in [1,2,3]:
      lang_to = "eng" if choice_to == 1 else ("fra" if choice_to == 2 else "ita")
      
    elif choice_to == 4:
            click.echo("Returning back...")
            return menu()
    else:
        click.echo("Invalid choice. Please choose a valid option.")

    input = click.prompt("Enter word", type=str).lower() #No longer case sensetive
    api = Fetch_from_api(input) #Call and then passs to class
    response = api.fetch_translation(lang_from,lang_to) #Pass to function
    click.echo(response) #Results
    click.echo("Press 1 to go back.")
    btn = click.prompt("Press 2 to translate some more words", type=int)     
    if btn == 1:
        click.echo("Returning back to the main menu...")
        return menu()
    elif btn ==2:
        translate()
    else: 
        click.echo("Invalid choice. Please choose a valid option.")

    



@cli.command()
def synonyms():
    word = click.prompt("Search up related words", type=str).lower() #No longer case sensetive
    api = Fetch_from_api(word)  #Make new instance of class and pass perameter
    synonym_data = api.fetch_synonyms()  #Call function of that instance
    click.echo(synonym_data)
    click.echo("Press 1 to go back.")
    btn = click.prompt("Press 2 to grab some more synonyms", type=int)     
    if btn == 1:
        click.echo("Returning back to the main menu...")
        return menu()
    elif btn ==2:
        synonyms()
    else: 
        click.echo("Invalid choice. Please choose a valid option")

@cli.command()
def progress():
    click.echo("Here is your progress of English, French and Italian.")
    click.echo("You have learnt this many words from each language")

    progress = UserHandler(session, username)
    user_progress = progress.get_progress()
    click.echo(user_progress)

    

    back_btn = click.prompt("Press 1 to go back.", type=int)
    if back_btn == 1:
        click.echo("Returning back to the main menu...")
        return menu()
    else:
        click.echo("Invalid choice. Please choose a valid option.")

    

if __name__ == "__main__":
    # Create session
    session = create_session(engine)
    
    # If user is logged in then
    if user():
      # Call main command
      menu()
      cli()  

    

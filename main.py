import click
from cli import progress, vocabulary, wordSearch, synonyms

@click.command()
@click.option("--name", prompt="Enter your name", help="The user's name")
def main(name):
    click.echo(f"Hi {name}, welcome to the Language Learning CLI Application!")
    click.echo("Please choose an option to continue:")
    click.echo("Press 1 to start learning vocabulary.")
    click.echo("Press 2 to search for defenitions.")
    click.echo("Press 3 to to search for synonyms.")
    click.echo("Press 4 to check your progress.")
    click.echo("Press 5 to exit.")
    
    choice = click.prompt("Enter your choice", type=int)
    
    if choice == 1:
        vocabulary()
    elif choice == 2:
        wordSearch()
    elif choice == 3:
        synonyms()
    elif choice == 4:
        progress()
    elif choice == 5:
        click.echo("Exiting...")
    else:
        click.echo("Invalid choice. Please choose a valid option.")



if __name__ == "__main__":
    main()

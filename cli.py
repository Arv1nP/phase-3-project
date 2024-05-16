import click
from language_api import Fetch_from_api


@click.group()
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
            click.echo(f"{vocabulary_data}, Now write them down")  # Display the fetched vocabulary data
            print(lang)
        elif choice == 4:
            click.echo("Returning back...")
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
    lang_from = "eng" if choice_from == 1 else ("fra" if choice_from == 2 else "ita")


    click.echo("Please choose a language you want to serach to:")
    click.echo("Press 1 for English.")
    click.echo("Press 2 for French.")
    click.echo("Press 3 for Italian.")
    click.echo("Press 4 to go back.")

    choice_to = click.prompt("Enter your choice", type=int)
    lang_to = "eng" if choice_to == 1 else ("fra" if choice_to == 2 else "ita")

    input = click.prompt("Enter word", type=str).lower()
    api = Fetch_from_api(input)
    response = api.fetch_translation(lang_from,lang_to)
    click.echo(response)


@cli.command()
def synonyms():
    word = click.prompt("Search up related words", type=str)
    api = Fetch_from_api(word)  # You may need to pass the language here
    synonym_data = api.fetch_synonyms()  # Pass the word to the fetch_synonyms method
    click.echo(synonym_data)

@cli.command()
def progress():
    click.echo("")
    click.echo("Please choose a language to check Check progress from: ")
    click.echo("Press 1 for English.")
    click.echo("Press 2 for French.")
    click.echo("Press 3 for Italian.")
    click.echo("Press 4 to go back.")

    choice = click.prompt("Enter your choice", type=int)
    lang = ("en" if choice == 1 else ("fr" if choice == 2 else "it"))

if __name__ == "__main__":
    cli()

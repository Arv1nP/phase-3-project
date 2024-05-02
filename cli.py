import click
from language import Random_word_api

    
@click.command()
def vocabulary():
    click.echo("Please choose a language:")
    click.echo("Press 1 for English.")
    click.echo("Press 2 for French.")
    click.echo("Press 3 for Italian.")
    click.echo("Press 4 to go back.")

    choice = click.prompt("Enter your choice", type=int)
    api = Random_word_api("en" if choice == 1 else ("fr" if choice == 2 else "it"))  # Instantiate the Random_word_api class with the chosen language
    
    if choice in [1, 2, 3]:
        vocabulary_data = api.fetch_vocabulary()  # Fetch vocabulary for the chosen language
        click.echo(vocabulary_data)  # Display the fetched vocabulary data
    elif choice == 4:
        click.echo("Returning back...")
    else:
        click.echo("Invalid choice. Please choose a valid option.")

@click.command()
def wordSearch():
    click.echo("Search up definitions")
    # Grammar exploration logic

@click.command()
def synonyms():
    word = click.prompt("Search up related words", type=str)
    api = Random_word_api(word)  # You may need to pass the language here
    synonym_data = api.fetch_synonyms()  # Pass the word to the fetch_synonyms method
    click.echo(synonym_data)

@click.command()
def progress():
    click.echo("Check progress")
    # Progress checking logic

if __name__ == "__main__":
    vocabulary.add_command(wordSearch)
    vocabulary.add_command(synonyms)
    vocabulary.add_command(progress)
    vocabulary()

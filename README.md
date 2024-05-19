# Language Learning CLI Application

Welcome to the Language Learning CLI Application! This Python command-line interface (CLI) tool helps users learn vocabulary, translate words, search for synonyms, and track their progress in various languages.

## Overview

The Language Learning CLI Application is designed to facilitate language learning in an efficient and user-friendly manner. It offers a variety of features that complement each other in functionality to aid users in their language learning journey, including vocabulary learning, translation between languages, synonym search, and progress tracking.

## Installation

To use this CLI tool, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the `main.py` script to start the CLI application.

## Prerequisites

Before running the application, ensure that you have the following prerequisites installed:

- Python installed on your machine
- Code editor (e.g., Visual Studio Code, PyCharm)

## Usage

Once the application is running, follow the on-screen instructions to navigate through the different options:

- Register or login to your account.
- Choose an option from the main menu:
  - Learn vocabulary: Select a language and start learning 3 new words.
  - Translate words: Translate words between 3 different languages.
  - Search for synonyms: Find synonyms for any given word also multilingual.
  - Check your progress: View your learning progress in each language.

## Features

- User authentication: Register and login to your account securely.
- Vocabulary learning: Learn new words in English, French, or Italian.
- Translation: Translate words between English, French, and Italian.
- Synonym search: Find synonyms for any word you want.
- Progress tracking: Monitor your learning progress in each language.

## Architecture

This application is built using Python and utilizes the following modules:

- Click: For building command-line interfaces.
- SQLAlchemy: For interacting with the SQLite database.
- Requests: For making HTTP requests to fetch data from APIs.

## Project Structure

The project consists of the following files:

- `main.py`: Contains the main CLI logic and user interaction.
- `user.py`: Defines the `UserHandler` class for user registration, login, and progress tracking.
- `language_api.py`: Implements the `Fetch_from_api` class for fetching vocabulary, synonyms, and translations from external APIs.
- `data_structures.py`: Defines the database structure and session management functions.

## CLI Script (`main.py`)

The `main.py` script is the entry point for the CLI application. It handles user authentication, menu navigation, and interaction with other modules. Upon execution, it prompts users to either register or log in. After successful authentication, users are presented with a main menu where they can choose various options such as learning vocabulary, translating words, searching for synonyms, checking progress, and exiting the application.

### Vocabulary Learning

The **Vocabulary Learning** function allows users to learn three new words in each of the supported languages: English, French, and Italian. Upon selecting this option from the main menu, users are prompted to choose a language. After selecting a language, the application fetches three random words from an external API and displays them to the user. Users can then write down these words to aid in their learning process.

### Synonym Search

The **Synonym Search** function assists users in understanding the random vocabulary learned by providing synonyms for words in three different languages: English, French, and Italian. When users select this option from the main menu, they are prompted to enter a word. The application then fetches synonyms for the provided word from an external API and displays them to the user, helping to broaden their vocabulary and comprehension.

### Translation

The **Translation** function enables users to translate words between the three supported languages: English, French, and Italian. Upon selecting this option from the main menu, users are prompted to choose the source and target languages for translation, as well as the word they wish to translate. The application fetches the translation of the word from the selected source language to the target language using an external API and displays it to the user.

### Progress Tracking

The **Progress Tracking** function allows users to monitor their learning progress in each of the supported languages: English, French, and Italian. Upon selecting this option from the main menu, users can view the number of new words they have learned in each language. The application retrieves this information from the database and displays it to the user, providing valuable insights into their language learning journey.

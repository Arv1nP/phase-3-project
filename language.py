import requests
from sqlalchemy.ext.declarative import declarative_base

class Random_word_api():
    def __init__(self, language):
        self.language = language
        self.base_url = "https://random-word-api.herokuapp.com/word"

    def fetch_vocabulary(self):
        url = f"{self.base_url}?lang={self.language}&number=3"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")

    def fetch_synonyms(self):
        synonym_url = "https://synonyms-word-info.p.rapidapi.com/v1/word/synonyms" #Not using base_url anymore
        headers = {
            "X-RapidAPI-Key": "4b63236c6dmshb00c2a2f818fc0dp1146c9jsn1a89cdfd1cd9",
            "X-RapidAPI-Host": "synonyms-word-info.p.rapidapi.com"
        }
        params = {"str": self.language} #no more a language but the word input by the user is provided
        response = requests.get(synonym_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            synonyms_data = [synonym[0] for synonym in data.get('data', {}).get('synonyms', [])[:10]]  #Dictionary method .get data then .get synonyms
            return synonyms_data
        else:
            print(f"Error: {response.status_code}")





def practice_exercises(language, exercise_type):
    # API call to fetch exercise questions
    pass

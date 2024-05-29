import requests



class Fetch_from_api():
    def __init__(self, data):
        self.data = data
        self.base_url = "https://random-word-api.herokuapp.com/word"

    def fetch_vocabulary(self):
        url = f"{self.base_url}?lang={self.data}&number=3" #Fetch request url and parameters
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
        params = {"str": self.data} #The word input by the user is provided
        response = requests.get(synonym_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            synonyms_data = [synonym[0] for synonym in data.get('data', {}).get('synonyms', [])[:10]]  #Dictionary method .get data then .get synonyms
            return synonyms_data
        else:
            print(f"Error: {response.status_code}, Spelling mistake could be the issue")
        
    def fetch_translation(self, param_1, param_2):
        
        url = f"https://link-bilingual-dictionary.p.rapidapi.com/{param_1}/{param_2}/{self.data}"  # Parameters from and to, then the word

        headers = {
            "X-RapidAPI-Key": "4b63236c6dmshb00c2a2f818fc0dp1146c9jsn1a89cdfd1cd9",
            "X-RapidAPI-Host": "link-bilingual-dictionary.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()  # Result
            # Extracting translations directly from the "results" list
            translation_data = [word['word'] for word in data.get('results', [])[:10]]  
            return translation_data
        else:
            print(f"Error: {response.status_code}")



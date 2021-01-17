import json


class Analize:
    def __init__(self, json_champs):
        self.json_champs = json_champs

    def show_champions(self):
        with open(f'{self.json_champs}.json', 'r') as f:
            data = json.loads(f.readlines()[0])
            return data

    def choose_champ(self, *choose: str):
        data = self.show_champions()
        champ_name = [champ for champ in data if champ['name'][0].lower() == choose[0].lower()]
        return champ_name

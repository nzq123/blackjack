import requests
import json

response_API = requests.get(
    'https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6')
data = response_API.text
deck_data = json.loads(data)
# print(deck_data)


def draw_card(deckId):
    response = requests.get(
        f"https://www.deckofcardsapi.com/api/deck/{deckId}/draw/?count=1")
    data = response.text
    card = json.loads(data)['cards'][0]
    return card['value']

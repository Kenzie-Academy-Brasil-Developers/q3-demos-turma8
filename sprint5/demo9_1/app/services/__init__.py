import requests
import ipdb


def retrieve_rick_and_morty_images():
    url = "https://rickandmortyapi.com/api/character"

    response = requests.get(url)
    # ipdb.set_trace()

    # response.json()['results'][0]['image']

    results = response.json()["results"]

    return [char["image"] for char in results]

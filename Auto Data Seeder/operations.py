import requests


def create_entry(api_url, json, headers):
    response = requests.post(api_url, json, headers)
    return response


def update_entry(api_url, id, json, headers):
    api_url = api_url+str(id)
    response = requests.put(api_url, json, headers)
    return response


def delete_entry(api_url, id):
    api_url = api_url+str(id)
    response = requests.delete(api_url)
    return response

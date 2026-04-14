import requests

def call_api(keyword: str):
    url = "https://api.artic.edu/api/v1/artworks/search"
    params = {
        "q": keyword,
        "limit": 5,
        "fields": "id,title,image_id,artist_title,date_display"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {
            "error": "Failed to fetch data",
            "status_code": response.status_code
        }

    data = response.json()
    print(data)
    return data
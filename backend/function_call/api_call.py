import requests

def call_api(keyword: str):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            params={"q": keyword, "fields": "id,title,artist_title,image_id,date_display"},
            timeout=5,
            
        )

        data = response.json()
        
        return data

    except requests.exceptions.RequestException as e:
        print("API error:", e)
        return []
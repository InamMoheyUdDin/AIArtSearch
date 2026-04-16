import json
from function_call.api_call import call_api

def retrieve_data(response):
    if response.choices[0].message.tool_calls:
        function_call = response.choices[0].message.tool_calls[0].function
        if function_call.name == "get_artwork":
            keyword = json.loads(function_call.arguments)["keyword"]
            if keyword:
                artwork = call_api(keyword)
            
                return [
                    {
                        "title": a.get("title"),
                        "artist": a.get("artist_title", "Unknown Artist"),
                        "date": a.get("date_display", "Unknown"),
                        "image_id": a.get("image_id")
                    } for a in artwork["data"][:5]]
            else:
                return "Sorry, I couldn't make any requests based on your input"
        else:
            return "Sorry, I couldn't find any artwork"
    else:
        return "Sorry, I don't understand your request"
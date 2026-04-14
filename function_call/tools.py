
tools = [
    {
    "type": "function",
    "function":{
        "name": "get_artwork",
        "description": "Get the relevent artwork based on the keyword the user enters",
        "parameters":{
            "type": "object",
            "properties":{
                "keyword":{
                    "type": "string",
                    "description": "Key word enter by user"
                    }
                },
                "required": ["keyword"]
            }
        }
    }
]
import json 

api_response = ''' 
{
  "id": 101,
  "name": {
    "first_name": "Anish",
    "last_mame": "Shakya"
  },
  "username": "anish",
  "contact": {
    "email": "anish@example.com",
    "social_media": {
      "Meta": "facebook/anishshakya1",
      "Insta": {
        "id1": "instagram/anish1",
        "id2": "instagram/anishshaya2"
      }
    }
  },
  "address": {
    "Country": "Nepal",
    "Province": "Bagmati",
    "street": "Main Road",
    "city": "Kathmandu",
    "zipcode": "44600",
    "geo": {
      "lat": "27.7172",
      "lng": "85.3240"
    }
  },
  "company": {
    "name": "Example Analytics",
    "department": "Data Engineering"
  }
}

'''

customer = json.loads(api_response)

def flatten_dict(data, parent_key="", separator="_"):
    flattened = {}

    for key, value in data.items():

        new_key = f"{parent_key}{separator}{key}" if parent_key else key

        if isinstance(value, dict):
            flattened.update(
                flatten_dict(
                    value,
                    parent_key=new_key,
                    separator=separator
                )
            )
        else:
            flattened[new_key] = value

    return flattened

print(flatten_dict(customer))
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker  
from rasa_sdk.executor import CollectingDispatcher  
import requests

class ActionGetWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        api_key = "0a3c449075a82e26292c1379f3b3c3bd"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Try to get location from slot or default
        location = tracker.get_slot("location") or "Himachal Pradesh"

        # Check entities in message if available
        for entity in tracker.latest_message.get("entities", []):
            if entity.get("entity") == "location":
                location = entity.get("value")

        # Construct API request
        complete_url = f"{base_url}appid={api_key}&q={location}&units=metric"

        try:
            response = requests.get(complete_url)
            data = response.json()

            if data.get("cod") != 200:
                reply = f"I couldn't find the weather for '{location}'. Please try a different city."
            else:
                main = data["main"]
                temperature = main["temp"]
                weather_desc = data["weather"][0]["description"]

                # Smart snow response
                if "snow" in weather_desc.lower():
                    reply = f"Yes, it looks like it will snow in {location}. The temperature is {temperature}°C."
                else:
                    reply = f"The weather in {location} is currently '{weather_desc}' with a temperature of {temperature}°C."

        except Exception as e:
            reply = "Sorry, I couldn't retrieve the weather due to a technical issue."

        dispatcher.utter_message(text=reply)
        return []

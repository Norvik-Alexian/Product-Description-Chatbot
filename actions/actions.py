import os
import requests

from typing import Any, Text, Dict, List
from dotenv import load_dotenv
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

load_dotenv()


class ActionProductDescriptionGenerator(Action):

    def name(self) -> Text:
        return "action_product_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        PRODUCT_DESCRIPTION_ENDPOINT = os.getenv('PRODUCT_DESCRIPTION_ENDPOINT')
        UC_X_API_KEY = os.getenv('UC-X-API-KEY')

        headers = {
            'accept': 'application/json',
            'UC-X-API-KEY': UC_X_API_KEY,
        }

        json_data = {
            'keywords': [
                'ucraft',
                'website builder',
                'ecommerce'
            ],
            'content_type': 'description_highlight',
            'count': 1
        }

        response = requests.post(PRODUCT_DESCRIPTION_ENDPOINT,
                                 headers=headers, json=json_data)

        generated_text = '\n'.join(response.json())
        dispatcher.utter_message(text=generated_text)

        return []
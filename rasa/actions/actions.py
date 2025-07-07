import logging
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# Configure structured logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class ActionCheckOrderStatus(Action):
    def name(self) -> Text:
        return "action_check_order_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        order_number = next(tracker.get_latest_entity_values("order_number"), None)

        if not order_number:
            dispatcher.utter_message(text="Please provide your order number.")
            return []

        try:
            # Replace with actual API or DB logic in production
            logger.info(f"Fetching status for order: {order_number}")
            status_info = {
                "status": "Shipped",
                "eta": "2 business days"
            }

            dispatcher.utter_message(
                text=f"Order #{order_number} is {status_info['status']} and will arrive in {status_info['eta']}."
            )
            return [SlotSet("order_number", order_number)]

        except Exception as e:
            logger.error(f"Error fetching order status for {order_number}: {str(e)}")
            dispatcher.utter_message(
                text="Sorry, I couldn’t retrieve your order at the moment. Please try again later."
            )
            return []


class ActionSendReturnLink(Action):
    def name(self) -> Text:
        return "action_send_return_link"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        try:
            return_url = "https://example.com/returns"
            dispatcher.utter_message(text=f"You can start your return here: {return_url}")
            logger.info("Return link sent successfully.")
        except Exception as e:
            logger.error(f"Failed to send return link: {str(e)}")
            dispatcher.utter_message(
                text="I couldn’t fetch the return link right now. Please try again later."
            )

        return []


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        user_input = tracker.latest_message.get("text", "[no message]")
        logger.warning(f"Fallback triggered. User message: {user_input}")

        dispatcher.utter_message(
            text="Sorry, I didn't understand that. Please reach out to customer care for further assistance."
        )

        return []

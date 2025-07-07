import pytest
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions import ActionCheckOrderStatus, ActionSendReturnLink, ActionDefaultFallback


def test_check_order_status_success(monkeypatch):
    tracker = Tracker(
        sender_id="test_user",
        slots={},
        latest_message={"entities": [{"entity": "order_number", "value": "123456"}]},
        events=[],
        paused=False,
        followup_action=None,
        active_loop={},
        latest_action_name=None
    )

    dispatcher = CollectingDispatcher()
    action = ActionCheckOrderStatus()

    result = action.run(dispatcher, tracker, {})
    assert any("Order #123456" in m["text"] for m in dispatcher.messages)


def test_check_order_status_missing_number():
    tracker = Tracker(
        sender_id="test_user",
        slots={},
        latest_message={"entities": []},
        events=[],
        paused=False,
        followup_action=None,
        active_loop={},
        latest_action_name=None
    )

    dispatcher = CollectingDispatcher()
    action = ActionCheckOrderStatus()

    result = action.run(dispatcher, tracker, {})
    assert "Please provide your order number." in dispatcher.messages[0]["text"]


def test_send_return_link():
    tracker = Tracker(
        sender_id="test_user",
        slots={},
        latest_message={},
        events=[],
        paused=False,
        followup_action=None,
        active_loop={},
        latest_action_name=None
    )

    dispatcher = CollectingDispatcher()
    action = ActionSendReturnLink()

    result = action.run(dispatcher, tracker, {})
    assert "return here" in dispatcher.messages[0]["text"]


def test_default_fallback():
    tracker = Tracker(
        sender_id="test_user",
        slots={},
        latest_message={"text": "asdfgh"},
        events=[],
        paused=False,
        followup_action=None,
        active_loop={},
        latest_action_name=None
    )

    dispatcher = CollectingDispatcher()
    action = ActionDefaultFallback()

    result = action.run(dispatcher, tracker, {})
    assert "didn't understand" in dispatcher.messages[0]["text"]

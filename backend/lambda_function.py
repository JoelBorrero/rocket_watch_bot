import json
from models import Message
from services import Game, Telegram


def lambda_handler(event: dict, context):
    """
    Handles incoming Lambda function events.

    Args:
        event (dict): The event data.
        context: The Lambda function runtime context.

    Returns:
        dict: The response data.
    """
    event = event["body"]
    if isinstance(event, str):
        event = json.loads(event)

    response = {}
    game = Game()
    telegram = Telegram()
    if "message" in event:
        message = Message.from_json(event["message"])
        if message.text == Telegram.Commands.START:
            response = game.start()
            telegram.send_photo(
                chat_id=message.chat_id,
                photo=response["image"],
                state=response,
            )
    elif "callback_query" in event:
        message = Message.from_json(event["callback_query"]["message"])
        message.text = event["callback_query"]["message"]["reply_markup"]["inline_keyboard"][0][0]["callback_data"]
        if message.text == Telegram.Commands.START:
            response = game.start()
            telegram.send_photo(
                chat_id=message.chat_id,
                photo=response["image"],
                state=response,
            )
        else:
            state = game.play_from_callback(event["callback_query"]["data"])
            if state["landing_frame"] is None:
                telegram.send_photo(
                    chat_id=message.chat_id,
                    photo=state["image"],
                    state=state,
                    message_id=message.id
                )
            else:
                telegram.send_message(
                    chat_id=message.chat_id,
                    text="Yay! You found the landing frame!\n"
                         "Thanks to your skills, we know that "
                         "the rocket landed on the frame "
                         f"{state['landing_frame']}.",
                    message_id=message.id,
                    button="Play again"
                )
    elif event.get("from") == "vue":
        if "state" in event:
            response = game.play_from_game(event["state"])
        else:
            response = game.start()
    return {"statusCode": 200, "body": response}

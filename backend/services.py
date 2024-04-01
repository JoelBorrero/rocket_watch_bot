from os import getenv

from json import dumps, loads
from requests import get, post, Response
from urllib.parse import quote, urljoin

from models import State


class Game:
    def __init__(
            self,
            host: str = "https://framex-dev.wadrid.net/api/",
            video_name: str = "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c",
    ):
        self.host = host
        self.video_name = video_name

        self.state = State()

    def with_image(self, image=None) -> dict:
        return {
            "frames": self.state.frames,
            "image": image or self.get_image(),
            "left": self.state.left,
            "right": self.state.right,
            "landing_frame": self.state.landing_frame,
        }

    def set(self, state: dict) -> None:
        self.state = State.from_dict(state)

    def get_image(self) -> str:
        frame = int((self.state.left + self.state.right) / 2)
        return self.get_image_from_frame(frame)

    def get_image_from_frame(self, frame: int) -> str:
        return urljoin(self.host, f"video/{quote(self.video_name)}/frame/{quote(f'{frame}')}/")

    def play(self, response: bool) -> int:
        """
        Runs a bisection.

        - `response` true if the value is within the "right" range
        """

        if self.state.frames < 1:
            raise ValueError("Cannot bisect an empty array")

        if self.state.left + 1 < self.state.right:
            mid = int((self.state.left + self.state.right) / 2)
            if response:
                self.state.right = mid
            else:
                self.state.left = mid
            if self.state.left + 1 == self.state.right:
                self.state.landing_frame = self.state.right
                return self.state.landing_frame
            return mid

        return self.state.right

    def play_from_game(self, game: dict) -> dict:
        self.set(game)
        self.play(game["response"])
        return self.with_image()

    def play_from_callback(self, data: str):
        self.state = State.from_short(loads(data))
        self.play(self.state.response)
        return self.with_image()

    def start(self) -> dict:
        response = get(urljoin(self.host, f"video/{quote(self.video_name)}/")).json()
        self.state.frames = response["frames"]
        self.state.left = 0
        self.state.right = self.state.frames - 1
        return self.with_image()


class Telegram:
    class Commands:
        START = "/start"

    def get_updates(self) -> Response:
        return get(self.url("getUpdates")).json()

    def send_message(self, chat_id: int, text: str, message_id: str = None, button: str = None) -> Response:
        data = {"chat_id": chat_id}
        if button is None:
            data["text"] = text
            return post(self.url("sendMessage"), data=data)
        else:
            data["message_id"] = message_id
            data["caption"] = text
            data["reply_markup"] = dumps({
                "inline_keyboard": [[
                    {"text": button, "callback_data": "/start"}
                ]]
            })
            return post(self.url("editMessageCaption"), data=data)

    def send_photo(self, chat_id: int, photo: str, state: dict, message_id: str = None) -> Response:
        state.pop("image")
        callback_no = State(response=False, **state).dump_short()
        callback_yes = State(response=True, **state).dump_short()
        data = {
            "chat_id": chat_id,
            "reply_markup":
                dumps({
                    "inline_keyboard": [[
                        {"text": "Yes 🚀", "callback_data": callback_yes},
                        {"text": "No ⚓️", "callback_data": callback_no},
                    ]],
                    "one_time_keyboard": True,
                })
        }
        if message_id is None:
            data["photo"] = photo
            data["caption"] = "Did the rocket launch yet?"
            return post(self.url("sendPhoto"), data=data)
        else:
            data["message_id"] = message_id
            data["media"] = dumps({"type": "photo", "media": photo})
            return post(self.url("editMessageMedia"), data=data)

    @staticmethod
    def url(path: str) -> str:
        return f"https://api.telegram.org/bot{getenv('TELEGRAM_API_KEY')}/{path}"

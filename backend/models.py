from json import dumps


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def from_json(data: dict):
        return User(first_name=data["first_name"], last_name=data.get("last_name"))


class Message:
    def __init__(self, pk: int, text: str, user: User, chat_id: int):
        self.id = pk
        self.text = text
        self.user = user
        self.chat_id = chat_id

    @staticmethod
    def from_json(data: dict):
        return Message(
            pk=data["message_id"],
            text=data.get("text"),
            user=User.from_json(data["from"]),
            chat_id=data["chat"]["id"],
        )


class State:
    def __init__(self, frames: int = None, left: int = None, right: int = None, landing_frame=None,
                 response: bool = None):
        self.frames = frames
        self.left = left
        self.right = right
        self.landing_frame = landing_frame
        self.response = response

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            frames=data["frames"],
            left=data["left"],
            right=data["right"],
            landing_frame=data["landing_frame"],
            response=data["response"]
        )

    @classmethod
    def from_short(cls, short: dict):
        return cls(
            frames=short["f"],
            left=short["l"],
            right=short["r"],
            landing_frame=short["lf"],
            response=short["re"]
        )

    def dump_short(self) -> str:
        return dumps({
            "f": self.frames,
            "l": self.left,
            "r": self.right,
            "lf": self.landing_frame,
            "re": self.response,
        })

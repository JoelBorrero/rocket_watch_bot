from json import dumps


class User:
    def __init__(self, first_name, last_name):
        """
        Initializes a new instance of the User class.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
        """
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def from_json(data: dict):
        """
        Creates a User object from JSON data.

        Args:
            data (dict): The JSON data representing the user.

        Returns:
            User: The User object.
        """
        return User(first_name=data["first_name"], last_name=data.get("last_name"))


class Message:
    def __init__(self, pk: int, text: str, user: User, chat_id: int):
        """
        Initializes a new instance of the Message class.

        Args:
           pk (int): The ID of the message.
           text (str): The text of the message.
           user (User): The user who sent the message.
           chat_id (int): The ID of the chat.
        """
        self.id = pk
        self.text = text
        self.user = user
        self.chat_id = chat_id

    @staticmethod
    def from_json(data: dict):
        """
        Creates a Message object from JSON data.

        Args:
            data (dict): The JSON data representing the message.

        Returns:
            Message: The Message object.
        """
        return Message(
            pk=data["message_id"],
            text=data.get("text"),
            user=User.from_json(data["from"]),
            chat_id=data["chat"]["id"],
        )


class State:
    def __init__(self, frames: int = None, left: int = None, right: int = None, landing_frame=None,
                 response: bool = None):
        """
        Initializes a new instance of the State class. This is the state of the game.

        Args:
            frames (int): The total number of frames.
            left (int): The left boundary.
            right (int): The right boundary.
            landing_frame: The landing frame if found.
            response (bool): The user's response.
        """
        self.frames = frames
        self.left = left
        self.right = right
        self.landing_frame = landing_frame
        self.response = response

    @classmethod
    def from_dict(cls, data: dict):
        """
        Factory constructor to create a State object from a dictionary.

        Args:
            data (dict): The dictionary representing the state.

        Returns:
            State: The State object.
        """
        return cls(
            frames=data["frames"],
            left=data["left"],
            right=data["right"],
            landing_frame=data["landing_frame"],
            response=data["response"]
        )

    @classmethod
    def from_short(cls, short: dict):
        """
        Factory to create a State object from a short dictionary.

        Args:
            short (dict): The short dictionary representing the state.

        Returns:
            State: The State object.
        """
        return cls(
            frames=short["f"],
            left=short["l"],
            right=short["r"],
            landing_frame=short["lf"],
            response=short["re"]
        )

    def dump_short(self) -> str:
        """
        Dumps the state object to a short JSON string.
        It's being shortened due to callback limitations on Telegram buttons.

        Returns:
            str: The short JSON string representing the state.
        """
        return dumps({
            "f": self.frames,
            "l": self.left,
            "r": self.right,
            "lf": self.landing_frame,
            "re": self.response,
        })

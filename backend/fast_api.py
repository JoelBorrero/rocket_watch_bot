from os import getenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from lambda_function import lambda_handler


API_BASE = getenv("API_BASE", "https://framex-dev.wadrid.net/api/")
VIDEO_NAME = getenv(
    "VIDEO_NAME", "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://rocket-watch-bot.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def lambda_wrapper(body: dict):
    """
    Endpoint to handle incoming requests and pass them to the Lambda handler.
    This FastAPI project is used to improve the development experience and upload later to AWS.

    Args:
        body (dict): The request body.

    Returns:
        dict: The response from the Lambda handler.
    """
    return lambda_handler({"body": body}, None)

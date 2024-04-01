# Rocket Watch Bot

![](https://github.com/JoelBorrero/rocket_watch_bot/blob/main/frontend/src/assets/rocket.png)

Rocket Watch Bot is a comprehensive solution for tracking rocket launches interactively. This project contains both the frontend and backend components within a single mono repository, providing a seamless development and deployment experience.

**Features:**
- **Interactive Interface**: Users are presented with images of rocket launches and prompted to indicate whether the rocket has been launched or not.
- **Real-time Feedback**: The bot provides real-time feedback based on user input, allowing for efficient tracking of rocket launch events.
- **Mono Repository**: Both the frontend and backend components are housed within a single repository, streamlining development and maintenance processes.

**Technologies Used:**
- **Frontend**: Vue.js framework for building dynamic user interfaces.
- **Backend**: Python 3.12 for connecting to the Telegram API. The backend was initially tested using FastAPI but finally deployed as a serverless application on AWS Lambda for simplicity and cost efficiency.
- **Deployment**: Because of it is a simple project, all incoming requests are handled within the same wrapper function to utilize the AWS Lambda endpoint. I could have used API Gateway, but I didn't see it as necessary.

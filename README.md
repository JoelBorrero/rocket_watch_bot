# Rocket Watch Bot

![](https://github.com/JoelBorrero/rocket_watch_bot/blob/main/frontend/src/assets/rocket.png)

**Rocket Watch Bot** is a comprehensive solution for tracking rocket launches interactively. This project contains both the frontend and backend components within a single mono repository, providing a seamless development and deployment experience.

## Features
- 📟 **Interactive Interface**: Users are presented with images of rocket launches and prompted to indicate whether the rocket has been launched or not.
- ⚡️ **Real-time Feedback**: The bot provides real-time feedback based on user input, allowing for efficient tracking of rocket launch events.
- 🔰 **Mono Repository**: Both the frontend and backend components are housed within a single repository, streamlining development and maintenance processes.
- 📝 **TODOs**:
  - Use _State_ model on _Game_ service responses (Usages in _lambda_function.py_)
  - Implement tests, at least for the backend as priority
  - Pre-commit and CI/CD on success builds

## Technologies Used:
- <img width="12" src="https://vuejs.org/images/logo.png" alt="Vue logo"></a> **Frontend**: Vue.js framework for building dynamic user interfaces.
- <img width="12" src="https://cdn.worldvectorlogo.com/logos/aws-lambda-1.svg" alt="Lambda logo"></a> **Backend**: Python 3.12 for connecting to the Telegram API. The backend was initially tested using FastAPI but finally deployed as a serverless application on AWS Lambda for simplicity and cost efficiency.
- 🛅 **Deployment**: Because of it is a simple project, all incoming requests are handled within the same wrapper function to utilize the AWS Lambda endpoint. I could have used API Gateway, but I didn't see it as necessary.

## Contributing

To contribute to the **Rocket Watch Bot**, follow these steps:

1. Clone the [repository](https://github.com/JoelBorrero/rocket_watch_bot) and create a new branch from `main` with a descriptive name reflecting your contribution.
2. Ensure your code adheres to the project's coding standards and style guidelines, leveraging linters and style checks.
3. Thoroughly test your changes before committing, and push your branch to the remote repository.
4. Create a pull request targeting the `main` branch, including a detailed description of your modifications. Remember to fill the template file all the fields from the template form.
5. After a code review, addressing feedback promptly, your changes will be merged into `main`.

Thank you for enhancing the **Rocket Watch Bot** — your contributions are integral to creating a more dynamic experiences.

Happy coding! 🚀👩‍💻👨‍💻
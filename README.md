# AgeDetection Bot 🤖

This Telegram bot estimates the age of a person from a photo using AI-powered facial analysis. Built for fun and learning, it uses Docker Compose for deployment and integration with Telegram API.

---

## Features

- 📸 **Age Estimation**: Upload a photo of a face, and the bot will predict the person's age.
- 💬 **Interactive Commands**: Start, help commands for a smooth user experience.
- 🐳 **Dockerized Deployment**: Simple and portable deployment with Docker.
- 🚀 **Fast & Reliable**: Designed for quick and accurate results.

---

## Bot Commands

- `/start` - Welcome message and brief instructions.
- `/help` - Detailed usage guide.
  
---

## Prerequisites

- **Docker**: Installed on your system.
- **Docker Compose**: Installed and properly configured.
- **Telegram Bot Token**: Obtain one by creating a bot using [BotFather](https://core.telegram.org/bots#botfather) and place YOUR TOKEN into api.py file.

---

## Installation and Deployment
```bash
git clone git@github.com:Vlad4Per/PMDL-course-project.git
cd PMDL-course-project/code/deployment
docker-compose up --build

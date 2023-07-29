# Tutorial for Telegram Bot API

## Introduction

This tutorial is for those who want to develop a Telegram bot for the first time. We will use `requests` library to send HTTP requests to Telegram Bot API. We will also use `json` library to parse the response from Telegram Bot API.

## Prerequisites

- Python 3.6 or above
- `requests` library
- `json` library

## Create a Telegram Bot

1. Open Telegram app and search for `@BotFather`.
2. Send `/newbot` command to `@BotFather`.
3. Follow the instructions to create a new bot.
4. Copy the token of the bot.

## Get telegram bot information using `getMe` method

1. URL: `https://api.telegram.org/bot<token>/getMe`
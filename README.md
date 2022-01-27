# Navi - WIP Multipurpose Discord Bot
Created during the end of hacktoberfest 2021.

## Dependencies
- Python3.9+
- pycord (2.0.0a) ``pip install -U git+https://github.com/Pycord-Development/pycord``
- python-dotenv ``pip install python-dotenv``

## Installation
- Install the dependencies
- Create a bot profile and invite it with the ``bot`` and ``applications.commands`` scope.
- Create a file named ``.env``
- In the ``.env`` file, add the following line: ``BOT_TOKEN=0123456789``
  - Make sure to replace ``0123456789`` to your actual bot token.
- Run ``python3 src/main.py`` to run the bot.

## To Do
- Remove .env and move to config.py
- More Commands
- Fully move to slash commands
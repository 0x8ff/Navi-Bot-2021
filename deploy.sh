#!/bin/sh
if ! command -v pip > /dev/null; then
	echo "Error: pip not installed."
	exit 1
fi

echo "Installing Pycord-Dev"
pip install -U git+https://github.com/Pycord-Development/pycord /
pip install python-dotenv

echp "Running bot..."
python3 src/bot.py
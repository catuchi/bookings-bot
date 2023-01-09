# Bookings Bot

Web Scaping bot built with Python and Selenium. Automates search on bookings.com and displays results in an easily digestable format using [Prettytable](https://pypi.org/project/prettytable/)

## Run Locally

Version Requirements

```py
"engines": {
    "pip": "20.3.4",
    "python": "2.7.18"
  }
```

To run this project, you will need to install Chromedriver. Click [here](https://www.youtube.com/watch?v=pyqz8X7UUDs) to learn how to install Chromedriver

Assign driver_path to r=":/path/to/chromedriver"

Clone the project

```bash
  git clone git@github.com:catuchi/bookings-bot.git
```

Go to the project directory

```bash
  cd bookings-bot
```

Install dependencies

```bash
  pip install selenium
  pip install prettytable
```

Start the server

```bash
  python run.py
```

# [phytotron 🪴📋](https://en.wikipedia.org/wiki/Phytotron)

a greenhouse board application submitting bot

## Project Status

⚠️ This project is still in development and not yet ready for use. ⚠️

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
    - [settings.py](#settingspy)
    - [phytotron.toml](#phytotrontoml)
- [Usage](#usage)
- [Contributing](#contributing)
    - [Suggest New Form Fields](#suggest-new-form-fields)
    - [Development](#development)

## Requirements

- Python 3.13

## Installation

```shell
git clone https://github.com/yoonthegoon/phytotron.git
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

### settings.py

The bot will be unable to scrape Google as the default settings by scrapy are:

```python
# phytotron/settings.py

USER_AGENT = "Scrapy/2.12.0 (+https://scrapy.org)"  # L16-L20
ROBOTSTXT_OBEY = True  # L23
DEFAULT_REQUEST_HEADERS = {  # L43-47
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
}
```

I cannot suggest you change those in [settings.py](/phytotron/settings.py) to get around
Google's [robots.txt](https://www.google.com/robots.txt), but it is something that can be done.

### phytotron.toml

Add a `phytotron.toml` to the project root directory.
Below is an example configuration:

```toml
# phytotron.toml

first_name = "string"
last_name = "string"
email = "string"

[arguments]
days = 0  # jobs posted in last <days> days
keywords = ["string"]

[phone]
number = 0  # phone number (no cc)
country_code = 1
type = "string"  # home, mobile, etc.
fill_not_required = false

[address]
street_address = "string"
city = "string"
state = "string"
zip_code = 0
fill_not_required = false

[resume]
path = "/path/to/resume.pdf"
fill_not_required = true

[work_authorization]
us_work_auth = true
us_citizen = true
require_sponsor = false
fill_not_required = false

[demographic]
gender = "prefer not to say"
lgbtq = "prefer not to say"
hispanic_latino = "prefer not to say"
race = "prefer not to say"
veteran_status = "prefer not to say"
disability_status = "prefer not to say"
fill_not_required = false

[common]
school = "string"
degree = "string"
study = "string"
school_start = 2020-08-16
school_end = 2024-04-15

contact_sms = false

govt_work = false

linkedin_profile = "https://linkedin.com/in/<profile>/"
websites = ["https://github.com/yoonthegoon"]

hear_how = "https://github.com/yoonthegoon/phytotron"

fill_not_required = false
```

## Usage

Run the bot.

```shell
python -m phytotron
```

An `items.csv` will be written in the project root directory.
It contains the URL and labels of the missing required fields of all the applications it failed to submit.

Fill in the inputs for each field rerun the bot with:

```shell
python -m phytotron rerun
```

It will go to all the failed application submissions and resubmit them with your new field inputs.
This will overwrite `items.csv` with the remaining failed submissions.
From there, you can decide whether or not you'd like to fill those applications out manually.

## Contributing

### Suggest New Form Fields

If there are form fields you're running into frequently, open an issue with the desired field.
I may update the `phytotron.toml` and add handling the field.

### Development

To open a PR, fork the repository and open a PR with your changes from there.

Poetry 1.8.4 is required for development.
In the project root directory, run the following:

```shell
poetry install
poetry shell
```

Before opening a PR, please go through this checklist:

- [ ] Update project version in [pyproject.toml](/pyproject.toml#L3)
  following [Semantic Versioning](https://semver.org/)
- [ ] Update lock file `poetry update`
- [ ] Update requirements `poetry export -o requirements.txt`
- [ ] Format with ruff `ruff format .`

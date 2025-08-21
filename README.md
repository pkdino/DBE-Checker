# DBE Checker

**Data Breach Exposure Checker**  
A Python-based tool that checks if an email address (or list of emails) has appeared in known data breaches using [Have I Been Pwned](https://haveibeenpwned.com) and [Shodan](https://www.shodan.io).  
This project is designed for learning purposes only and demonstrates how Python can be used for automation, API interaction, and security awareness reporting.

---

## Features

- Check a single email address or multiple addresses at once
- Query the Have I Been Pwned API for breach data
- Display breach details such as site name, date, and compromised data types
- Save results into JSON or CSV for later analysis
- Generate user-friendly reports for awareness purposes
- Compatible with Python 3.8+
- Requires [Have I Been Pwned API key](https://haveibeenpwned.com/API/Key)
- Requires [Shodan API key](https://account.shodan.io/register)

---

## Purpose

This project was built to:

- Practice Python problem-solving with real-world cybersecurity challenges
- Learn how to interact with external APIs securely
- Explore the importance of data breach awareness and credential safety
- Showcase a blue team–oriented tool that aligns with modern security needs
- Enable deep problem-solving through trial and error
- Create something practical and realistic within the cybersecurity field

---

## How to Use

This Python script checks if an email has been involved in known data breaches using **Have I Been Pwned (HIBP)** and allows simple **Shodan searches** for devices and services on the internet.

### Prerequisites

- Python 3.9 or higher
- `pip` installed
- API keys:
  - [Have I Been Pwned API key](https://haveibeenpwned.com/API/Key)
  - [Shodan API key](https://account.shodan.io/register)


### Clone the Repository


**BASH:**

```git clone https://github.com/pkdino/DBE-Checker.git```

```cd DBE-Checker```


## Install Packages


```pip install -r requirements.txt```

*(If the requirements dont work, them manually install: ```pip install shodan requests python-dotenv```)*


### Running The Script


```python main.py```
- You'll be prompted to enter your email to check against HIBP.
- After the return, youll enter a Shodan search query (e.g., apache, nginx, ssh) to see the number of devices/services that match your query.


### Key Information


**You need to create your own ```.env``` file and use your own API keys.** This is the safest way without exposing your keys publicly!
If you don't know how to create a ```.env``` file, you can refer to [python-dotenv on PyPI.](https://pypi.org/project/python-dotenv/)
HIBP does require a *small* cost for API access, while Shodan has free and paid tiers.

---------------------

### Important Disclaimer

This tool is created **strictly for educational purposes.** It must only be used on email accounts that *YOU* personally own or have explicit permission to test. Unauthorized use on third-party accounts may violate privacy laws and ethical guidelines. Be safe, and use this project I created responsibly!

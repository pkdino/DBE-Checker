# DBE Checker

**Data Breach Exposure Checker**
A Python-based tool that checks if an email address (or list of emails) has appeared in known data breaches using [Have I Been Pwned](https://haveibeenpwned.com) and [Shodan](https://www.shodan.io).
This project is designed for learning purposes only and demonstrates how Python can be used for automation, API interaction, and security awareness reporting.


**Features**

- Check a single email address or multiple addresses at once
- Query the Have I Been Pwned API for breach data
- Display breach details such as site name, date, and compromised data types
- Save results into JSON or CSV for later analysis
- Generate user-friendly reports for awareness purposes
- Python 3.8+
- A Have I Been Pwned API key


**Purpose**

This project was built to:
- Practice Python problem-solving with real-world cybersecurity challenges
- Learn how to interact with external APIs securely
- Explore the importance of data breach awareness and credential safety
- Showcase a blue team–oriented tool that aligns with modern security needs
- Enable deep problem solving through trial and error
- Create something practical/realistic within the cybersecurity field

---

**Key Information to Know**

You'll need to make your own .env file and use your own API keys for HIBP/Shodan. Doing this is the safest way without giving out your keys to anyone. If you don't know how to make an .env file, you can find it on the [pypi.org](https://pypi.org/project/python-dotenv/) here or ask your local AI assistant *(reading is fundamental though.)*

You will need to create your own accounts, and utilize the free version of Shodan. HIBP does cost very little, but it is needed to retrieve your API key (Shodan has membership tiers.)

**Important Disclaimer**

This tool is created *strictly* for educational purposes. It must only be used on email accounts that you personally own or have explicit permission to test. Unauthorized use on third-party accounts may violate privacy laws and ethical guidelines. Be safe, and beware!

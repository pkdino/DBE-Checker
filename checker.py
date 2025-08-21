import os
import requests
from shodan import Shodan, APIError
from dotenv import load_dotenv, find_dotenv

# ------------------ ENVIRONMENT ------------------ #
load_dotenv(find_dotenv())
HIBP_KEY = os.getenv("HIBP_KEY")
SHODAN_KEY = os.getenv("SHODAN_KEY")

if not SHODAN_KEY:
    raise ValueError("Missing SHODAN_KEY in .env")

# Optional: show key presence
print("HIBP_KEY loaded:", bool(HIBP_KEY))

# ------------------ SHODAN CLIENT ------------------ #
shodan_api = Shodan(SHODAN_KEY)

def shodan_banner_count(api, query, limit=5):
    """
    Search Shodan for a query and return the number of results.
    Limit results to avoid free account restrictions.
    """
    try:
        result = api.search(query, limit=limit)
        print(f"[-] Shodan results for '{query}' (limited to {limit}): {result['total']}")
        for match in result['matches']:
            print(f"  - IP: {match['ip_str']}, Port: {match['port']}")
        return result['total']
    except APIError as e:
        # Handles Shodan API-specific errors, including 403
        if '403' in str(e):
            print("[x] Shodan 403: API key does not have access or exceeded limits. Please Check membership.")
        else:
            print(f"[x] Shodan API error: {e}")
        return 0
    except Exception as e:
        print(f"[x] Unexpected error with Shodan: {e}")
        return 0

# ------------------ HIBP ------------------ #
def check_hibp(email, hibp_key):
    """
    Check if an email has been in a breach using HIBP API.
    """
    if not hibp_key:
        print("[-] HIBP key missing; skipping HIBP check.")
        return None

    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": hibp_key,
        "user-agent": "DBE_Checker"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []  # No breaches
        else:
            print(f"[x] HIBP error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"[x] Exception while contacting HIBP: {str(e)}")
        return None

# ------------------ MAIN ------------------ #
def main():
    # HIBP check
    email = input("Enter your email to check against HIBP: ").strip()
    breaches = check_hibp(email, HIBP_KEY)

    if breaches is None:
        print("Something went wrong with HIBP (or key missing).")
    elif len(breaches) == 0:
        print("[-] No breaches found for this email.")
    else:
        print(f"[!] Your email was found in {len(breaches)} breach(es):")
        for breach in breaches:
            print(f" - {breach['Name']} (breached on {breach['BreachDate']})")

    # Shodan search
    query = input("\nEnter a Shodan search query (e.g., apache, nginx, ssh): ").strip()
    shodan_banner_count(shodan_api, query)

if __name__ == '__main__':
    main()
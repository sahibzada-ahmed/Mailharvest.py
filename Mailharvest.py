import re
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import random
import time

# Function to generate random colors for text
def random_color(text):
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    return colored(text, random.choice(colors))

def extract_emails_from_url(url):
    try:
        response = requests.get(url)
        content = response.text

        # Use a regex pattern to find all email addresses in the content
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
        return set(emails)

    except requests.exceptions.RequestException as e:
        print(random_color(f"Error fetching the URL: {e}"))
        return set()

def print_futuristic_banner():
    banner = """
███████╗██╗     ███████╗███████╗████████╗
██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝
█████╗  ██║     █████╗  ███████╗   ██║   
██╔══╝  ██║     ██╔══╝  ╚════██║   ██║   
██║     ███████╗███████╗███████║   ██║   
╚═╝     ╚══════╝╚══════╝╚══════╝   ╚═╝   
"""
    for line in banner.splitlines():
        print(random_color(line))
        time.sleep(0.1)

def main():
    print_futuristic_banner()
    print(random_color("Email Harvester Tool\n"))
    url = input(random_color("Enter the URL to harvest emails from: "))
    emails = extract_emails_from_url(url)

    if emails:
        print(random_color(f"\nFound {len(emails)} email(s):\n"))
        for email in emails:
            print(random_color(email))
    else:
        print(random_color("No emails found on the provided URL."))

if __name__ == "__main__":
    main()

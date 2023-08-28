import requests

urls = ['https://www.walmart.ca/', 'https://www.canadiantire.ca/', 'https://www.homehardware.ca/',
        'https://snapklik.com/', 'https://homeloft.ca/', 'https://www.walmart.com/', 'https://www.lifeandhome.com/']

for url in urls:
    try:
        # Attempt to fetch robots.txt for each website
        response = requests.get(f"{url}robots.txt")
        
        if response.status_code == 200:
            print(f"\nRobots.txt for {url}\n{'-'*40}\n{response.text}\n{'-'*40}")
        else:
            print(f"Couldn't fetch robots.txt for {url}. HTTP Status Code: {response.status_code}")
            
    except Exception as e:
        print(f"Error fetching robots.txt for {url}: {e}")

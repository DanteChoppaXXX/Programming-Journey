#!../bin/python3
import webbrowser

# Make a list of urls to open in browser
urls = ['google.com', 'facebook.com', 'instagram.com']

for url in urls:
    webbrowser.open(f"https://{url}")
    
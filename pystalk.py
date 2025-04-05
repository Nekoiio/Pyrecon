#!/usr/bin/env python3

import argparse
import requests
import whois
import dns.resolver
import exifread
import os
from colorama import Fore, Style

def check_username(username):
    print(f"{Fore.CYAN}[*] Checking username: {username}{Style.RESET_ALL}")
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Replit": f"https://replit.com/@{username}",
        "Snapchat (unconfirmed)": f"https://story.snapchat.com/@{username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Flickr": f"https://www.flickr.com/photos/{username}",
        "WhatsApp (unconfirmed)": f"https://wa.me/{username}",
        "Clubhouse": f"https://www.joinclubhouse.com/@{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "Disqus": f"https://disqus.com/by/{username}",
        "Slack": f"https://{username}.slack.com",
        "Behance": f"https://www.behance.net/{username}",
        "500px": f"https://500px.com/{username}",
        "Gist (GitHub)": f"https://gist.github.com/{username}",
        "Steemit": f"https://steemit.com/@{username}",
        "Ask.fm": f"https://ask.fm/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "LiveJournal": f"https://{username}.livejournal.com",
        "Xing": f"https://www.xing.com/profile/{username}",
        "Foursquare": f"https://foursquare.com/{username}",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "Ravelry": f"https://www.ravelry.com/users/{username}",
        "Twitch Clips": f"https://www.twitch.tv/{username}/clips"
    }

    for site, url in platforms.items():
        try:
            res = requests.get(url, timeout=5, headers={"User-Agent": "pystalk"})
            if res.status_code == 200:
                print(f"{Fore.GREEN}[+] Found on {site}: {url}{Style.RESET_ALL}")
            elif res.status_code == 404:
                print(f"{Fore.RED}[-] Not found on {site}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[!] {site}: Unexpected status {res.status_code}{Style.RESET_ALL}")
        except requests.RequestException:
            print(f"{Fore.YELLOW}[!] Error connecting to {site}{Style.RESET_ALL}")

def check_email(email):
    print(f"{Fore.CYAN}[*] Checking data breaches for email: {email}{Style.RESET_ALL}")
    headers = {"User-Agent": "pystalk-checker"}
    res = requests.get(f"https://haveibeenpwned.com/unifiedsearch/{email}", headers=headers)

    if res.status_code == 200:
        print(f"{Fore.RED}[!] Email found in breach data!{Style.RESET_ALL}")
    elif res.status_code == 404:
        print(f"{Fore.GREEN}[+] No breaches found.{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[!] Error or rate-limited. Status: {res.status_code}{Style.RESET_ALL}")

def check_domain(domain):
    print(f"{Fore.CYAN}[*] Fetching WHOIS and DNS for: {domain}{Style.RESET_ALL}")
    try:
        w = whois.whois(domain)
        print(f"{Fore.GREEN}[+] WHOIS info:\n{w}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] WHOIS failed: {e}{Style.RESET_ALL}")

    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f"{Fore.GREEN}[+] DNS A record: {rdata}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] DNS lookup failed: {e}{Style.RESET_ALL}")

def extract_metadata(file_path):
    print(f"{Fore.CYAN}[*] Extracting metadata from: {file_path}{Style.RESET_ALL}")
    if not os.path.isfile(file_path):
        print(f"{Fore.RED}[-] File not found.{Style.RESET_ALL}")
        return

    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
        for tag in tags.keys():
            print(f"{Fore.GREEN}[{tag}] {tags[tag]}{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="pyStalk - Simple OSINT CLI Tool")
    parser.add_argument('--user', help='Username to check across platforms')
    parser.add_argument('--email', help='Email address to check for breaches')
    parser.add_argument('--domain', help='Domain to fetch WHOIS and DNS info')
    parser.add_argument('--meta', help='Image or file to extract metadata')

    args = parser.parse_args()

    if args.user:
        check_username(args.user)
    if args.email:
        check_email(args.email)
    if args.domain:
        check_domain(args.domain)
    if args.meta:
        extract_metadata(args.meta)

if __name__ == "__main__":
    main()

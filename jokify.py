#!/usr/bin/env python3
"""jokify – fetch and display a random joke from JokeAPI.

A tiny, dependency‑free example of a CLI tool.
"""
import json
import sys
import urllib.request

API_URL = "https://v2.jokeapi.dev/joke/Any?type=single,twopart"


def fetch_joke():
    try:
        with urllib.request.urlopen(API_URL) as response:
            if response.status != 200:
                raise RuntimeError(f"Bad response: {response.status}")
            data = json.load(response)
            return data
    except Exception as e:
        sys.stderr.write(f"Error fetching joke: {e}\n")
        sys.exit(1)


def format_joke(joke_data):
    if joke_data.get("type") == "single":
        return joke_data.get("joke", "")
    elif joke_data.get("type") == "twopart":
        setup = joke_data.get("setup", "")
        delivery = joke_data.get("delivery", "")
        return f"{setup}\n{delivery}"
    else:
        return "No joke found."


def main():
    joke = fetch_joke()
    print(format_joke(joke))


if __name__ == "__main__":
    main()

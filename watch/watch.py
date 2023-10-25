import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    if matches := re.search(
        r'^.*<iframe src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+).*</iframe>.*$',
        s,
    ):
        new_URL = f"https://youtu.be/{matches.group(1)}"
        return new_URL
    else:
        return None


if __name__ == "__main__":
    main()

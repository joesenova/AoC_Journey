import os
import sys
import httpx
import datetime


def get_input_data(day: int, year: int) -> None:
    """ Gets the input for the day passed from the input api link
    :param day: The day of the month to use for the input get
    :param year: The year of the current/selected AoC to use for the input get
    """
    cookie = os.environ["AOC_COOKIE"]
    base_url = os.environ["AOC_BASE_URL"]

    cookies = {
        "session": cookie
    }

    url = f"{base_url}/{year}/day/{day}/input"
    resp = httpx.get(url, cookies=cookies)
    with open("input.txt", mode="w") as f:
        f.write(resp.text)


def main(day: int = None, year: int = None):
    if not day:
        day = datetime.date.today().day
    if not year:
        year = datetime.date.today().year
    get_input_data(day, year)


if __name__ == "__main__":
    sys.exit(main())

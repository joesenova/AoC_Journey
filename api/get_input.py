import os
import sys
import httpx
import datetime


def get_input_data(day: int) -> None:
    """ Gets the input for the day passed from the input api link
    :param day: The day of the month to use for the input get
    """
    cookie = os.environ["AOC_COOKIE"]
    base_url = os.environ["AOC_BASE_URL"]
    year = datetime.date.year

    cookies = {
        "session": cookie
    }
    resp = httpx.get(f"{base_url}/{year}/day/{day}/input", cookies=cookies)
    with open("input.txt", mode="w") as f:
        f.write(resp.text)


def main(day: int = None):
    if not day:
        day = datetime.date.today().day
    get_input_data(day)


if __name__ == "__main__":
    sys.exit(main())

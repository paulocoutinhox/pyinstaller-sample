import requests


def open_url(params):
    r = requests.get(url=params["url"])

    return "Status code: {0}".format(
        r.status_code,
    )

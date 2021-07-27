from datetime import datetime


def get_now(params):
    dt = datetime.fromtimestamp((params["timestamp"] / 1000))

    return "Created at {0}".format(
        dt.strftime("%Y-%m-%d %H:%M:%S"),
    )

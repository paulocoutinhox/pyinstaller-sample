import logging
import os
from contextlib import redirect_stdout
from io import StringIO

import webview

import api

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    # development path
    gui_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "gui",
        )
    )

    # frozen executable path
    if not os.path.exists(gui_dir):
        gui_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "gui",
        )

    # window
    is_debug = True if os.environ.get("PYWEBVIEW_DEBUG") == "1" else False

    api = api.API()
    url = os.path.abspath(os.path.join(gui_dir, "index.html"))

    if is_debug:
        url = "http://localhost:8080/index.html"

    window = webview.create_window(
        "My App",
        url=url,
        js_api=api,
        min_size=(800, 600),
    )

    webview.start(
        debug=is_debug,
        http_server=True,
    )

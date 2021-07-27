import webview


def select_folder():
    dirs = webview.windows[0].create_file_dialog(webview.FOLDER_DIALOG)

    if dirs and len(dirs) > 0:
        directory = dirs[0]

        if isinstance(directory, bytes):
            directory = directory.decode("utf-8")

        response = "Selected: {0}".format(directory)
    else:
        response = "Canceled"

    return response


def toggle_fullscreen():
    webview.windows[0].toggle_fullscreen()
    return "OK"

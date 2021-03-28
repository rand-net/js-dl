from .js_dl import *


def main():
    js_dl = JS_DL(
        "https://api.cdnjs.com/libraries", "https://cdnjs.cloudflare.com/ajax/libs"
    )

    sel_library = js_dl.list_all_libs()
    sel_version = js_dl.select_lib_version(sel_library)
    (lib_down_url, selected_library_file) = js_dl.get_lib_file_url(
        sel_library, sel_version
    )
    js_dl.download_lib_file(
        lib_down_url, selected_library_file, sel_library, sel_version
    )

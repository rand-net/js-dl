from prompt_toolkit import prompt
from art import *
import json
from prompt_toolkit.completion import (
    WordCompleter,
    Completer,
    FuzzyWordCompleter,
)
import requests


class JS_DL:
    def __init__(self, endpoint_url, download_url):
        self.endpoint_url = endpoint_url
        self.download_url = download_url
        tprint("js-dl")

    def list_all_libs(self):
        print("\nDownloading libraries list....")
        libraries_dict = requests.get(self.endpoint_url).text
        libraries = json.loads(libraries_dict)
        libraries_list = []
        for value in libraries["results"]:
            libraries_list.append(value["name"])

        libraries_completion = FuzzyWordCompleter(libraries_list)
        selected_library = prompt("\nLibrary: ", completer=libraries_completion)
        print(selected_library)
        return selected_library

    def select_lib_version(self, sel_library):
        # https://api.cdnjs.com/libraries/vue?fields=versions
        library_version_endpoint = (
            self.endpoint_url + "/" + sel_library + "?fields=versions"
        )
        library_versions = requests.get(library_version_endpoint).text
        library_versions = json.loads(library_versions)
        library_versions_list = []
        for version in library_versions["versions"]:
            library_versions_list.append(version)
        library_versions_completer = FuzzyWordCompleter(library_versions_list)
        selected_version = prompt("\nVersion: ", completer=library_versions_completer)
        print(selected_version)
        return selected_version

    def get_lib_file_url(self, sel_library, sel_version):
        # https://cdnjs.cloudflare.com/ajax/libs/vue/2.6.11/vue.js
        # https://api.cdnjs.com/libraries/vue/2.6.11?fields=files

        library_download_file_endpoint = (
            self.endpoint_url + "/" + sel_library + "/" + sel_version + "?fields=files"
        )
        library_files = requests.get(library_download_file_endpoint).text
        library_files = json.loads(library_files)
        file_path_urls = []
        for file in library_files["files"]:
            file_path_urls.append(file)

        library_file_completion = FuzzyWordCompleter(file_path_urls)
        selected_library_file = prompt("\nFile: ", completer=library_file_completion)

        # print(selected_library_file)

        library_download_url = (
            self.download_url
            + "/"
            + sel_library
            + "/"
            + sel_version
            + "/"
            + selected_library_file
        )
        return library_download_url, selected_library_file

    def download_lib_file(self, library_download_url, selected_library_file):
        print(library_download_url)
        file_content = requests.get(library_download_url).text
        with open(selected_library_file, "w") as f:
            f.write(file_content)


js_dl = JS_DL(
    "https://api.cdnjs.com/libraries", "https://cdnjs.cloudflare.com/ajax/libs"
)
sel_library = js_dl.list_all_libs()
sel_version = js_dl.select_lib_version(sel_library)
(lib_down_url, selected_library_file) = js_dl.get_lib_file_url(sel_library, sel_version)
js_dl.download_lib_file(lib_down_url, selected_library_file)

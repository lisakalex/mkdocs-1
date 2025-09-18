#!/home/al/.venv/bin/python3
import os
import json
import time
import requests
from datetime import datetime, timedelta, date
from collections import deque
from bs4 import BeautifulSoup
from dateutil import parser
import urllib.parse


class NewsUpdater:
    def __init__(self):
        self.start_time = time.time()
        self.today_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.count_replace = 1

    def process_files(self):
        for currentpath, _, files in os.walk('html/'):
            for file in files:
                if self.should_process_file(file, currentpath):
                    path_file = os.path.join(currentpath, file)
                    try:
                        with open(path_file) as file:
                            read_file = file.read()
                        self.replace_text(read_file, path_file)
                        print(f"{self.count_replace} {path_file}")
                        self.count_replace += 1
                    except Exception as e:
                        print(f"Error processing {path_file}: {e}")

    def should_process_file(self, file, currentpath):
        excluded_extensions = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.css', '.js', '.ico', '.woff2', '.woff')
        excluded_dirs = ('assets', 'paged')
        return not file.endswith(excluded_extensions) and not any(dir in currentpath for dir in excluded_dirs)

    def run(self):
        self.process_files()
        finish_time = round((time.time() - self.start_time) / 60, 2)
        print(f'Processed {self.count_replace - 1} files, time taken {finish_time} min')

        with open('count_replace.txt', "a") as file:
            file.write(f"{self.today_time} files {self.count_replace - 1}, time {finish_time} min\n")


if __name__ == '__main__':
    updater = NewsUpdater()
    updater.run()

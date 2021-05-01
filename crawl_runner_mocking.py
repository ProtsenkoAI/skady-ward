from time import sleep


class CrawlRunner:
    def __init__(self, tracker, config: dict):
        ...

    def run(self):
        while True:
            sleep(1)

    def stop(self):
        ...

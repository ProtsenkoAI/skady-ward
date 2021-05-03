from threading import Thread

from events_tracker_with_state import EventsTrackerWithState, TrackerState
from suvec.common.crawl_runner import CrawlRunner


class BackgroundCrawler(CrawlRunner):
    def __init__(self, crawler: CrawlRunner, crawl_tracker: EventsTrackerWithState):
        self.tracker = crawl_tracker
        self.crawler = crawler
        self.run_thread = Thread(target=self.crawler.run)

    def run(self):
        self.run_thread.start()

    def stop(self):
        self.crawler.stop()

    def get_tracker_state(self) -> TrackerState:
        # TODO: need to return standard state at the start
        return self.tracker.get_state()

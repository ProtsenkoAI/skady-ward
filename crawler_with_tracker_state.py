from threading import Thread

from crawl_runner_mocking import CrawlRunner, EventsTrackerWithState, TrackerState


class BackgroundCrawler:
    def __init__(self, config: dict):
        self.tracker = EventsTrackerWithState()
        self.crawl_runner = CrawlRunner(self.tracker, config)
        self.run_thread = Thread(target=self.crawl_runner.run)

    def run(self):
        self.run_thread.start()

    def stop(self):
        self.crawl_runner.stop()

    def get_tracker_state(self) -> TrackerState:
        # TODO: need to return standard state at the start
        return self.tracker.get_state()



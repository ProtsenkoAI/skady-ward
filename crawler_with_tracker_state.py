from crawl_runner_mocking import CrawlRunner

TrackerState = dict


class CrawlerWithTrackerState:
    def __init__(self, config: dict):
        self.tracker = EventsTrackerWithState()
        self.crawl_runner = CrawlRunner(self.tracker, config)

    def run(self):
        self.crawl_runner.run()

    def stop(self):
        self.crawl_runner.stop()

    def get_tracker_state(self) -> TrackerState:
        # TODO: need to return standard state at the start
        return self.tracker.get_state()


class EventsTrackerWithState:
    def get_state(self):
        return {}

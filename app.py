# TODO: move skady-user-vectorizer to dependencies/ and add them to gitignore

from PyQt5 import QtWidgets
import sys

from main_widget import MainWidget
from events_tracker_with_state import EventsTrackerWithState

from suvec.vk_api_impl.session.records_managing.records_storing import ProxyStorage, CredsStorage
from suvec.vk_api_impl.session.records_managing.records_storing.serializers import ProxyRecordsSerializer, CredsRecordsSerializer


if __name__ == "__main__":
    # TODO: need to create proxies and creds jsons if they aren't created yet

    qt_app = QtWidgets.QApplication([])
    # crawl_runner = VkApiCrawlRunner()
    # bg_crawler = BackgroundCrawler()

    proxies_save_pth = "/home/gldsn/Projects/skady-user-vectorizer/resources/proxies.json"
    creds_save_pth = "/home/gldsn/Projects/skady-user-vectorizer/resources/creds.json"

    proxy_storage = ProxyStorage(proxies_save_pth, ProxyRecordsSerializer())
    creds_storage = CredsStorage(creds_save_pth, CredsRecordsSerializer())

    events_tracker = EventsTrackerWithState()

    main_widget = MainWidget(events_tracker, proxy_storage, creds_storage,
                             crawler_kwargs={"parse_res_save_pth": "parsed.json"})

    main_widget.resize(800, 480)
    main_widget.show()

    sys.exit(qt_app.exec_())

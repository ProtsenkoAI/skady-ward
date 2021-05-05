from PyQt5 import QtWidgets
import sys
import os

from main_widget import MainWidget
from suvec.common.events_tracking import StatedEventsTracker

from suvec.vk_api_impl.session.records_managing.records_storing import ProxyStorage, CredsStorage
from suvec.vk_api_impl.session.records_managing.records_storing.serializers import ProxyRecordsSerializer, \
    CredsRecordsSerializer

if __name__ == "__main__":
    qt_app = QtWidgets.QApplication([])
    # crawl_runner = VkApiCrawlRunner()
    # bg_crawler = BackgroundCrawler()

    base_pth = "/home/gldsn/Projects/skady-user-vectorizer/resources/"

    proxies_save_pth = os.path.join(base_pth, "proxies.json")
    creds_save_pth = os.path.join(base_pth, "creds.json")

    proxy_storage = ProxyStorage(proxies_save_pth, ProxyRecordsSerializer())
    creds_storage = CredsStorage(creds_save_pth, CredsRecordsSerializer())

    events_tracker = StatedEventsTracker(log_pth=os.path.join(base_pth, "crawl_logs.txt"))

    crawler_kwargs = dict(
        requester_checkpoints_path=os.path.join(base_pth, "checkpoints/requester_checkpoint.json"),
        data_resume_checkpoint_save_pth=os.path.join(base_pth, "checkpoints/data_checkpoint.json"),
        long_term_save_pth=os.path.join(base_pth, "parsed_data.json")
    )

    main_widget = MainWidget(events_tracker, proxy_storage, creds_storage,
                             crawler_kwargs=crawler_kwargs)

    main_widget.resize(800, 480)
    main_widget.show()

    sys.exit(qt_app.exec_())

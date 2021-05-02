# TODO: when convert suvec to distributable package, remove its dependencies from skady-ward's pipfile
import sys
sys.path.append("/home/gldsn/Projects/skady-user-vectorizer/suvec")

from PyQt5 import QtWidgets
from main_widget import MainWidget
from crawler_with_tracker_state import BackgroundCrawler


if __name__ == "__main__":
    # TODO: set up suvec properly later and refactor imports
    from vk_api_impl.session.records_managing.records_storing import AuthRecordsStorage, CredsStorage
    from vk_api_impl.session.records_managing.records_storing.serializers import ProxyRecordsSerializer, CredsRecordsSerializer

    qt_app = QtWidgets.QApplication([])

    crawler = BackgroundCrawler(config={})

    proxies_save_pth = "/home/gldsn/Projects/skady-user-vectorizer/suvec/proxies.json"
    creds_save_pth = "/home/gldsn/Projects/skady-user-vectorizer/suvec/creds.json"

    proxy_storage = AuthRecordsStorage(proxies_save_pth, ProxyRecordsSerializer())
    creds_storage = CredsStorage(creds_save_pth, CredsRecordsSerializer())

    main_widget = MainWidget(crawler, proxy_storage, creds_storage)

    main_widget.resize(800, 480)
    main_widget.show()

    sys.exit(qt_app.exec_())

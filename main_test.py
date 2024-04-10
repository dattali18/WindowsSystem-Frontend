# external imports
import sys

from PySide6.QtWidgets import QApplication

# internal imports
from Tests import *
from Models import MoviesModel
from Controllers import MediaController
from Views import MediaView


# setting up a test for the media_controller

def test_media_controller():
    app = QApplication(sys.argv)

    view = MediaView()
    controller = MediaController(view, None)

    controller.show()

    sys.exit(app.exec())


def main():
    # test_media_controller()
    print("testing")


if __name__ == "__main__":
    main()

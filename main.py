import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QScreen

from Controllers import (
    LibrariesController,
    CreateLibraryController,
    UpdateLibraryController,
)
from Models import LibrariesModel, Models
from Views import LibrariesView, CreateLibraryView, UpdateLibraryView


def create_library_window() -> None:
    app = QApplication(sys.argv)

    view = CreateLibraryView()
    model = LibrariesModel()

    controller = CreateLibraryController(view=view, model=model)
    controller.show()
    sys.exit(app.exec())


def libraries_window() -> None:
    app = QApplication(sys.argv)

    view = LibrariesView()
    model = LibrariesModel()

    controller = LibrariesController(view=view, model=model)

    controller.view.show()

    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = view.frameGeometry()
    geo.moveCenter(center)
    view.move(geo.topLeft())

    sys.exit(app.exec())


def libraries_window() -> None:
    app = QApplication(sys.argv)

    view = LibrariesView()
    model = LibrariesModel()

    controller = LibrariesController(view=view, model=model)

    controller.view.show()

    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = view.frameGeometry()
    geo.moveCenter(center)
    view.move(geo.topLeft())

    sys.exit(app.exec())


def update_library_window() -> None:
    app = QApplication(sys.argv)

    view = UpdateLibraryView()
    view = UpdateLibraryView()
    model = Models()

    controller = UpdateLibraryController(view=view, model=model, library_id=1)

    controller.view.show()
    view.show()

    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = view.frameGeometry()
    geo.moveCenter(center)
    view.move(geo.topLeft())

    sys.exit(app.exec())


def main() -> None:
    libraries_window()


if __name__ == "__main__":
    main()

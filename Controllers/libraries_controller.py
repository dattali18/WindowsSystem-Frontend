class Frame1Controller:
    def __init__(self, libraries_model, movies_model, frame_view):
        self.libraries_model = libraries_model
        self.movies_model = movies_model
        self.frame_view = frame_view

        # Connect signals from the view to controller methods
        self.frame_view.back_btn.clicked.connect(self.handle_back_btn_clicked)
        self.frame_view.forward_btn.clicked.connect(self.handle_forward_btn_clicked)
        self.frame_view.search_btn.clicked.connect(self.handle_search_btn_clicked)
        self.frame_view.create_btn.clicked.connect(self.handle_create_btn_clicked)
        self.frame_view.update_btn.clicked.connect(self.handle_update_btn_clicked)

        # Populate initial data in the table
        self.populate_table()

    def populate_table(self):
        # Fetch data from the model and populate the table
        # movies = self.movies_model.get_movies()
        # self.populate_table_with_movies(movies)
        print("hi")

    def populate_table_with_movies(self, movies):
        # Clear existing rows in the table
        self.frame_view.playlist_table.setRowCount(0)

        # Populate the table with movies data
        for row, movie in enumerate(movies):
            self.frame_view.playlist_table.insertRow(row)
            self.frame_view.playlist_table.setItem(
                row, 0, QTableWidgetItem(movie.title)
            )
            # Add more columns as needed

    def handle_back_btn_clicked(self):
        # Handle back button click
        print("back button clicked")

    def handle_forward_btn_clicked(self):
        # Handle forward button click
        print("forward button clicked")

    def handle_search_btn_clicked(self):
        # Handle search button click
        print("search button clicked")

    def handle_create_btn_clicked(self):
        # Handle create button click
        print("create button clicked")

    def handle_update_btn_clicked(self):
        # Handle update button click
        print("update button clicked")

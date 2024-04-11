from Models import ImageModel


def test_get_image():
    image_url = "https://m.media-amazon.com/images/M/MV5BOTA5NjhiOTAtZWM0ZC00MWNhLThiMzEtZDFkOTk2OTU1ZDJkXkEyXkFqcGdeQXVyMTA4NDI1NTQx._V1_SX300.jpg"

    model = ImageModel()
    image: bytes = model.get_image(image_url)

    print(image)


def test_post_image():
    image_url = "https://m.media-amazon.com/images/M/MV5BMjExOTQ4MDMyMV5BMl5BanBnXkFtZTgwMTE3NDM2MzE@._V1_SX300.jpg"

    model = ImageModel()

    image: bytes = model.get_image(image_url)
    tags = model.post_image(image)

    print(tags[0:5])

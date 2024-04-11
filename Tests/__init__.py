from .movies_api_tests import (
    test_get_movie_id,
    test_get_movie_imdbID,
    test_get_movies,
    test_get_movies_search,
    test_movies_model,
    test_post_movie,
)
from .libraries_api_tests import (
    test_delete_libraries_id,
    test_delete_libraries_movies,
    test_delete_libraries_tvseries,
    test_get_libraries,
    test_get_libraries_name,
    test_get_library_id,
    test_get_library_movies,
    test_get_library_tvseries,
    test_post_libraries,
    test_post_libraries_movies,
    test_post_libraries_tvseries,
    test_put_libraries_id,
)
from .image_api_tests import test_get_image, test_post_image

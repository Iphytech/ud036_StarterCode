import webbrowser

# class definition.


class favourite_movies():
        # constructor for the class favourite_movies.
        def __init__(self, favourite_movie_title, favourite_movie_image, favourite_movie_url):  # NOQA
            # initializes favourite movies attributes
            self.title = favourite_movie_title
            self.collection_image = favourite_movie_image
            self.collection_youtube_url = favourite_movie_url


def display_favourite_movies(self):
    # opens the collection_youtube_url  in the default browser.
    webbrowser.open(self.collection_youtube_url)

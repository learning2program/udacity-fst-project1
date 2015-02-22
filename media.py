import webbrowser

class Movie():
    """Movie class definition

    Accepts a title, storyline, URL for poster image and a URL for the trailer.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Launches (opens) a webbrowser and displays the movies page
        """
        webbrowser.open(self.trailer_youtube_url)


import webbrowser


class Movie():
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):  # noqa
        """ initialize movie by passing movie attribute  """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """ open movie trailer on the default browser  """
        webbrowser.open_new(self.trailer_youtube_url)

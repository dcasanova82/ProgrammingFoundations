import webbrowser


class Video():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration, storyline, poster_image):
        self.title = title
        self.duration = duration
        self.storyline = storyline
        self.poster_image_url = poster_image


class Movie(Video):
    """ This class provides a way to store movie related information"""

    def __init__(self, title, duration, storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, duration, storyline, poster_image)
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """ This class provides a way to store tv show related information"""

    def __init__(self, title, duration, storyline, poster_image, episode, season):
        Video.__init__(self, title, duration, storyline, poster_image)
        self.episode = episode
        self.season = season
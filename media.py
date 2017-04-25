import webbrowser

#class movie to show listof movies and information about each

class Movie():

    """the constructor method , containing the movie,
     movie storyline, poster image and the movie trailer """
    
    def __init__(self,movie_title, movie_storyline, 
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

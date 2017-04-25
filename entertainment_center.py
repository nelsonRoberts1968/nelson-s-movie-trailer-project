import fresh_tomatoes
import media

# instances of movie class in media.py file

gladiator = media.Movie("The Gladiator",
                        "Roman empire warriors",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=l-kV68xPVnM")

training_day = media.Movie("Training Day",
                           "Corrupted cop in the streets of LA",
                           "https://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg",
                           "https://www.youtube.com/watch?v=JJbmI17uVjc")

troy = media.Movie("Troy",
                   "True love causes war between cities",
                   "https://upload.wikimedia.org/wikipedia/en/b/b8/Troy2004Poster.jpg",
                   "https://www.youtube.com/watch?v=Q3HquKCNkdE")

toy_story = media.Movie("Toy Story",
                        "story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Amrine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b8/This_Aint_Avatar.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
                     
        
the_matrix= media.Movie("The Matrix",
                        "the other world is controlled by eliens",
                        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=vKQi3bBA1y9")


# The movie array to load the movie list that gets uploded on the webpage

movies = [gladiator,training_day,troy,toy_story, avatar, the_matrix]
fresh_tomatoes.open_movies_page(movies)

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=e8GBfNo3IHY")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet author",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
interestellar = media.Movie("Interestellar",
                            "A space odyssey",
                            "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=zSWdZVtXT7E")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, interestellar]
# fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__module__)
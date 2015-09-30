import fresh_tomatoes
import media

# This file stores movie list in media class format :
# title, storyline(imdb link), poster_url, youtube_url
# class instance name is from its title in lower_cases

erin_brockovich = media.Movie("Erin Brockovich",
                              "http://www.imdb.com/title/tt0195685/",
                              "http://www.gstatic.com/tv/thumb/movieposters/24917/p24917_p_v7_aa.jpg",
                              "www.youtube.com/watch?v=9TjEklyF7-E")

hotel_rwanda = media.Movie("Hotel Rwanda",
                           "http://www.imdb.com/title/tt0395169/?ref_=fn_al_tt_1",
                           "http://www.gstatic.com/tv/thumb/movieposters/35240/p35240_p_v7_aa.jpg",
                           "www.youtube.com/watch?v=qZzfxL90100")

camille_claudel = media.Movie("Camille Claudel",
                              "http://www.imdb.com/title/tt2018086/?ref_=fn_al_tt_2",
                              "https://upload.wikimedia.org/wikipedia/en/f/f6/Camille_Claudel_1915_poster.jpg",
                              "https://youtu.be/UsB9QoMgr0I")

huit_femmes = media.Movie("8 Femmes",
                          "http://www.imdb.com/title/tt0283832/?ref_=fn_al_tt_1",
                          "https://upload.wikimedia.org/wikipedia/en/2/22/8-femmes-poster.jpg",
                          "www.youtube.com/watch?v=CAxqXsao2Ew")

# movies is a list of movies from above
movies = [erin_brockovich, hotel_rwanda, camille_claudel, huit_femmes]

# this will create html page
fresh_tomatoes.open_movies_page(movies)

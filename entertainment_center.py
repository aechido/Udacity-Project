import fresh_tomatoes
import media
sound_of_music = media.Movie("Sound of Music","a musical family fleeing oppression",
                             "https://cdn1.pamono.com/p/z/1/5/151327_rnr4dcg3cd/british-the-sound-of-music-film-poster-by-howard-terpning-1965-1.jpg",
                             "https://www.youtube.com/watch?v=lEcKXr3mJ_o")


#sound_of_music.show_trailer()

oliver = media.Movie("Oliver","an orphan is taken in by a gang of thieves","http://www.oliver1968.co.uk/lbyus2.jpg",
                     "https://www.youtube.com/watch?v=ImKgBACucAw")

hidden_figures = media.Movie("Hidden Figures","African American women helps NASA during the space race",
                              "http://cdn-static.denofgeek.com/sites/denofgeek/files/styles/gallery_adv/public/2016/11/hidden_figures_0.jpg?itok=fNiXfMIo",
                              "https://www.youtube.com/watch?v=RK8xHq6dfAo")

the_bodyguard = media.Movie("The Bodyguard", "a famous singer needs protection from a stalker",
                             "http://www.moviesongs.com/wp-content/uploads/2015/08/bodyguard.jpg",
                             "https://www.youtube.com/watch?v=4JFRdJTszRM")

dirty_dancing = media.Movie("Dirty Dancing", "a girl learns to dance from an off-limits professional dancer",
                             "https://www.movieposter.com/posters/archive/main/66/MPW-33382",
                             "https://www.youtube.com/watch?v=eIcmQNy9FsM")

center_stage = media.Movie("Center Stage", "a group of young people pursues ballet career",
                           "http://images4.fanpop.com/image/photos/22300000/Movie-Poster-center-stage-22390463-1379-2068.jpg",
                           "https://www.youtube.com/watch?v=b9Lk0dY_Arw")

movies = [sound_of_music, oliver, hidden_figures, the_bodyguard, dirty_dancing, center_stage]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

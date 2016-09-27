# coding=utf-8
import media
import fresh_tomatoes
toystory = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life.",
    "http://vignette4.wikia.nocookie.net/pixar/images/c/ca/Toy_story_ver1_xlg.jpg/revision/latest?cb=20110515142143",  # noqa
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "By 2154, humans have depleted Earth's natural resources, leading to a severe energy crisis.",  # noqa
    "http://resizing.flixster.com/7j4Uky7sPOl5jUPSL2JBIDjeCvk=/800x1200/v1.bTsxMTE3Njc5MjtqOzE3MTkxOzIwNDg7ODAwOzEyMDA",  # noqa
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

airforceone = media.Movie(
    "Air Force One",
    "American and Russian Special Forces capture General Ivan Radek (Jürgen Prochnow)",  # noqa
    "https://upload.wikimedia.org/wikipedia/en/2/2a/Air_Force_One_(movie_poster).jpg",  # noqa
    "https://www.youtube.com/watch?v=vIHPP7c6GNU")

robot = media.Movie(
    "Robots ",
    "In Rivet Town, Rodney Copperbottom is a young inventor who dreams of making the world a better place)",   # noqa
    "http://www.impawards.com/2005/posters/robots.jpg",  # noqa
    "https://www.youtube.com/watch?v=p9X16KPOgFI")

"""call open_movies_page() to generate html file and open it on browser"""
fresh_tomatoes.open_movies_page(movies=[toystory, avatar, airforceone, robot])

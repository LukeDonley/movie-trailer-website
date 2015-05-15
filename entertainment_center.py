import fresh_tomatoes
import media

# Initialize and define instances of Movie
persona = media.Movie(
  "Persona",
  "A nurse is put in charge of an actress who can't talk "
  "and finds that the actress's persona is melding with hers.",
  "https://upload.wikimedia.org/wikipedia/en/0/08/Persona_Poster.jpg",
  "https://www.youtube.com/watch?v=3rtSjV_gFkw",
  "1966",
  "Ingmar Bergman")
cries_and_whispers = media.Movie(
  "Cries & Whispers",
  "When a woman dying of cancer in early twentieth-century Sweden is visited "
  "by her two sisters, long-repressed feelings between the siblings rise to "
  "the surface.",
  "http://www.gstatic.com/tv/thumb/movieposters/6653/p6653_p_v7_aa.jpg",
  "https://www.youtube.com/watch?v=6Pw7FYex5pQ",
  "1972",
  "Ingmar Bergman")
seventh_seal = media.Movie(
  "The Seventh Seal",
  "A man seeks answers about life, death, and the existence of God as he "
  "plays chess against the Grim Reaper during the Black Plague.",
  "https://upload.wikimedia.org/wikipedia/en/6/69/Seventhsealposter.jpg",
  "https://www.youtube.com/watch?v=NtkFei4wRjE",
  "1957",
  "Ingmar Bergman")
weekend = media.Movie(
  "Weekend",
  "A supposedly idyllic weekend trip to the countryside turns into a never-"
  "ending nightmare of traffic jams, revolution, cannibalism and murder",
  "http://p2.la-img.com/1144/26856/10187638_1_x.jpg",
  "https://www.youtube.com/watch?v=dFJLuhVvBPM",
  "1967",
  "Jean-Luc Godard")
days_of_heaven = media.Movie(
  "Days of Heaven",
  "A hot-tempered farm laborer convinces the woman he loves to marry their "
  "rich but dying boss so that they can have a claim to his fortune.",
  "http://blog.freepeople.com/wp-content/uploads/2012/12/Untitled-414.jpg",
  "https://www.youtube.com/watch?v=EzZ8phk8yYc",
  "1978",
  "Terrence Malick")
my_life_to_live = media.Movie(
  "My Life To Live",
  "Twelve episodic tales in the life of a Parisian woman "
  "and her slow descent into prostitution.",
  "https://40.media.tumblr.com/7fcaaa717e2ffe1bfc6bee2d3b489cbc"
  "/tumblr_nnbw10QqXK1rjxpgao1_500.jpg",
  "https://www.youtube.com/watch?v=dfZQpLSuxKE",
  "1962",
  "Jean-Luc Godard")
stroszek = media.Movie(
  "Stroszek",
  "In Berlin, an alcoholic man, recently released from prison, joins his "
  "elderly friend and a prostitute in a determined dream to leave Germany "
  "and seek a better life in Wisconsin.",
  "http://upload.wikimedia.org/wikipedia/en/2/20/Stroszek_poster.JPG",
  "https://www.youtube.com/watch?v=cNVnlk6q1es",
  "1977",
  "Werner Herzog")
fitzcarraldo = media.Movie(
  "Fitzcarraldo",
  "The story of Brian Sweeney Fitzgerald, an extremely determined man who "
  "intends to build an opera house in the middle of a jungle.",
  "https://s-media-cache-ak0.pinimg.com/originals/22/8a/d0/"
  "228ad007cea85f41515690d9a4c93d5a.jpg",
  "https://www.youtube.com/watch?v=F53yUsgVuL0",
  "1982",
  "Werner Herzog")
seven_samurai = media.Movie(
  "Seven Samurai",
  "A poor village under attack by bandits recruits seven "
  "unemployed samurai to help them defend themselves.",
  "https://www.movieposter.com/posters/archive/main/6/MPW-3125.jpg",
  "https://www.youtube.com/watch?v=7mw6LyyoeGE",
  "1954",
  "Akira Kurosawa")

# Create array of Movie objects to populate movie page
movies = [persona,
          cries_and_whispers,
          seventh_seal, weekend,
          days_of_heaven,
          my_life_to_live,
          fitzcarraldo,
          stroszek,
          seven_samurai]

# Call open_movies_page to create the Movies page
fresh_tomatoes.open_movies_page(movies)

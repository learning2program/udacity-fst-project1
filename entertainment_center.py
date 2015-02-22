#!/usr/bin/env python
import fresh_tomatoes
import media

shawshank_redemption = media.Movie("Shawshank Redemption",
                        "Andy Dufresne (Tim Robbins) is sentenced to two consecutive life terms in prison for the "
                        "murders of his wife and her lover and is sentenced to a tough prison. However, "
                        "only Andy knows he didn't commit the crimes. While there, he forms a friendship with "
                        "Red (Morgan Freeman), "
                        "experiences brutality of prison life, adapts, helps the warden, etc., all in 19 years.",
                        "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=K_tLp7T6U1c")

Unbroken = media.Movie(
    "Unbroken",
     "As a boy, Louie Zamperini is always in trouble, but with the help of his older brother he turns his life around and channels his energy into running, later qualifying for the 1936 Olympics. When World War II breaksout, Louie enlists in the military. After his plane crashes in the Pacific, he survives an incredible 47 days adrift in a raft, until his capture by the Japanese navy. Sent to a POW camp, Louie becomes the favorite target of a particularly cruel prison commander.",
     "http://upload.wikimedia.org/wikipedia/en/7/76/Unbroken_poster.jpg",
     "http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dkk1M_HwmFMM&ei=g2nlVMbqIoKkoQSU6IDQAQ&usg=AFQjCNHhVWyq92Fodphb6TPEYvskF69HVA&sig2=o39OFm_K0HoG_HJEDIFxfg&bvm=bv.86475890,d.cGU")

everything_is_illuminated = media.Movie("Everything is Illuminated",
                                        "A young Jewish-American man obsessed with his family history, ",
                                        "http://upload.wikimedia.org/wikipedia/en/2/27/Everything_Is_Illuminated_film.jpg",
                                        "https://www.youtube.com/watch?v=tSUOYY4oukc")

movies = [ shawshank_redemption, Unbroken, everything_is_illuminated  ]
fresh_tomatoes.open_movies_page(movies)
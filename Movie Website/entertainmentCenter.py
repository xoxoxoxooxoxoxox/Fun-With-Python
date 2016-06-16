import freshTomatoes
import movie

insideOut = movie.Movie("Inside Out", 
						"After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house, and school.",
						"https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
						"https://www.youtube.com/watch?v=1t0A_tZGrYw")

xMenApocalypse = movie.Movie("X Men: Apocalypse", 
							"With the emergence of the world's first mutant, Apocalypse, the X-Men must unite to defeat his extinction level plan.", 
							"https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg",
							"https://www.youtube.com/watch?v=Jer8XjMrUB4")	

captainAmerica = movie.Movie("Captain America: Civil War",
							"Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man.",
							"https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
							"https://www.youtube.com/watch?v=dKrVegVI0Us")

meBeforeYou = movie.Movie("Me Before You", 
							"A girl in a small town forms an unlikely bond with a recently-paralyzed man she's taking care of.", 
							"https://upload.wikimedia.org/wikipedia/en/f/fd/Me_Before_You_%28film%29.jpg",
							"https://www.youtube.com/watch?v=uEv57GJzHMw")

nowYouSeeMe2 = movie.Movie("Now You See Me 2", 
							"The Four Horsemen resurface and are forcibly recruited by a tech genius to pull off their most impossible heist yet.",
							"https://upload.wikimedia.org/wikipedia/en/9/9a/Now_You_See_Me_2_poster.jpg", 
							"https://www.youtube.com/watch?v=AuEjHzOIgBE")

findingDory = movie.Movie("Finding Dory", 
						"The friendly-but-forgetful blue tang fish reunites with her loved ones, and everyone learns a few things about the real meaning of family along the way.",
						 "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg", 
						 "https://www.youtube.com/watch?v=MKJA-VLpiCo")

movies = [insideOut, xMenApocalypse, captainAmerica, meBeforeYou, nowYouSeeMe2, findingDory]
freshTomatoes.open_movies_page(movies)
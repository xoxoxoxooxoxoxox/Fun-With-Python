import webbrowser

class Movie():
	def __init__(self, movieTitle, storyLine, moviePoster, youTubeLink):
		self.title = movieTitle
		self.storyLine = storyLine
		self.poster_image_url = moviePoster
		self.trailer_youtube_url = youTubeLink
		
	def playTrailer(self):
		webbrowser.open(self.trailer_youtube_url)
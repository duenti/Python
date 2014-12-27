import webbrowser
#Aspas tripla cria documentacao, que e acessivel por __doc__()
class Music():
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __name__(self):
		return "Music"

	def __init__(self,band,year,cover,audio):
		self.band = band
		self.year = year
		self.cover = cover
		self.audio = audio

	def play(self):
		webbrowser.get('/usr/bin/google-chrome %s').open(self.audio)

class Album(Music):
	"""Classe para armazenamento de dados relacionado a albuns de musica"""

	def __name__(self):
		return "Album"

	def __init__(self,band,year,cover,audio,album):
		Music.__init__(self,band,year,cover,audio)
		self.name = album

class Live(Music):
	"""Classe para armazenamento de dados relacionado a apresentacoes ao vivo de bandas"""

	def __name__(self):
		return "Album"

	def __init__(self,band,year,cover,audio,location):
		Music.__init__(self,band,year,cover,audio)
		self.location = location

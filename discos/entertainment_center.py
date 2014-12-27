import media
import html_maker
	
sebtp = media.Album("Selling Egland By The Pound",
						 "Genesis",
						 1973,
						 "http://consultoriadorock.com/wp-content/uploads/2013/10/Selling-England-By-The-Pound1.jpg",
						 "http://www.youtube.com/watch?v=7Rn9tzirks4")

mirage = media.Album("Mirage",
					 "Camel",
					 1974,
					 "http://ecx.images-amazon.com/images/I/61-XFjwAHUL.jpg",
					 "http://www.youtube.com/watch?v=PbD85j1PuPw")

mutantes = media.Album("Os Mutantes",
					   "Os Mutantes",
					   1969,
					   "http://sp5.fotolog.com/photo/53/28/109/music_is_my_dope/1206487413_f.jpg",
					   "http://www.youtube.com/watch?v=I_tp4fdO-YU")

harvest = media.Album("Harvest",
					  "Neil Young",
					  1972,
					  "http://1.bp.blogspot.com/-aJ5ISXydup8/UBqjdJolYkI/AAAAAAAAAuk/V3j3oc7MUdM/s1600/YoungNeil-Harvest.jpg",
					  "http://www.youtube.com/watch?v=8odlwI94uFA")

dejavu = media.Album("Deja Vu",
					 "Crosby, Stiils, Nash & Young",
					 1970,
					 "http://leskeud.com/wp-content/uploads/2013/08/Dj+Vu+Crosby+Stills+Nash++Young++Dj.png",
					 "http://www.youtube.com/watch?v=UIrUAHaNvCI")

loki = media.Album("Loki?",
				   "Arnaldo Baptista",
				   1974,
				   "http://consultoriadorock.com/wp-content/uploads/2013/06/1275582687_arnald11.jpg",
				   "http://www.youtube.com/watch?v=x64aNMRtsgI")

albuns = [sebtp,mirage,mutantes,harvest,dejavu,loki]
#html_maker.open_albuns_page(albuns)
print(sebtp.__name__(),sebtp.__module__())
import urllib

def read_text():
	quotes = open('movie_quotes.txt')
	content = quotes.read()
	quotes.close()
	return content

def check_profanity(text):
	connection = urllib.urlopen('http://www.wdyl.com/profanity?q=' + text)
	output = connection.read()
	connection.close()
	print(output[14])
	if(output[14] == 't'):
		return True
	return False

text = read_text()
boolea = check_profanity(text)
print(boolea)
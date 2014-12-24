import os
import time

url = 'https://www.youtube.com/watch?v=f8SfDZ65A0o'

print('Alarme foi ativado em ' + time.ctime())
for x in xrange(3):
	time.sleep(4) #10s
	webbrowser.get('/usr/bin/google-chrome %s').open("http://www.youtube.com")
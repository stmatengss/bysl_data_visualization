#-*- coding: UTF-8 -*- 
import web
import sys
from web.contrib.template import render_jinja
import codecs

reload(sys)  
sys.setdefaultencoding('utf8') 

urls = ('/', 'Upload')

render = render_jinja("template", encoding="utf-8")

class Upload:
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		return getattr(render,'index')()

	def POST(self):
		input = web.input()
		x = input.myfile
		y = input.algorithm
		print y
		filedir = 'D:/working/bysj/data' # change this to the directory you want to store the file in.
		if 'myfile' in x: # to check if the file-object is created
			filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
			filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
			fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
			fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
			fout.close() # closes the file, upload complete.
		raise web.seeother('/')


if __name__ == "__main__":
	app = web.application(urls, globals()) 
	app.run()
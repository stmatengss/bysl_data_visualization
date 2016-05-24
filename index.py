#-*- coding: UTF-8 -*- 
import web
import sys
import json
from web.contrib.template import render_jinja
import codecs
import shutil
import os
import os.path
import draw

reload(sys)  
sys.setdefaultencoding('utf8') 

urls = ('/', 'Upload',
        '/result', 'Result',
		'/down', 'Down')

render = render_jinja("template", encoding="utf-8")

class Down:
	def GET(self):
		data = {
			'url' : "data/test.txt"
		}
		return json.dumps(data)

class Result:
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		return getattr(render,'result')()

class Upload:
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		return getattr(render,'index')()

	def POST(self):
		input = web.input()
		x = web.input(myfile={})
		y = input.algorithm
		core_num = input.cores
		worker_num = input.workers
		memory_num = input.memory
		#filedir = 'D:/working/bysj/data' # change this to the directory you want to store the file in.
		if 'myfile' in x: # to check if the file-object is created
			print "success"
			#filepath=input.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
			#filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
			fout = open('data/test2.txt','w') # creates the file where the uploaded file should be stored
			fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
			fout.close() # closes the file, upload complete.
		
		shutil.copy('data/test2.txt','static/output/res.txt')
		draw.draw_simple('static/output/res.txt')
		
		
		raise web.seeother('/result')
		#return getattr(render,'index')()


if __name__ == "__main__":
	app = web.application(urls, globals()) 
	app.run()

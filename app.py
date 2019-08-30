from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from flask import request
import mobinet
import os
import keras
from random import sample
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
Bootstrap(app)
UPLOAD_FOLDER = '/'
class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/signup' , methods=['GET', 'POST'])
def signup():
	form = PhotoForm()
	if form.validate_on_submit():
		if ((form.photo.data).filename[-4:]!=".png") and ((form.photo.data).filename[-4:]!=".jpg") and ((form.photo.data).filename[-5:]!=".JPEG"):
			return '<h1>we only accept images with png , jpg or JPEG extentions you gave us '+(form.photo.data).filename[-4:]+'</h1>'
		f = request.files['photo']
		f.save(secure_filename(f.filename))
		l=mobinet.main(f.filename)
		os.remove(f.filename)
		if len(l[0])==0:
			return '<h1> :( sadly no picture in our database resambels your photo</h1>'
		else:
			ch=""
			s=0
			for i in range(len(l[0])):
				if s==0:
					ch=ch+"<tr><td style='width:25%;height:200px;'><table style='width:100%;height:200px;'><tr><td><h3 align='center'>"+str(l[2][i]/3.41)+"%</h3></td></tr><tr><td><img style='width:100%;height:200px;' src="+'"static/base/'+l[0][i]+'"></td></tr></table></td></tr>'
					s=s+1
				elif s==1 or s==2:
					s=s+1
					ch=ch[:-5]
					ch=ch+"<td style='width:25%;height:200px;'><table style='width:100%;height:200px;'><tr><td><h3 align='center'>"+str(l[2][i]/3.41)+"%</h3></td></tr><tr><td><img style='width:100%;height:200px;' src="+'"static/base/'+l[0][i]+'"></td></tr></table></td></tr>'
				else:
					s=0
					ch=ch[:-5]
					ch=ch+"<td style='width:25%;height:200px;'><table style='width:100%;height:200px;'><tr><td><h3 align='center'>"+str(l[2][i]/3.41)+"%</h3></td></tr><tr><td><img style='width:100%;height:200px;' src="+'"static/base/'+l[0][i]+'"></td></tr></table></td></tr>'
		return "<!DOCTYPE html><html><head><title>Summer Project</title></head><body><table style='height: 100%;width: 100%'><tr><td colspan=100%><table style='width: 100%'><tr><td align='center'><h1 align='center'>your picture is probably:</h1></td></tr><tr><td align='center'><h1 align='center'>"+l[1]+"</h1></td></tr><tr><td align='center'><h1 align='center'>These are the images that are the closest to your photo</h1></td></tr></table></td></tr>"+ch+"</table></body></html>"
	return render_template('signup.html', form=form)
@app.route('/list' , methods=['GET', 'POST'])
def list()
	with open('register.txt') as myfile:
		l=myfile.readlines()
	s=0
	ch=""
	for i in sample(l,100):
		j=i.split()
		if s==0:
			ch=ch+"<tr><td style='width:25%;height:200px;'><table style='width:100%;height:200px;'><tr><td><h3 align='center'>"+str(j[1])+"</h3></td></tr><tr><td><img style='width:100%;height:200px;' src="+'"static/base/'+j[0]+'"></td></tr></table></td></tr>'
			s=s+1
		elif s==1 or s==2:
			s=s+1
			ch=ch[:-5]
			ch=ch+"<td style='width:25%;height:200px;'><table style='width:100%;height:200px;'><tr><td><h3 align='center'>"+str(j[1])+"</h3></td></tr><tr><td><img style='width:100%;height:200px;' src="+'"static/base/'+j[0]+'"></td></tr></table></td>'
		else:
			s=0
			ch=ch[:-5]
			ch=ch+"<td style='width:25%;height:200px;'><table style='width:100%;height:200px;'><tr><td><h3 align='center'>"+str(j[1])+"</h3></td></tr><tr><td><img style='width:100%;height:200px;' src="+'"static/base/'+j[0]+'"></td></tr></table></td></tr></tr>'
	return "<!DOCTYPE html><html><head><title>Summer Project</title></head><body><table style='height: 100%;width: 100%'><tr><td colspan=100% align='center'><h1>these are the data set elements</h1></td></tr>"+ch+"</table></body></html>
if __name__ == '__main__':
    app.run(debug=True)

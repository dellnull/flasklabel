from flask import Flask, request, render_template_string, render_template
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
Bootstrap(app)
app.config.update(
    TESTING=False,
    SECRET_KEY='O24{Flask_Flag_Failure}'
)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result')
def label_template():
	bottle = {'label':"My Personal Label", 'secret':"UGhldmJoZj8gYWl2ZnZoei5wYnovcG5lcnJlZg=="}
	if request.args.get('label'):
		bottle['label'] = request.args.get('label')
	template = '''<h2>%s</h2>''' % bottle['label']
	return render_template_string(template, bottle=bottle)


if __name__ == "__main__":
	app.run(debug=True)

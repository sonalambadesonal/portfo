from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def about(page_name):
	return render_template(page_name)


def write_to_file(data):
	with open('database.txt', mode='a') as database:
		emails = data["email"]
		subjects = data["subject"]
		messages = data["message"]
		file = database.write(f'\n{emails},{subjects},{messages}')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		emails = data["email"]
		subjects = data["subject"]
		messages = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([emails,subjects,messages])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')

		except:
			return 'did not save to database'

	else:
		return 'Something Went Wrong. Try again!'



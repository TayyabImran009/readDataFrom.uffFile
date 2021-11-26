After opning the project on your terminal install the dependencies:

Run on your terminal to install all the required packages:
	pip install -r requirements.txt
To get the clone of the data from git url type:
	git clone https://gist.github.com/de956088bab2a9168c7647fdf1be7cc5.git
Open the python shell for some python commands:
	python manage.py shell
To import some important libraries type:
	import os
	import csv
Import table from models.py type:
	from getData.models import info
Change the type of the file type:
	os.rename('de956088bab2a9168c7647fdf1be7cc5/DTC5259515123502080915D0010.uff','de956088bab2a9168c7647fdf1be7cc5/DTC5259515123502080915D0010.csv')
Now open the file:
	with open('de956088bab2a9168c7647fdf1be7cc5/DTC5259515123502080915D0010.csv') as f:
Read the file:
	reader = csv.reader(f)
Now make loop to add all the data to the data base:
	for row in reader:
		d = info(data=row)
		d.save()
Now exit the python shell by pressing:
	ctrl+d
confirm by pressing:
	y and enter
To see the data at admin panel run the project by typing:
	python manage.py runserver
To open admin panel open the browser and enter the url:
	http://localhost:8000/admin
Type the user name and passwrd:
	username: admin
	password: admin123
Click on infos to see all your data

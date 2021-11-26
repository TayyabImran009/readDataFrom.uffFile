After opning the project on your terminal
pip install -r requirements.txt // Run on your terminal
git clone https://gist.github.com/de956088bab2a9168c7647fdf1be7cc5.git // Run on your terminal
python manage.py shell // Run on your terminal
import os // Run on your terminal
import csv // Run on your terminal
from getData.models import info // Run on your terminal
os.rename('de956088bab2a9168c7647fdf1be7cc5/DTC5259515123502080915D0010.uff','de956088bab2a9168c7647fdf1be7cc5/DTC5259515123502080915D0010.csv') // Run on your terminal
with open('de956088bab2a9168c7647fdf1be7cc5/DTC5259515123502080915D0010.csv') as f: // Run on your terminal
reader = csv.reader(f) // Run on your terminal
for row in reader: // Run on your terminal
d = info(data=row) // Run on your terminal
d.save() // Run on your terminal
press ctrl+d
press y and enter
python manage.py runserver // Run on your terminal
http://localhost:8000/admin // Open browser and enter the url
username: admin // write username
password: admin123 // write password

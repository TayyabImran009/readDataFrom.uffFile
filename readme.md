## After opning the project on your terminal:
### To install all the required packages run:
```
pip install -r requirements.txt
```
### To get a clone of the data from git url run:
```
git clone https://gist.github.com/de956088bab2a9168c7647fdf1be7cc5.git
```
### Open the python shell for some python code:
```
python manage.py shell
```
### Now import some important libraries run:
```
import os
```
```
import csv
```
### Import table from models.py:
```
from getData.models import info
```
### Change the type of the file:
```	
os.rename('de956088bab2a9168c7647fdf1be7cc5/DTC5259515123502080915D0010.uff','de956088bab2a9168c7647fdf1be7cc5/DTC5259515123502080915D0010.csv')
```
### Now open the file:
```
with open('de956088bab2a9168c7647fdf1be7cc5/DTC5259515123502080915D0010.csv') as f:
```
### Read the file:
```
reader = csv.reader(f)
```
### Now make loop to add all the data to the database:
```
for row in reader:
	d = info(data=row)
	d.save()
```
### Now exit the python shell by pressing:
> ctrl+d <br/>
confirm by typing y and then press enter.
### To see the data at admin panel run the project by typing:
```	
python manage.py runserver
```
### To open admin panel open the browser and enter the url:
```	
http://localhost:8000/admin
```
### Type the user name and passwrd:
> username: admin <br />
> password: admin123
## Click on infos to see all your data

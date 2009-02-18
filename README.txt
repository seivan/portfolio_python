The content of this folder should look like

MyPortfolio/
	README.txt
	doc/
		installation.txt
		manual.pdf
		
	web/
		images/
			*
		style/
			style.css

		templates/
			list.kid, project.kid, techniques.kid
		
		data.csv
		data.py
		index.html
		list.py
		project.py
		techniques.py
/

/README.txt
This is the file you are reading at the moment.
It's more a of readme over the files an folders and not an actual readme over
the project. Consider this a 'map' explaining the 'whats' and 'wheres' of 
of this project.


/doc/
Manual covering both installation and usage.

/doc/installation.txt
This file covers how to install the portfolio combined with installation 
directions for the required applications.
Such requirements are; Python, Apache, mod_python and Kid-templating.
The file does not take on installation guide for eg Apache, but on how to 
aquire, install and modify Apache to work with the portfolio.

/doc/csv.txt
This is the file that explains how to use it, 
eg, explaination on how to change the content of the data.csv file to show 
what you want. 

/doc/guide.pdf
Guide over the different parts of the system

/doc/data_testing.txt
Explains the output and data-format looks like.
There also be explanation of different parts of the project and the functions in the data-layer also putting on some testing against the
functions.

/doc/presentation_testing.txt
Testing the system with two others

/doc/diary_*
Diary over our projects

/doc/svn.log
Our svn log

/doc/documentation.html
/doc/html/index.html
Documentation over our code and functions
with comments.

/web/
The 'web' folder is where the presentation-layer is located.
It's the front-end of the system.

/web/log.txt
Logfile

/web/images
Images should be stored in the 'images' folder, as it is right now it's empty,
but can be added if desired, more of this is in the actual manual.
Only images used on the website as portfolio content are stored in this folder
so the images required for eg the style sheet is stored in another folder

web/style/
This is where the .css file is and images required for the website layout are.

/web/templates/
Here are the kid templates that generate valid xhtml.
The front-end so to speak.
These are used in conjuction with the .py files in /web/
More about these files are in the manual.
You could say, that these files are the presentation layers
More in the /doc/manual.pdf

/web/data.csv
This is where the content on the portfolio is stored, it's a
'comma-separated values' file. The CSV-filecould be called 'database', this is the file you fill with the content you want it to be shown on the front-end.
That is, what you type in here, is what is shown on the website.
More in the /doc/manual.pdf

/web/data.py
The backbone and structure of the portfolio.
This is the data-layer where the interaction with data.csv is done.
It reads the content of the .csv file, it modify the way the file is presented
then to organize it to be used in conjuction with the front-end, the 
presentation layers in the /web/templates/*.kid
More in the /doc/manual.pdf

/web/index.html
First front page, static xhtml with the css-file.
The actual design is here, and just copied on to the /web/*.kid files.

/web/*.py
These (except data.py) are the files to make sure that xhtml can be used with
python, these files are used within mod_python to show python-content online 
with apache.
These are linked to the /web/*.kid files.
More in the /doc/manual.pdf

If you have any suggestions or comments, please mail us.

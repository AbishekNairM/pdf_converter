# pdf_converter 
this is a base line submission link for a problem for a startup that requires u to extract data and show it to the user.
cd pdfconverter
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
cntrl-click to run django project
upload an image of a pdf file(jpg,png,etc)
u will get an output page showing all the information that was retrieved.

OCR is used using pytesseract to extract the text. I am familiar with only the basic flow of django, rest all i figured through online resources like: chatgpt for everything, 
for django i used: https://realpython.com/get-started-with-django-1/#projects-app-models and https://docs.djangoproject.com/en/4.2/intro/tutorial01/
for image extraction i used: https://nanonets.com/blog/how-to-extract-data-from-invoices-using-python/ now i chose the OCR method because upon asking doubts to the recruiter, i was hinted towards using OCR but the implementation is very elementary
i used chatgpt to make the django form of the above code from the site and played around with it.
since i had almost zero experience with github i used: chatgpt(obviously) and https://www.jcchouinard.com/create-your-first-github-project-in-vscode/#How_to_Publish_to_Github_from_VSCode to push the folder

Challenges i faced: i first tried reading with NER, i got nothing. I tried manya arbritary methods chatgpt came and could get only get header values. Then i searched for the implementation mentioned and came across pytesseract. Seemingly it used OCR and i was still unable to read anything probably cause my code was imperfect. Then i asked a doubt to the examiner and He told me that OCR will be used. when i used the sites code, i was able too read a majority of the words in the image. I tried using preprocessing but it read even less but showed values that weren't marked before. So i tried merging it and read more values but extraction was still difficult. In the end i found a similar implementation and used it as a base and used chatgpt to code it.  

I am a fresher that was effected by covid and a 2022 passout from a normal tier-3 college, I aspire to be a software engineer and am willing to learn under anybody to become a full time software engineer.
so if u have any suggestions, links, job oppurtunities, anything please do contact my mail: abisheknair.m1999@gmail.com

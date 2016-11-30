# Data-Rep
### A To Do List
### Project for Data Representation and Querying 

HI, I created this programe for my module Data Representation and Querying. I chose to do a To Do list for this project. I wanted this program to take input from users and save the data input into a database using sqlite3. When the information is input the program will save it in the database and also make the newly saved information visible in the database and underneath where the information was input. At the bottom of the page there is a list called Most forgotten items, I thaught this was a clever extra as even though we use to-do lists we still often forget to write things in them, so the this is just a list comprised of the most forgoetten items.The program is written mostly in Python and HTML. It also uses Flask, Jquery, CSS and javascript.


### Learning experience
I learned a lot from this project, I have never programed in python before so that was quite a challanging picking up a new language and integrating it with html. I came across many stumbling blocks and tried to use couch db as the database server but found it very difficult so i tried to use sqlite and found it much more user friendly to create a database using python. I spent a lot of time on the internet trying to find workable code snippets for my project and even more time change them to make them compatable with my code. I tried straight away to make my code take in information on one page and output it on another but I found it kept glitching and would throw up an error after a few bliks of the same page, this was because of bootstrap. So I decided to make it all on a single page so bootstrap would not interefere and it would still be appealling to the eye and have all the effects I wanted it to have. I would have liked for the to do list to be output on the screen and not just saved in the database but as hard as I tried I just couldnt make it output the database to the screen. So in order for you to check your to do list you must just simply open up the todolist.db in a text edit and all your tasks will be saved there.

### Running the program
To run the To Do List we must go into terminal and then find the folder in documents,as my pyhton file is called webapp.py  We then type in 
```bash
$ python webapp.py
```
Terminal will then give you back a url to be copied and pasted into a url bar, when run in the url bar the program will run on that url in the browser.
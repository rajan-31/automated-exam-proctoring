# Exam Servillence
A ML model to keep watch on exam candidates through webcam and create and update observations.\
*To under Working view* **[WORKING.md](./WORKING.md)**

> If you want to try/ test this project download or clone the repository.

<br></br>

\*Below two installations i.e. "Installations for server" & "Database installation" are needed to run the server to see the observations in browser\
\*Do those on your local machine or in pyenv

**Installations for server**

> `pip install flask`\
> `pip install pymongo`

**Database installation**

First install mongoDB\
Create a database 'exam_servillence'\
In 'exam_servillence' create collection 'statss'

<br></br>
\* Installations below are to run ML model\
\* I assume that you already have Anaconda & PyCharm

open PyCharm -> 
click create new project -> select location where downloded folder is present ->
select "new environment using"-> from drop down select "conda"->
select python version "3.8" ->
uncheck "create a main.py welcome script" ->
click create project ->
click "create from existing resources"

click right bottom corner -> click interpreter settings-> click "+" button to install packages given below\

\*To install search name and click install package


> dlib\
opencv\
requests

<br></br>
**How to run**
*you need to run two programs "app.py" & "exam_servillence.py"*

to run app.py run foollowing command in commandline

`cd exam_servillence`\
`flask run`

> Run **exam_servilllence.py** in PyCharm

you will get a window of your webcam

**Now go to** http://127.0.0.1:5000/servillence to view observations

*Page will automatiaclly refresh after every 30 seconds & records will be updated every 30 seconds.*
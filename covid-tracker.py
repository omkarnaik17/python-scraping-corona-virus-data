import requests #to generate http requests, in simple language.. to load a webpage.
from bs4 import BeautifulSoup #a beautiful web scraping library.
import threading #threading library, as the name suggest.

def covidTracker():
    #next line is for "Threading", multi threading and so, you can also use infinite while loop
    #we create a thread and set a timer of 20 seconds to. So that the thread(our program) will run every 20 sec
    #threading.Timer([timeInterval], [definition(function) name to run]).start() [ '.start()' function to start threading]
    threading.Timer(60.0, covidTracker).start()
    #passing the URL we want our program to look for
    #we pass it as a string, in python you need not declare the variable in the beginning unless you loop over it
    url = "https://www.mohfw.gov.in/"
    
    #we use requests library to load the web page of above link in our variable 'getPage'
    getPage = requests.get(url)

    #we parse(smilar torendering in video editing) the from raw byte to html tags using the BeautifulSoup library
    #and store it into 'soup' variable
    soup = BeautifulSoup(getPage.text, "html.parser")

    #we remove the part of page that we need from the whole page
    #we need a 'div' tag which is given class = 'content newtab' e.g. <div class="content newtab"> {..required data..} </div>
    requiredPartOfPage = soup.findAll('section', {'id':'state-data'})

    #opening a document named helloworldCorona.html which our program will auto generate 'w' stands for 'write' mode
    f = open('helloworldCorona.html','w')

    #we initialise 3 lists as the tag data is in list format, you can try with dictionary and tuples as well!
    page = []
    table = []

    #we loop 'requiredPartOfPage' to get the 2nd and 4th item in the list. imp: list starts from 0 and not 1
    #you can check why we do so by doing : print(page)

    for reqdPara in requiredPartOfPage:
        page+=reqdPara
        table = page[1]

    #print(page)
    #we build a clean html file as below, this is also sstored in string format.
    #we use a inbuilt typecasting function 'str()' to convert list data format to string data format
    cleanHTML = "<html> <body>" + str(table) + "</body> </html>"

    #write the string, 'cleanHTML' to our html file and then close the file by 'f.close()'
    f.write(cleanHTML)
    f.close()
    #for our information that the program is running, we print
    print("Updated the page!")

#call the definition(function) to be executed.
covidTracker()

'''
ASCII-ART  scraper  writen  as  a first project
to  scrap  ASCII-ARTs  from  http://patorjk.com
after studying python for 20 days in quarantine.
I know  the code  is  bad, need your comment to
improve  and  become a better programmer like U.
You need to have selenium with chrome driver and
BeautifulSoup installed in order to run this code.

By - Henoxx            Email - henoxx@qq.com
Sun, March 29, 2020
STAY HOME, BE SAFE!

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import sqlite3
import string


conn = sqlite3.connect('arts.sql')
cur = conn.cursor()

try: # if table exist ignore
    cur.executescript(
    '''
    CREATE TABLE Pchar (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        p_char TEXT UNIQUE
    );
    CREATE TABLE Fname (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Fart (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        pchar_id INTEGER,
        fname_id INTEGER,
        Art TEXT UNIQUE
    )
    ''')
except: pass

chrome_driver_path = '/Users/.../chromedriver' # give your chrome driver path here
chrome_options = Options()
chrome_options.add_argument('--headless') # to run chrome without the window
webdriver = webdriver.Chrome(
        executable_path = chrome_driver_path,
        options = chrome_options
        
    )

all = f'{string.ascii_letters}{string.punctuation}{string.digits}'
char_set = all
i = 0

# this function will wait until 60 fonts loaded
# from the targate website  and all code is according to the website
def timer():
    counter = 0
    while True:
        global source
        global soup
        source = webdriver.page_source # raw html file for the bs4
        soup = BeautifulSoup(source,'lxml')
        counter = soup.find("div", {"id": "taagTestAllListLoaded"})
        try: counter = counter.contents[0]
        except: break
        print(counter,end='\r',flush=True)
        counter = counter.split(' ') # from the way the text is written
        counter = int(counter[1]) 
        if counter >= 60: break
        else: continue
    return source

# this loop will iterate through each letters in char_set
for char in char_set: 
    url = f"http://patorjk.com/software/taag/#p=testall&f=Alpha&t={char}"
    print(f'Char \'{char}\' being coppied ....')
    if i == 0: # for the first page there is no need to refresh the page
        webdriver.get(url)
        timer() # after opening the page call this func. to count the fonts loaded
    if i > 0: # after the first page refreshing have become my option :(
        webdriver.get(url)
        webdriver.refresh()
        timer()
    
    i += 1
    time.sleep(2)

    soup = BeautifulSoup(source,'lxml')
    tags = soup('div',class_='fig')
    count = 1
    for tag in tags:
        print(f'writing font {count} to database',end='\r\r\r',flush=True)
        try:
            content = tag.pre.contents[0]
        except:
            continue
        font_id = tag.pre['id'] # Get the font name from the <pre id =? > tag
        font_id = font_id.replace('taag_font_','') # Replace the unwanted part
        cur.execute('INSERT OR IGNORE INTO Pchar (p_char) VALUES (?)',(char,))
        cur.execute('SELECT id FROM Pchar WHERE p_char = ?',(char))
        pchar_id = cur.fetchone()[0]

        cur.execute('INSERT OR IGNORE INTO Fname (name) VALUES (?)',(font_id,))
        cur.execute('SELECT id FROM Fname WHERE name = ?',(font_id,))
        fname_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Fart (pchar_id,fname_id,art)
                        VALUES (?,?,?)''',(pchar_id,fname_id,content))
        count += 1
        conn.commit()
    print(f'COPY SUCCESSFULL!')

webdriver.close()
conn.close()
print('Finished CREATING/UPDATING database.')


'''
Problems:

1. Need a better way to scrap the data from the javascript 
   driven page by waiting until everything is loaded.
   checking the load text from the website is not a good
   approach and usually make mistake.
2. Refreshing doesn't look a better option while loading 
   the new url
3. Have no selenium knowladge, I think I can do this without
   the BeautifulSoup module. With selenium alone.
4. If I run this code again in the same databse it doesn't 
   update correctly. It creates another entity with different
   id. I really have to solve this :( 

'''
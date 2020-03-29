# ASCII-ART
This is my first project after studying python for 20 days. I tried to use everything I learned as a beginner. With this project, I tried to scrap a website (http://patorjk.com) to get and create a database for ascii arts. My first thought was, it was easy to scrap the website with just BeautifulSoup a tool that I learned to use a little. Then, I realized that the ascii arts page is JavaScript driven. Which I don't know how to handle. Googled about it for hours and tried to use Selenium with BeautifulSoup together. Thanks to the efforts I made, I have succeeded scraping ascii arts and saved them to a database. 

I used a technique to scrap every font for each ascii_letters, ascii_digits and ascii_punctuations by fully automated python script. Which I named it 'ascii_scraper.py'. However some minor problems are found and the code is somehow tedious. I am looking forward to improve based on suggested ideas and new knowledge I planed to gather. 

After scraping and creating the database successfully, it was very easy to call and print the ascii arts. But, printing was more complex when the string is more than one character long (which obviously is, most of the time :). I built several functions to work together and print a string. Yeah it works. However concatenation is by new line. I can't have them all in one line. This was the most difficult stage of this project. Although I tried to search, didn't found something fruitful. Created a stuckoverflow account and post the issue am having.
Luckily got an answer with in 5 minutes(silly me :[] ). Thank you stuckoverflow for the beautiful work you did <3 . I updated my ascii_art printer with line by line concatenation codes.

Both the scraper and printer have their own issues. I addressed some of the problems at the bottom of each script. Since I haven't referred any ascii art scraper and printer scripts, I am very proud to have this as a first project. I will be very happy to have a feedback from you. Thanks!

March 29, 2020

Stay Home, Be safe!

Henoxx

henoxx@qq.com

'''
ASCII-ART  printer  writen  as  a first project
after studying python for 20 days in quarantine.
I know  the code  is  bad, need your comment to
improve  and  become a better programmer like U.

By - Henoxx            Email - henoxx@qq.com
Sun, March 29, 2020
STAY HOME, BE SAFE!

'''

import sqlite3
import string
import random
import time

conn = sqlite3.connect('arts_database.sql')
cur = conn.cursor()

to_print = list() # store characters to print 
printable = list() # to get the characters make 'to_print' become empty list

# this are error free common fonts 
# found by another python automation through the database
common_fonts = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11,
12, 13, 15, 16, 17, 18, 20, 21, 24, 26,
28, 29, 35, 36, 37, 38, 41, 42, 44, 45, 47, 48, 49]
choice = random.choice(common_fonts)


# this function will fetch the art from database
# based on chars  and font id.
def selector(chars,fonts = 9):
    if fonts > 50: fonts = 9 # Only 50 fonts available for now :)
    cur.execute(f'''
                    SELECT Fart.Art FROM Fart JOIN Pchar
                    ON Pchar.p_char = '{chars}' AND fname_id = {fonts} 
                    AND Fart.pchar_id = Pchar.id ''')
    item = cur.fetchone()[0]
    return item

# function responsible for concatenating line by line for each ascii_art
def looper(chars):
    i = 0  
    combined_chars = None  
    while i < len(chars):
        if i == 0: # only grab the first char
            index_char = chars[i].split('\n')
            printable_str = chars[i]
        try:
            next_char = chars[i+1].split('\n') # try to find next char if exist
        except: 
            break # break the loop if there is no char left

        # this will combine the chars and return a zip object
        combined_chars = zip(index_char,next_char) 

        # add line by line and return a string
        printable_str = '\n'.join([x+y for x,y in combined_chars])

        # convert the new string to index char for further use
        index_char = printable_str.split('\n') 
        
        i += 1
    
    
    return printable_str


def art(p_char = 'fiyo!',fname_id = 9):
    # if user input font id not in common_fonts assign a random font
    if fname_id not in common_fonts: 
        fname_id = choice
        # show the user the font is not found and show the random font assigned
        print(f'Font not found assigning random font {fname_id}',end='\r\r')
        time.sleep(3)
    # these fonts only accept uppercase letters
    if (fname_id == 10 or fname_id == 29 
        or fname_id == 13 or fname_id == 49 or fname_id == 20):
         p_char = p_char.upper()
    p_char = str(p_char)
    global to_print
    global printable
    for chars in p_char:
        # examine digits alone because low number of fonts
        if (chars in list(string.digits)): 
            try:
                char_slected = selector(chars,fname_id)
                to_print.append(char_slected)
                continue
            except:  # if font not found
                char_slected = selector(chars,9) # default font 9 (it is tasted and have all the digits)
                to_print.append(char_slected)
                continue 
        # examine punctuations alone because low number of  fonts        
        if (chars in list(string.punctuation)): 
            # This are the available chars, if user char out of this replaced by '!'
            if (chars not in ['!','+','-','?','@']): chars = '!'
            try:
                char_slected = selector(chars,fname_id)
                to_print.append(char_slected)
            except:  # if font not found
                char_slected = selector(chars,9)
                to_print.append(char_slected) 

        else: # if they are ascii_letters
            try:
                char_slected = selector(chars,fname_id)
                to_print.append(char_slected)
            except TypeError: # this will handle by fetching NoneType 
                # it happens if there are no chars assigned in database for the user input
                # it will simply replace them by 'x'
                char_slected = selector('-',9)
                to_print.append(char_slected)
            except: # if font not found
                char_slected = selector(chars,9)
                to_print.append(char_slected)
    
    printable = to_print # takes the art list
    to_print = [] # ready for another round
    return looper(printable)

'''
Problems:

1. Erorr handling doesn't look good
2. The code is tedious.
'''
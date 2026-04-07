# Author: Ben McBride
# Date: April 3, 2026
# Assignment name: Hash It Out

import time
import random
import csv


class Node: #For linked lists
    #Constructor
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.link = None

    #public String toString(){
    def __str__(self):
        return str(self.key) + ", " + self.data.movie_title



class Movie:
    #Constructor
    def __init__(self,movie_title,genre,release_date,director,box_office_revenue,rating,duration_minutes,production_company,quote):
        self.movie_title = movie_title
        self.genre = genre
        self.release_date = release_date
        self.director = director
        self.box_office_revenue = box_office_revenue
        self.rating = rating
        self.duration_minutes = duration_minutes
        self.production_company = production_company
        self.quote = quote

    #public String toString(){
    def __str__(self):
        return (f"{self.movie_title}, {self.genre}, {self.release_date}, {self.director}, {self.box_office_revenue}, " 
                f"{self.rating}, {self.duration_minutes}, {self.production_company}, {self.quote}")



def basicSearch(var,term,movieList):
    if var == "title":
        print("Searching the unhashed list for film(s) named " + term + "...")
        start1 = time.time()
        for i in range(len(movieList)):
            if term == movieList[i].movie_title:
                end1 = time.time()
                print(term + " found at index " + str(i) + " in time " + str(end1-start1))
    if var == "quote":
        print('Searching the unhashed list for the film with the quote "' + term + '"...')
        start2 = time.time()
        for i in range(len(movieList)):
            if term == movieList[i].quote:
                end2 = time.time()
                print("Film " + movieList[i].movie_title + " with your quote found at index " + str(i) + " in time " + str(end2-start2))



def report(start,end,cols,mode,oper,var,func,size,hashedList):
    empties = 0
    for i in range(len(hashedList) - 1):
            if hashedList[i] == None:
                empties += 1
    if mode == "linearProbing": #Formatting for nicer printouts
        mode = "Linear Probing"
    if mode == "linkedList":
        mode = "Linked List"
    if oper == "build":
        oper = "Create table"
    if oper == "search":
        oper = "Search table"
    if var == "title":
        var = "Movie title"
    if var == "quote":
        var = "Iconic quote"
    print("")
    print("############### REPORT #################")
    print("Hash function:         " + str(func))
    print("Mode:                  " + mode)
    print("Operation:             " + oper)
    print("Variable hashed:       " + var)
    print("Size of hashed list:   " + str(size))
    print("----------------------------------------")
    print("Time taken (seconds):  " + str(end-start))
    print("Collisions:            " + str(cols))
    print("Unused spaces:         " + str(empties))



def hashTable(mode,oper,var,func,size,curList,term):
    cols = 0
    if mode == "linearProbing":
        if oper == "build":
            hashedList = [None] * size
            if var == "title":
                print("Building hash table...")
                start = time.time()
                for i in range(len(curList) - 1):
                    j = func(curList[i].movie_title,size)
                    while hashedList[j] != None:
                        cols += 1
                        j += 1
                    hashedList[j] = curList[i]
                end = time.time()
                print("Hash table built.")
                report(start,end,cols,mode,oper,var,func,size,hashedList)
                return hashedList
            if var == "quote":
                print("Building hash table...")
                start = time.time()
                for i in range(len(curList) - 1):
                    j = func(curList[i].quote,size)
                    while hashedList[j] != None:
                        cols += 1
                        j += 1
                    hashedList[j] = curList[i]
                end = time.time()
                print("Hash table built.")
                report(start,end,cols,mode,oper,var,func,size,hashedList)
                return hashedList
            
        if oper == "search": #This searches for only the first movie of this name in the list for simplicity; the assignment didn't specify it had to return all of them
            if var == "title":
                print("Searching hash table...")
                start = time.time()
                i = func(term,size)
                while curList[i].movie_title != term:
                    cols += 1
                    i += 1
                end = time.time()
                report(start,end,cols,mode,oper,var,func,size,curList)
                return curList[i]
            if var == "quote":
                print("Searching hash table...")
                start = time.time()
                i = func(term,size)
                while curList[i].quote != term:
                    cols += 1
                    i += 1
                end = time.time()
                report(start,end,cols,mode,oper,var,func,size,curList)
                return curList[i]

                
    if mode == "linkedList":
        if oper == "build":
            hashedList = [None] * size
            if var == "title":
                print("Building hash table...") #I had to research some of this as I am not very familiar with linked lists, and doing it in Python wasn't covered in class
                start = time.time()
                for i in range(len(curList) - 1):
                    j = func(curList[i].movie_title,size)
                    newNode = Node(j,curList[i])
                    curNode = hashedList[j]
                    if curNode == None:
                        hashedList[j] = newNode
                    else:
                        cols += 1
                        while curNode.link != None:
                            cols += 1
                            curNode = curNode.link
                        curNode.link = newNode
                end = time.time()
                print("Hash table built.")
                report(start,end,cols,mode,oper,var,func,size,hashedList)
                return hashedList
            if var == "quote":
                print("Building hash table...")
                start = time.time()
                for i in range(len(curList) - 1):
                    j = func(curList[i].quote,size)
                    newNode = Node(j,curList[i])
                    curNode = hashedList[j]
                    if curNode == None:
                        hashedList[j] = newNode
                    else:
                        cols += 1
                        while curNode.link != None:
                            cols += 1
                            curNode = curNode.link
                        curNode.link = newNode
                end = time.time()
                print("Hash table built.")
                report(start,end,cols,mode,oper,var,func,size,hashedList)
                return hashedList
            
        if oper == "search":
            if var == "title":
                print("Searching hash table...")
                start = time.time()
                i = func(term,size)
                curNode = curList[i]
                while curNode.data.movie_title != term:
                    cols += 1
                    curNode = curNode.link
                end = time.time()
                report(start,end,cols,mode,oper,var,func,size,curList)
                return curNode.data
            if var == "quote":
                print("Searching hash table...")
                start = time.time()
                i = func(term,size)
                curNode = curList[i]
                while curNode.data.quote != term:
                    cols += 1
                    curNode = curNode.link
                end = time.time()
                report(start,end,cols,mode,oper,var,func,size,curList)
                return curNode.data



def hashBrown():
    print("April Fools!")
    print("/----\\\n"
          "|;;;;|\n"
          "|;;;;|\n"
          "|;;;;|\n"
          "|;;;;|\n"
          "\\----/")
    print("(Simply delicious...)")

        

def dummy(term,size): #Non-working "hash function" that always collides for testing the other code; not one of the five.
    return 0
                


def firstLetter(term,size):
    if ord(term[0].lower()) in range(97,123): #Is the first letter a basic English letter?
        return (ord(term[0].lower()) - 97) % size #Return its position in the alphabet
    else: #If it's an edge case (number, symbol, Unicode character)...
        return 26 % size #...put those all in one dedicated bucket.



def sumFirstEight(term,size):
    k = 0 #Temporary value
    for i in range(max(len(term),8)): #Iterate over the first 8 letters, if there are that many
        k += ord(term[i].lower()) - 97 #Add the position of the character in the alphabet
    if k in range(0,201): #Max possible sum of the positions of eight letters
        return k % size
    else:
        return 201 % size #Single edge case bucket
    
            

def main():
    movieList = []
    #File handling and building unhashed movie list
    with open ("MOCK_DATA.csv",encoding="utf-8",newline='') as myFile: #Learned via Google when looking up how to stop names with commas from being split
        counter = 0
        myReader = csv.reader(myFile,delimiter = ',',quotechar = '"')
        for line in myReader:
            discard = False
            if line[0] == "movie_title": #Is this line the legend at the top?
                discard = True #Then don't add it
            if len(line) < 9:
                discard = True
                print("Error: Line " + str(counter) + " is missing data and was skipped.")
            if len(line) > 9:
                discard = True
                print("Error: Line " + str(counter) + " contains duplicate or extraneous data and was skipped.")
            if discard == False: #Process the data further if we can work with it
                newMovie = Movie(line[0].strip(' "'),line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8].strip(' "'))
                movieList.append(newMovie)
            counter += 1

    #Randomly select a movie from the list to search for
    toSearch = movieList[random.randint(0,len(movieList)-1)]

    #Conduct a timed simple search of the unhashed array for comparison
    basicSearch("title",toSearch.movie_title,movieList)
    basicSearch("quote",toSearch.quote,movieList)

    #Now begin hashing and searching
    print("")
    hashedList1 = hashTable("linearProbing","build","quote",sumFirstEight,15000,movieList,None)
    searchResult = hashTable("linearProbing","search","quote",sumFirstEight,15000,hashedList1,toSearch.quote)
    print("")
    print("You searched for: " + str(searchResult))
    print("")
    hashedList2 = hashTable("linkedList","build","quote",sumFirstEight,202,movieList,None)
    searchResult2 = hashTable("linkedList","search","quote",sumFirstEight,202,hashedList2,toSearch.quote)
    print("")
    print("You searched for: " + str(searchResult2))
    print("")
        
        

            
if __name__ == "__main__":
    main()

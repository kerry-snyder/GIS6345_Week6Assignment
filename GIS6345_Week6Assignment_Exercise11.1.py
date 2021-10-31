#Exercise 11.1
#Write a function that reads the words in words.txt and stores them as keys in adictionary. 

#Version with text file outside of function

#Open text file and define dictionary
fin = open('words.txt')
w = dict()
def find_words(t):
    for line in t:
        w[line[:-1]]= 1

#Run function on text file
find_words(fin)

#Test function 
print('aah' in w)
print('aah' in w)
print('quiero' in w)

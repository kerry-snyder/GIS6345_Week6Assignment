#Exercise 12.1

#Define a dictionary
d = dict()

#Define the function
def most_frequent(w):
    for char in w:
        if char in d:
            d[char] +=1
        else:
            d[char] = 1
    dsorted = dict(sorted(d.items(), key = lambda x:x[1], reverse=True))
    print(dsorted)
    for char in w:
        d[char] = 0

#Test the function on a single word
most_frequent('cormorant')

#Test the function in different languages using the first line of the novel Pride and Prejudice
English = 'it is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife'
Spanish = 'es una verdad universalmente reconocida, que un hombre soltero en posesión de una buena fortuna, debe estar en necesidad de una esposa'
French = 'c’est une vérité universellement reconnue, qu’un homme célibataire en possession d’une bonne fortune, doit être en manque d’une femme'
German = 'es ist eine allgemein anerkannte wahrheit, dass ein einzelner mann, der im besitz eines glücks ist, eine frau haben muss'

print('English')
most_frequent(English)
print('French')
most_frequent(French)
print('German')
most_frequent(German)
print('Spanish')
most_frequent(Spanish)

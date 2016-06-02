# Gjennom � ut�ve denne operasjonen, s�ker datamaskinen gjennom lister for � finne ut hvor lang tid de individuelle maskinene bruker p� og komme igjennom de.
# M�let er � finne ut hvor rask hver enkelt maskin kan prossessere elementer gjennom en algoritme.

def search_fast(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
        return False
    
# search_fast s�ker gjennom mindre lister en search_slow, dette for � gi en kontrast mellom hvordan en PC fungerer ved forskjellige byrder.
# Denne testen blir gjort for � gi en pekepinn p� komponentene til maskinen, og hva slags hastighet de kan kj�re python i.    
    
def search_slow(haystack, needle): 
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
            print needle
    return return_value    

haystack = open('komponenter105.txt')
haystack.read()

needle = 'needle'

# Her printer funksjonen ut en liste over hastighetene maskinen bruker til � kj�re igjennom elementene.

if __name__ == '__main__':
    import timeit
    print("Search_fast took in seconds") 
    print(timeit.timeit("search_fast(haystack, needle)", setup="from __main__ import search_fast, haystack, needle"))
    print("Search_slow took in seconds") 
    print(timeit.timeit("search_slow(haystack, needle)", setup="from __main__ import search_slow, haystack, needle"))
   


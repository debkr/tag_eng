# Tagging Engine 1.0.2
# Python Soup 1 May 2016


# enter filename or quit (with default)
fname = raw_input('Enter the filename or Q to quit: ')
if fname.lower() == 'q' :
    quit()
elif len(fname) == 0 :         # default on enter
    fname = 'words.txt'        # default on enter

    
# open file or return error message
try:
    fhand = open(fname)
except:
    print 'Filename not found:', fname
    quit()
### IMPROVEMENT: ADD FILNAME ENTRY INTO FUNCTION & CALL FUNCTION INSTEAD OF QUIT()


# excluded words list
excluded = ['this','that','what','who','as','like','our','us','be','it','to','our','the','on','we','do','can','a','is','are','was','were','or','and','of','for','from','you','your','me','my','we','our','they','their','us','them','at','out','to','this','that','the','those','some','any','no','none','on','within']
#excluded1 = ["from","in","else","with","without","if","not"]
### IMPROVEMENT: ASK USER IF WISH TO INCLUDE OR EXCLUDE PYTHON RESERVED WORDS LIST


# split all words in file into a list
text = fhand.read()
text = text.lower()
wordlist = text.split()
### IMPROVEMENT: GIVE USER Y/N OPTION TO STRIP OUT PUNCTUATION &/OR HTML TAGS


# counting all words into a dictionary
words = dict()
for word in wordlist :
    if word in excluded : continue
#    if word in excluded1 : continue   ### IMPROVEMENT: USER-DEFINED
    words[word] = words.get(word,0) + 1

    
# counting most common words in dictionary
wordhigh = None ; counthigh = None
for word,count in words.items() :
    if wordhigh is None or count > counthigh :
        wordhigh = word
        counthigh = count
print '\n', 'Most common word and its count:'
print wordhigh, counthigh, '\n'


# print all words in descending order
wordlist = words.keys()
countlist = words.values()
inp = raw_input('Do you want a complete listing (Y/N)?')
if inp.lower() == 'y' :
    print '\n', 'All words in descending order:'
    y = range(len(wordlist))
    for y in y :
        x = range(len(wordlist))
        for x in x :
            if countlist[x] == counthigh - y :
                print wordlist[x], countlist[x]
### IMPROVEMENT: USER SPECIFY REQUIRED ORDER: ASCENDING OR DESCENDING


# n orders of word frequency (n is user-defined)
inp = raw_input('Enter a number for "n orders of word frequency":')
n = int(inp)
### IMPROVEMENT: ADD ERROR HANDLING (non-numeric entry)


# while n not zero,
# loop through all counts from counthigh downwards
# and return all words & counts for n-i-1
order = 1
countnum = 0
while n <> 0 :
    if countnum == counthigh : break
    if counthigh - countnum in countlist :
        print '\n', 'Order:', order
        print '--------'
        x = range(len(wordlist))
        for x in x :
            if countlist[x] == counthigh - countnum :
                print wordlist[x], countlist[x]
        order = order + 1
        countnum = countnum + 1
    else :
        countnum = countnum + 1
        continue        
    n = n - 1
print '\n', '++Finished++', '\n'


# simple listing (dictionary of words and counts)
inp = raw_input('Do you want a simple listing (Y/N)?')
if inp.lower() == 'y' :
    print words
### IMPROVEMENT: ADD ERROR HANDLING (non-numeric entry)

print '\n', '++Goodbye++'
quit()

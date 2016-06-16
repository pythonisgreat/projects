direction =['north', 'east', 'south', 'west']
verb = ['go', 'stop', 'kill','eat']
noun = ['princess', 'bear', 'door', 'shoe', 'pies']
stop = ['the', 'in', 'at', 'it', 'from', 'of']

userinput = 'go north'
sentence = []


def scan(text):
    words = text.split()
    for x in words:
        if x in direction:
            #print x
            sentence.append(('direction', x))
        elif x in verb:
            #print x
            return[('verb', x)]
        elif x in noun:
            #print x
            return[('noun', x)]
        elif x in stop:
            #print x
            return[('noun', x)]
        elif x.isdigit():
            convert_number(x)
        else:
            print 'wtf'
    #return sentence

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

scan(userinput)
print sentence

#first_word = ('verb', 'go')
#second_word = ('direction', 'north')
#third_word = ('direction', 'west')
#sentence = [first_word, second_word, third_word]

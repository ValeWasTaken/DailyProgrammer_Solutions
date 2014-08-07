import re

def main():
    a2m = { #ASCII to Morse dictionary
        'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.',
        'f':'..-.','g':'--.','h':'....','i':'..','j':'.---',
        'k':'-.-','l':'.-..','m':'--','n':'-.','o':'---',
        'p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-',
        'u':'..-','v':'...-','w':'.--','x':'-..-','y':'--.-',
        'z':'--..','1':'.----','2':'..---','3':'...--','4':'....-',
        '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
        '0':'-----',',':'--..--','.':'.-.-.-','?':'..--..','/':'-..-.',
        '-':'-....-','(':'-.--.-',')':'-.--.-',' ':'','':' '
        }

    m2a = dict((a,b) for b, a in a2m.iteritems()) #Morse to ASCII dictionary
    m2a['  '] = ' '

    s = raw_input('-->').lower()

    def encode(s): return ' '.join(a2m[x] for x in s)
    def decode(s): return ''.join(m2a[x] for x in re.findall(r'[.-]+|  ', s))
    e = encode(s)
    d = decode(e)
    
    print e # Morse translation
    print d # English translation
main()

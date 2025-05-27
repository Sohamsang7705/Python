morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--','Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--','4': '....-','5': '.....','6': '-....',
    '7': '--...','8': '---..','9': '----.',
    ' ': '/'  
}

reverse_dict = {}
for key in morse_dict:
    value = morse_dict[key]
    reverse_dict[value] = key

def to_morse(text):
    result = ""
    for char in text.upper():
        if char in morse_dict:
            result += morse_dict[char] + " "
        else:
            result += "? "
    return result

def to_text(morse):
    result = ""
    words = morse.split(" / ")  
    for word in words:
        letters = word.split()  
        for letter in letters:
            if letter in reverse_dict:
                result += reverse_dict[letter]
            else:
                result += "?"
        result += " "
    return result


print ("Morse Code Translator")
print("1. Text to morse:")
print("2. morse to text")

choice = input ("Enter ! or 2: ")

if choice == "1":
    text = input ('Enter your message: ')
    print ('morse code :', to_morse(text))

elif choice == "2":
    morse = input('Enter Morse code:')
    print('text',to_text(morse))

else:
    print("Invalid Input")
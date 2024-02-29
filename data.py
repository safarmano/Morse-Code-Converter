morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '"': '.−..−.', '!': '-.-.--', ':': '−−−...',
    '-': '−....−', '/': '−..−.', '(': '−.−−.', ')': '−.−−.−', '=': '−...−', '+': '.−.−.', '@': '.−−.−.', '*': '...-...',
    '$': '...−..−', '#': '−−−−−−−', '%': '−−...−−', '\\': '-...-....', '|': '−−−.−−−', '<': '−.−.−−', '>': '--.--',
    '{': '.----.-..', '}': '.----.-..-', '[': '−.−−.-.', ']': '−.−−.−-.-', '^': '−..−..', '`': '...−..', '~': '−.−−.−−',

    'START SIGNAL': '-.-.-.', 'END OF WORK': '...-.-', 'ERROR': '........', 'WAIT': '.-...'
}

messages = {
    "welcome_message": "\n\n\nWelcome to the Morse Code Converter!",

    "rules_message":   "\nWe kindly ask you to carefully review the rules outlined below:\n\n"
                       "1. Only the English alphabet can be utilized for encoding, or the appropriate"
                       " Morse code for decoding.\n\n"
                       "2. To obtain Morse code for terms like 'Start Signal', prefix the term with '#' and type it"
                       " in uppercase.\n\n"
                       "3. Please avoid using non-English alphabet characters or symbols as they won't be encoded "
                       "or decoded.\n\n"
                       "4. Upon encoding or decoding, the output is automatically copied, enabling direct pasting.\n\n"
                       "5. You can append the encoded or decoded words to the 'results' text file by clicking "
                       "the 'Save' button.",

    "copyright_message": "Copyright © Samir Farman 2024",

    "mark_info": "Please note that some punctuation marks and miscellaneous signs are not universally standardized "
                 "and may vary depending on the context or the specific Morse code adaptation being used.",

    "term_info": "This is a term used to indicate a specific action in the signalling process!",

    "character_error": "Some entered characters are not recognized. Please ensure that you exclusively utilize "
                       "the English alphabet to avoid encoding errors. Otherwise, they will not be encoded.",

    "code_error": "Some entered codes are not recognized. "
                  "Ensure that you adhere strictly to Morse code signals, which consist solely of dots (.) and "
                  "dashes (-), and that they are formatted correctly according to Morse code writing conventions. "
                  "Failure to do so may result in decoding errors.",

    "empty_field_error": "Please do not leave any fields empty on the left or right side.",

    "empty_field_error_saving": "To proceed with saving, please ensure that all fields on the left or right"
                                  " side are filled."
}


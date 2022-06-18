import string
import os

def custom_made_alphabet(value):
    value = str(value)
    assert value.isdigit() or value.isalpha() , ''
    # define an alphabet
    alfa = "abcdefghijklmnopqrstuvwxyz"

    # define reverse lookup dict
    rdict = dict([(x[1],x[0]) for x in enumerate(alfa)])
    # enumerate alfa returns a list of tuples which is reversed then converted into a dict
    if value.isdigit():
        return alfa[int(value)]
    return rdict[value]

def pos_alphabet(character):
    return ord(character)
    # returns character position in alphabet

def char_alphabet(pos):
    return chr(pos)
    # returns character occupying a certain pos in alphabet

def with_pos_import(character):
    return string.ascii_lowercase.index(character)


def with_char_import(pos):
    return string.ascii_lowercase[pos]


def make_trans(text,action='encode'):
    #string.maketrans() deprecated ...use str.maketrans or bytes.maketrans or bytesarray.maketrans
    #to convert string into bytes begin your string with b eg b'ddd'
    textin = "abcdefghijklmnopqrstuvwxyz"
    textout = "cdefghijklmnopqrstuvwxyzab"
    texttrans = str.maketrans(textin, textout)
    texttrans_decode = str.maketrans(textout, textin)

    #text = "qcc, gr umpiq"

    a = text.translate(texttrans)
    b = text.translate(texttrans_decode)
    if action == 'decode':
        return b
    return a




def alphabet(arg,return_lower=True):
    arg = str(arg)
    assert arg.isdigit() or arg.isalpha()

    if arg.isdigit():
        if return_lower:
            return chr(int(arg) + 97).lower()
        return chr(int(arg) + 97).upper()

    return ord(arg.lower()) - 97
def encode_me(FILE):
    if FILE != 'encrypt.py':
        with open(FILE,'r+') as f:
            text = f.read()
            encoded = make_trans(text) # default encodes,,to decode use 2nd arg as decode
        with open(FILE, 'w') as f:
            f.write(encoded)


def decode_me(FILE):
    if FILE != 'encrypt.py':
        with open(FILE, 'r+') as f:
            text = f.read()
            decoded = make_trans(text,'decode')

        with open(FILE, 'w') as f:
            f.write(decoded)

def main():
    # This is a classic encoder
    # # File must be in clear text.. If you encode an already encoded text, recovering it
    # might result into problems
    # Write anything with freedom
    # Give location of your text file in the FILE variable as a string
    FILE = ''
    run = True
    while run:

        print("               " + '\33[96m' + ".-._   _ _ _ _ _ _ _ _ " + '\33[0m' + "\n"
              "    " + '\33[96m' + ".-''-.__.-'" + '\33[0m' + "" + '\33[31m' + "oo" + '\33[0m' + " " + '\33[35m' + "'-' ' ' ' ' ' ' ' '-." + '\33[0m' + "\n"
              "  '" + '\33[31m' + ".___ '" + '\33[0m' + "    .  .--_ '-' '-' '-' _'-' '._\n"
              "   " + '\33[5m' + '\33[31m' + "v" + '\33[0m' + ": " + '\33[6m' + '\33[31m' + "v" + '\33[0m' + " '" + '\33[5m'
              + '\33[31m' + "vv-" + '\33[0m' + "'  '_   '.       .'  _--' '" + '\33[32m' + ".'." + '\33[0m' + "\n"
              "     '=.___.=_.--'   :_.__.__:_   '.   " + '\33[32m' + ": :" + '\33[0m' + "\n"
              "            " + '\33[34m' + "(((" + '\33[0m' + "___.-'         '-.  /   " + '\33[32m' + ": :" + '\33[0m' + "\n"
              "==============================" + '\33[34m' + "(((" + '\33[0m' + "-'\ " + '\33[32m' + ".' /" + '\33[0m' +
              "=======================\n"
              "                         " + '\33[32m' + "________..'  .'" + '\33[0m' + "\n"
              " " + '\33[35m' + "HAcK_BM KeY CrOC" + '\33[0m' + "        " + '\33[32m' + "'-._______.-'" + '\33[0m' + "")

        response = ''
        # print("\n\nTo open your desired file, type |open|")
        response = input('\nType |encode| or |decode| to perform operation\n \nType '
                         '|exit| or |terminate| to exit\n >>')
        if response.lower() == 'encode':
            FILE = str(input('Kindly provide full path to your desired file\n  >>'))
            # TODO verify if path is valid, if not return a response
            # Perform the encryption
            encode_me(FILE)

        if response.lower() == 'decode':
            FILE = str(input('Kindly provide full path to your desired file\n  >>'))
            # TODO verify if path is valid, if not return a response
            # Perform the decryption
            decode_me(FILE)


        # open the file to view
        if response.lower() == 'open':
            # define a method that opens the file.
            code = os.system('FILE')
            # And probably another that closes the file

        if response.lower() == 'terminate' or response.lower() == 'exit':
            run = False




if __name__ == '__main__':
    main()

import pyperclip
"""Simple program to encrypt and decrypt text with ROT13"""

def rot_13(message_in):
    ''' Function takes in a sting then iterates thru each charcter and tests to
    see if it is an alpha character. Non-alphas are passed unchanged to the
    list. Next it tests if the character is upper or lower case to determine
    correct range to check for the value to decide to add or subtract 13 from 
    the ORD value and maintain case. Returns joined list as a string'''
    message_out = []
    for i in message_in:
        if i.isalpha() == False:
            message_out.append(i)
        elif i.isupper() == True:
            v = ord(i)
            if v < 78:
                nv = v+13
            else:
                nv = v-13
            message_out.append(chr(nv))
        elif i.islower() == True:
            v = ord(i)
            if v < 110:
                nv = v+13
            else:
                nv = v-13
            message_out.append(chr(nv))
        else:
            print('Somthing went wrong.')
    return(''.join(message_out))


def main():
    '''main function menu offers choices for manual entry or taking string from
    clipboard. Returned string is printed to the terminal and sends it to the
    clipboard'''
    try:
        while True:
            print('ROT13 Encoder/Decoder \n\n\n1) Enter message manually\n'
            '2) Get from clipboard\n3) Exit\n')
            choice = input('Select:')
        
            if choice == '1':
                message = input('Message to encode/decode:')
                zrffntr = rot_13(message)
                pyperclip.copy(zrffntr)
                print(f'\n{zrffntr}\n\n')
            elif choice == '2':
                zrffntr = rot_13(pyperclip.paste())
                pyperclip.copy(zrffntr)
                print(f'\n{zrffntr}\n\n')
            elif choice == '3':
                break
            else:
                print('You must select once of the menu choices')
    except:print('An exception occoured')

if __name__ == '__main__':
    main()
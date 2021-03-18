
def split(string):
    print(string)
    return [char for char in string] 


def rot_13(message_in):
    # split_message = split(message_in)
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

    print(message_out)

    return('test')


def main():
    message = 'Guvf vf n grfg zrffntr, pna lbh qrpbqr vg?'
    
    zrffntr = rot_13(message)
    print(zrffntr)


if __name__ == '__main__':
    main()
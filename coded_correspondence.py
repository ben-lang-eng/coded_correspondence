alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
message2 = 'Coding is fun!!!'
message3 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
message4 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
message5 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
message6 = "ymlok cp fbb ejv"
key1 = "dog"

def decrypter(msg, offset):
    result = ''
    msg_lower = msg.lower()
    for letter in msg_lower:
        if letter not in alphabet_string:
            result += letter
        elif letter in alphabet_string:
            result += alphabet_list[((alphabet_list.index(letter) + offset) % (len(alphabet_list)))]
    return print(result)

# decrypter(message, 10)

def encrypter(msg, offset):
    result = ''
    msg_lower = msg.lower()
    for letter in msg_lower:
        if letter not in alphabet_string:
            result += letter
        elif letter in alphabet_string:
            result += alphabet_list[((alphabet_list.index(letter) - offset) % (len(alphabet_list)))]
    return print(result)

# encrypter(message2, 10)
# decrypter(message3, 10)
# decrypter(message4, 14)

# for i in range(len(alphabet_list)):
#     decrypter(message5, i)
#     print("The offset is " + str(i) + ".")

def vig_encode(msg, key):
    result = ''
    key_lower = key.lower()
    msg_lower = msg.lower()
    for i in range(len(msg_lower)):
        if msg_lower[i] not in alphabet_string:
            print(msg_lower[i])
        elif msg_lower[i] in alphabet_string:
            print(key_lower[(i % (len(key_lower)))])
    # return print(result)

def vig_decode(msg, key):
    result = ''
    keyword_phrase = ''
    key_lower = key.lower()
    msg_lower = msg.lower()
    message_score = []
    key_score = []
    difference_score = []
    # Construct the keyword phrase
    for i in range(len(msg_lower)):
        if msg_lower[i] not in alphabet_string:
            keyword_phrase += msg_lower[i]
        elif msg_lower[i] in alphabet_string:
            keyword_phrase += key_lower[(i % (len(key_lower)))]
    print(keyword_phrase)

    # determine message phrase score
    for i in msg_lower:
        if i not in alphabet_string:
            message_score.append('*')
        elif i in alphabet_string:
            message_score.append(alphabet_list.index(i))
    print(message_score)

     # determine keyword phrase score
    for i in keyword_phrase:
        if i not in alphabet_string:
            key_score.append('*')
        elif i in alphabet_string:
            key_score.append(alphabet_list.index(i))
    print(key_score)

    # calculate score difference between message phrase and keyword phrase
    for i in range(len(message_score)):
        if message_score[i] == '*':
            difference_score.append('*')
        else:
            print(message_score[i] - key_score[i])
    # print(difference_score)

vig_decode(message6, 'dog')
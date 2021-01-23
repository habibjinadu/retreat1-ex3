#shuffle.py

def encode_shuffle(message, secret):
    shuffled_string = do_shuffle(message, shuffle_axis(secret))
    return ""

def decode_shuffle(message, secret):
    shuffled_string = do_shuffle(message, shuffle_axis(secret))
    return shuffled_string

def shuffle_axis(secret):
    number = 0
    for letter in secret:
        number += ord(letter)
    number += len(secret)
    #number = number % len(message)
    print("axis of rotation for : " + secret + " is " + str(number))
    # (ﾉ ͡° ͜ʖ ͡°)ﾉ ‥…━━━★
    return number

def do_shuffle(message, axis):
    message = list(message)
    
    message.reverse()
    
    # (ﾉ ͡° ͜ʖ ͡°)ﾉ ‥…━━━★
    def shift(seq, n):
        a = n % len(seq)
        return seq[-a:] + seq[:-a]
    
    message = shift(message, axis)
    return ''.join(message)

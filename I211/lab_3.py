##doubles = [x + x for x in range(10)]
##
##numbers = [ x for x in range(100) if x % 10 == 0]
##
##words = ['apple','ball', 'candle', 'dog', 'egg', 'frog']
##
##words = [words[i].upper() if len(words[i]) < 4 else words[i] for i in range(len(words))]
##words = [words[i].upper() for i in range(len(words)) if len(words[i]) < 4 ]


secret = input("Please enter the secret:")

censor = ['-' if secret[i].isalpha() else secret[i] for i in range(len(secret))]

print("".join(censor))


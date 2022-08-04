abjad = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
lo = abjad.split()
up = (abjad.upper()).split()

scramble = input("kata: ")
for c in scramble:
    if c in lo:
        ch = lo[(lo.index(c)+13) % len(lo)]
        print(ch,end = "")
    elif c in up:
        ch = up[(up.index(c)+13) % len(up)]
        print(ch,end = "")
    else:
        print(c,end="")


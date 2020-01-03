# Doesn't work
# def to_kikoo(elt):
#     listfrom = ["e","E","E","o","O","O","a","l","l","B","L","L","o","O"]
#     listto = ["3","€","£","0","Oo","Ow","@","1","|","8","|","1","°","°"]
#     yield elt
#
#     for i in range(len(listfrom)):
#         yield elt.replace(listfrom[i],listto[i])
#
#     for i in range(2,len(listfrom)):
#         for combination_tuple in itertools.combinations(list(range(len(listfrom))),i):
#             newword = elt
#             for number_toapply in combination_tuple:
#                 newword = newword.replace(listfrom[number_toapply],listto[number_toapply])
#             yield newword

def up_down_up_down(seq,start = "up"):
    seq = seq.lower()
    newseq = []
    current = start
    for elt in seq:
        if current == "up":
            newseq.append(elt.upper())
            current = "down"
        elif current == "down":
            newseq.append(elt.lower())
            current="up"
    return "".join(newseq)

def startby_maj(seq):
    seq = seq.lower()
    seq = seq[0].upper()+"".join(seq[1:])
    return seq

def maj_modif(elt):
    yield elt
    yield up_down_up_down(elt,start="up")
    yield up_down_up_down(elt,start="down")
    yield elt.lower()
    yield elt.upper()
    yield startby_maj(elt)

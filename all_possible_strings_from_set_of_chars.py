
def all_strings(list_of_chars, k):
    form_strings(list_of_chars, len(list_of_chars), k, "")



def form_strings(list_of_chars, a, b, prefix):
    if b==0:
        print(prefix)
        return
    for i in range(a):
        word = prefix + list_of_chars[i]
        form_strings(list_of_chars, a, b-1, word)


all_strings(["a","b","c"], 3)
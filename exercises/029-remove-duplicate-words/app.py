# Your code here
def remove_duplicate_words(string):
    array = string.split(" ")
    nodupes = list(set(array))
    sort = sorted(nodupes)
    string = " ".join(sort)
    print(string)

remove_duplicate_words("hello world and practice makes perfect and hello world again")
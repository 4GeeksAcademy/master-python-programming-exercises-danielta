# Your code here
def sequence_of_words(list):
    array = list.split(',')
    array.sort()
    string = ", ".join(array)
    print(string)


sequence_of_words("zebra,lion,alpha,charlie")
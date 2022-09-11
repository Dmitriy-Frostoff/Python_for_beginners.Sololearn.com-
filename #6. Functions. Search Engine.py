def search(text, word):
    etr = text.split(" ")
    for i in etr:
        if i == word:
            return("word found")
    return("word not found")   
         
text = input()
word = input()
print(search(text, word))

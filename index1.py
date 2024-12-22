word = input("Enter your word or sentence: ")
word = word.lower()
letter = input("Enter your letter or charecter: ")
letter = letter.lower()
i=0
NoOfLetter= 0
while i<len(word):
    if word[i]==letter:
        NoOfLetter+=1
    i+=1
print("Your letter or charecter",letter,"is repeted",NoOfLetter,"many times")
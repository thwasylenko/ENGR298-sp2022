# helpful function to see if word starts with vowel
def starts_with_vowel(word):
    # make word lower case
    word = word.lower()

    if word[0] == 'a' or word[0] == 'e' \
            or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        return True
    else:
        return False


# create a meaningful sentence
sentence = "I bombed this problem in Introduction to C++ I hope you do better"

# break sentence in various words
words = sentence.split(" ")

# create new list to hold sentence
pig_latin=list()

# iterate through words in sentence

### YOUR CODE HERE ###
for w in words:
    if len(w) < 3:
        pig_latin.append(w)
    elif starts_with_vowel(w) == True:
        new_w = w[0:] + "vay"
        pig_latin.append(new_w)
    elif starts_with_vowel(w) == False:
        new_w = w[1:] + w[0] + "ay"
        pig_latin.append(new_w)
    else:
        continue

# re-assemble list of words into string
new_sentence = ""
for w in pig_latin:
    new_sentence += w + " "

# print out final sentence
print(new_sentence)

def repeated_word(str1):
    lower = make_lower(str1)
    split_lower = splitter(lower)

    temp = []
    for word in split_lower:
        if word in temp:
            return word
        else:
            temp.append(word)
    return 'None'

def make_lower(original_str):
    lower = ''
    for word in original_str:
        lower += word.lower()
    return lower

def splitter(lower_str):
    split = lower_str.replace(", ", " ").split(' ')
    return split

# if __name__ == "__main__":
#     word = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

#     print(repeated_word(word))
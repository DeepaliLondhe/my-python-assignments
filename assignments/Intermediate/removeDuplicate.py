# remove duplicate from the given line

def remove_duplicate_chars(line: str)->str:
    results = " "
    for word in line:
        if word not in results:
            results += word
    return results


def remove_duplicate_words(sentence: str) -> str:
    words = sentence.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return " ".join(unique_words)

line = input("Enter a sentence: ")

print("Without duplicate characters:", remove_duplicate_chars(line))
print("Without duplicate words:", remove_duplicate_words(line))

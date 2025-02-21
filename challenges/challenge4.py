def operations(sentence):
    # Count the number of words
    word_count = len(sentence.split())
    
    # Reverse the order of words
    reversed_sentence = ' '.join(sentence.split()[::-1])
    
    # Replace all spaces with hyphens
    modified_sentence = sentence.replace(' ', '-')
    
    print(f"Number of words: {word_count}")
    print(f"Reversed sentence: {reversed_sentence}")
    print(f"Modified sentence: {modified_sentence}")


sent = input("Enter a sentence: ")
operations(sent)
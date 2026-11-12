# Frequency counter using dictionaries.
#* Frequency Counter Using Dictionaries: Develop a Python program to count
#the frequency of words in a sentence or occurrences of elements in a list using
#dictionaries.
#* Analyze input data, implement frequency counting, and verify the
#accuracy of the output. (CT)
#* Apply frequency counting to survey responses, classroom feedback, or
# product preferences and interpret the findings. (RWE)

words = input("Enter a sentence: ").split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
    print("Word Frequency:")
    print(freq)
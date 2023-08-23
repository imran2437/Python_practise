def linear_search_string(arr, target):
    for i, word in enumerate(arr):
        if word == target:
            return i
    return -1

word_list = ['apple', 'banana', 'cherry', 'date', 'fig']
target_word = 'cherry'
result = linear_search_string(word_list, target_word)
if result != -1:
    print(f"Target word '{target_word}' found at index {result}")
else:
    print(f"Target word '{target_word}' not found in the list.")

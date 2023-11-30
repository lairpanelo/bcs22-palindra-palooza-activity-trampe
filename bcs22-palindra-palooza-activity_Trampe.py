class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            self.top = temp.next
            temp = None

    def display(self):
        if self.top is None:
            print("Empty Stack")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

def clean_sentence(sentence):
    cleaned_sentence = ''.join(ch.lower() for ch in sentence if ch.isalpha())
    return cleaned_sentence

def is_palindrome_sentence(sentence):
    cleaned_sentence = clean_sentence(sentence)
    stack = Stack()

    for char in cleaned_sentence:
        stack.push(char)

    reversed_sentence = ''
   
    
    while stack.top:
        reversed_sentence += stack.top.data
        stack.pop()

    return cleaned_sentence == reversed_sentence

while True:
    input_sentence = input("\nEnter a sentence to check if it's a palindrome: ")
    print("Original Sentence:", input_sentence)
    
    result = is_palindrome_sentence(input_sentence)
    print("Is it a palindrome?:", result)
    
    if result:
        print("The sentence is a palindrome because it reads the same forward and backward, "
              "ignoring spaces, punctuation, and capitalization.")
    else:
        print("The sentence is not a palindrome.")

    choice = input("\nDo you want to check another sentence? (Y/N): ").strip().lower()
    if choice != 'y':
        break

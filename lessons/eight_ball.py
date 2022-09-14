from random import randint

your_question: str = input("ask a question: ")
my_response: int = randint(0,2)
response_mapping = {0:"nah man fake news", 1:"ayo, it might be true", 2:"Yes, it shall be"}

print(response_mapping[my_response])
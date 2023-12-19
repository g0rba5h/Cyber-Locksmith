import string
import itertools

def generate_combinations():
    phrase = "Alpha-Zero"
    criteria = [chr(i) for i in range(32, 127) if chr(i) not in string.ascii_letters and chr(i) not in string.digits]

    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    
    combinations = itertools.product(criteria, lowercase_letters, numbers, lowercase_letters, numbers)
    
    with open("combinations.txt", "w") as file:
        for combo in combinations:
            new_phrase = phrase + ''.join(combo)
            file.write(new_phrase + '\n')

if __name__ == "__main__":
    generate_combinations()
    print("Combinations generated and saved in 'combinations.txt'")


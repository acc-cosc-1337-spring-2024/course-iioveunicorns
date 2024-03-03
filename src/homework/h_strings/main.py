#
import strings

while True:
    response = int(input("""
    Menu:
    1 - Hamming Distance
    2 - DNA Complement
    3 - Exit
    Input Menu Selection: """))
    valid_responses = [1, 2, 3]

    if response not in valid_responses:
        print("Invalid Selection. Please choose one from the Menu...")
        continue

    elif response == 1:
        while True:
            dna1 = str(input("Input First Sequence: "))
            dna2 = str(input("Input Second Sequence: "))

            if len(dna1) != len(dna2):
                print("Please make strings equal length.")
                continue

            hamming_distance = strings.get_hamming_distance(dna1, dna2)
            print(f'\nThe hamming distance of {dna1} and {dna2} is {hamming_distance}')
            break
        continue
    
    elif response == 2:
        dna = str(input("Input DNA sequence: "))
        complement = strings.get_dna_complement(dna)
        print(f'\nThe complement of {dna} is {complement}')
        continue
    elif response == 3:
        print("Exiting Program...")
        break

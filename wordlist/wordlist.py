import itertools
import argparse

def generate_wordlist(characters, min_length, max_length, output_file):
    with open(output_file, "w") as f:
        for length in range(min_length, max_length + 1):
            for combination in itertools.product(characters, repeat=length):
                print(combination)
                f.write("".join(combination) + "\n")
    print(f"Wordlist generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a wordlist based on given parameters.")
    parser.add_argument("-c", "--characters", type=str, required=True, help="Characters to use in the wordlist.")
    parser.add_argument("-min", "--min_length", type=int, required=True, help="Minimum length of words.")
    parser.add_argument("-max", "--max_length", type=int, required=True, help="Maximum length of words.")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output file name.")
    
    args = parser.parse_args()
    
    generate_wordlist(args.characters, args.min_length, args.max_length, args.output)

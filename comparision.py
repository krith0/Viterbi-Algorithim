from difflib import SequenceMatcher

def calculate_match_percentage(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        text1 = file1.read()
        text2 = file2.read()

        # Create a SequenceMatcher object
        matcher = SequenceMatcher(None, text1, text2)

        # Get the matching blocks
        matching_blocks = matcher.get_matching_blocks()

        # Calculate the total matching characters
        total_matches = sum(block.size for block in matching_blocks)

        # Calculate the match percentage
        match_percentage = (total_matches / max(len(text1), len(text2))) * 100

        return match_percentage

if __name__ == "__main__":
    file1_path = "decoded bits.txt"  # Replace with the path to your first text file
    file2_path = "input_bits.txt"  # Replace with the path to your second text file

    match_percentage = calculate_match_percentage(file1_path, file2_path)
    print(f"Match Percentage: {match_percentage:.2f}%")

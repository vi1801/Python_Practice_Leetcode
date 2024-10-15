import re

def extract_mentions(message):
    # Correct regular expression pattern
    pattern = r'@id([1-9]\d{0,2})'  # Matches @id1 to @id999

    # Find all matches in the message
    matches = re.findall(pattern, message)

    # Prepend 'id' to each number to match the original format
    valid_mentions = [f'id{num}' for num in matches]

    return valid_mentions

# Sample group chat messages
messages = [
    "This is an example with no mentions",
    "This is an example with one mention of one user @id2",
    "This is an example with @id1, id173, id983 one mention of three users",
    "This is an example with sint, id1/id1983 several mentions"
]

for msg in messages:
    print(extract_mentions(msg))

if __name__ == "__main__":
    msg = "Here is a mention with @id12"
    print(extract_mentions(msg))  # Test with a specific message

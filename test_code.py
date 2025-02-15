fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

# Create empty dictionary for word counts
word_counts = dict()

try:
    with open(fname) as fh:
        for line in fh:
            # Convert to lowercase and split into words
            words = line.lower().split()
            
            # Count each word
            for word in words:
                # Remove punctuation if needed
                word = word.strip('.,!?:;')
                # Add or increment word count using get()
                word_counts[word] = word_counts.get(word, 0) + 1

    # Print results sorted by count
    print("\nWord count results:")
    print("-----------------")
    
    # Sort dictionary items by count (descending)
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Print top 10 most common words
    print("Top 10 most common words:")
    for word, count in sorted_counts[:10]:
        print(f"{word}: {count}")
    
    # Print total unique words
    print(f"\nTotal unique words: {len(word_counts)}")

except FileNotFoundError:
    print(f"File {fname} not found")
except Exception as e:
    print(f"An error occurred: {e}")
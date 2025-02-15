name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
    hours = dict()

    for line in handle:
        if line.startswith('From '):
            # Split line into words
            words = line.split()
            # Get time string (6th word)
            time = words[5]
            # Split time by colon and get hour
            hour = time.split(':')[0]
            # Count occurrences of each hour
            hours[hour] = hours.get(hour, 0) + 1

    # Sort and print the hours and counts
    for hour in sorted(hours.keys()):
        print(hour, hours[hour])

except FileNotFoundError:
    print("File cannot be opened:", name)
except IndexError:
    print("File format is incorrect")
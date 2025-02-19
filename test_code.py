import urllib.request
import json

def extract_comments():
    # Prompt for URL
    url = input('Enter URL: ')
    if not url:
        url = 'http://py4e-data.dr-chuck.net/comments_2172836.json'
    
    print('Retrieving:', url)
    
    try:
        # Read JSON data from URL
        data = urllib.request.urlopen(url).read()
        print('Retrieved', len(data), 'characters')
        
        # Parse JSON
        json_data = json.loads(data)
        
        # Extract comment counts and calculate sum
        comments = json_data['comments']
        total = sum(comment['count'] for comment in comments)
        
        print('Count:', len(comments))
        print('Sum:', total)
        
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    extract_comments()
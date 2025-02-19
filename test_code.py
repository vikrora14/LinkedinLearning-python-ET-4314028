import urllib.request
import urllib.parse
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_plus_code(address):
    serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
    params = {'q': address}
    
    # Create the full URL with encoded parameters
    url = serviceurl + urllib.parse.urlencode(params)
    print('Retrieving', url)
    
    try:
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        # Print the raw JSON string:
        print("Raw JSON:", data)
        
        # Parse JSON
        js = json.loads(data)
        
        # Print the parsed JSON (Python dictionary):
        print("Parsed JSON:", json.dumps(js, indent=2))
        
        # Now see if 'plus_code' is at the top-level or nested
        if 'plus_code' in js:
            print('Top-level plus_code:', js['plus_code'])
            return js['plus_code']
        else:
            print('No top-level plus_code found in JSON')
            return None
    except Exception as e:
        print('Error:', e)
        return None

def main():
    address = input('Enter location: ')
    if not address:
        address = 'Transilvania University'
    plus_code = get_plus_code(address)
    print("Plus code is:", plus_code)

if __name__ == '__main__':
    main()

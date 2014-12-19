'''Get small items from log.'''
import sys
import json


THRESHOLD = 6000000


def main():
    for line in sys.stdin:
        if not line:
            break
        
        doc = json.loads(line)
        
        if doc['bytes']['data'] < THRESHOLD:
            print(doc['item'], doc['bytes']['data'], doc['at'])


if __name__ == '__main__':
    main()

'''Drain the done set that uses up the memory in the tracker.'''
import redis
import time

def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    with open('done_set_data-{0}.txt'.format(int(time.time())), 'ab') as f:
        while True:
            item = r.spop('puush:done')
            
            if item:
                f.write(item)
                f.write('\n')
            else:
                break
                
if __name__ == '__main__':
    main()
            

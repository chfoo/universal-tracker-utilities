'''Drain the done set that uses up the memory in the tracker.'''
import redis
import time

def main():
    prefix = 'puush'
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    with open('done_set_{1}_data-{0}.txt'.format(int(time.time()), prefix), 'ab') as f:
        while True:
            item = r.spop('{0}:done'.format(prefix))
            
            if item:
                f.write(item)
                f.write('\n')
            else:
                break
                
if __name__ == '__main__':
    main()
            

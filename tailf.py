import time

def watch(fn,count):
    fp = open(fn, 'r')
    while True:
        new = fp.readline()

        if new and count==0:
            yield (new)
                    
        elif count>0:
            count = count-1
        else:
            time.sleep(0.5)

fn = 'example.txt'
fp = open(fn, 'r')
count=0

for line in fp:
    count += 1
count = count-10
fp.close()
for hit_sentence in watch(fn,count):
    print (hit_sentence)

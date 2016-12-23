#coding=utf-8
import os
import sys

def separate_stereo(stereo):
    try:
        inStereo = open(stereo, "rb")
        new_sub_dir = inStereo.name.replace(".pcm", "")
        print "name %s" % (new_sub_dir)

        if not os.path.exists(new_sub_dir):
            os.makedirs(new_sub_dir)
            
        stream_stereo = inStereo.read()
    except Exception, e:
        print e
        return
    try:
        left_dir = "%s\\left.pcm"%(new_sub_dir)
        print left_dir
        outLeft = open(left_dir, "wb")
    except Exception, e:
        print e
        return
    try:
        right_dir = "%s\\right.pcm"%(new_sub_dir)
        print right_dir
        outRight = open(right_dir, "wb")
    except Exception, e:
        print e
        return
    index = 0
    sum = len(stream_stereo)
    print sum
    while index + 4 < sum:
        outLeft.write(stream_stereo[index + 0])
        outLeft.write(stream_stereo[index + 1])
        outRight.write(stream_stereo[index + 2])
        outRight.write(stream_stereo[index + 3]) 
        index = index + 4

    inStereo.close()
    outLeft.close()
    outRight.close()
    
def separate_stereo_dir(path):
    allFile = os.listdir(path)
    for f in allFile:
        target = "%s/%s"%(path, f)
        print target
        separate_stereo(target)
    
#argv = str(sys.argv)
#print "argv: " + argv
target = raw_input("target:")
print target
#separate_stereo("stereo.pcm")
if os.path.isdir(target):
    separate_stereo_dir(target)
else:
    separate_stereo(target)
    

# Python script to store a .BIT file in the XuLA Flash.

import sys
import time

from xula import XuLA, elapsed
from bitstream import Bitstream, BitstreamHex, BitFile

def main(bitfilename):
    x = XuLA()
    t = time.time()
    x.write_flash(BitFile(bitfilename), 0, True)
    t = time.time() - t
    print "download complete, took", elapsed(t)

if __name__ == "__main__":
    print "XuLA Flash downloader"
    if len(sys.argv) != 2:
        print "usage: python %s <bitfile>" % sys.argv[0]
        sys.exit(1)
    main(sys.argv[1])

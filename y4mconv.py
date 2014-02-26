#!/usr/bin/python

# @@--
#  Copyright (C) 2014 Alberto Vigata
#  All rights reserved
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met
#  
#      * Redistributions of source code must retain the above copyright
#        notice, this list of conditions and the following disclaimer.
#      * Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#      * Neither the name of the University of California, Berkeley nor the
#        names of its contributors may be used to endorse or promote products
#        derived from this software without specific prior written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND ANY
#  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE LIABLE FOR ANY
#  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 

import re
import sys
from optparse import OptionParser

def fromy4m2yuv(options):
    """ takes a y4m file and transforms it into a raw yuv file """
    out_file = open(options.outfile, 'wb')
    in_file = open(options.infile, 'rb' )

    header = in_file.readline()

    width = (re.compile("W(\d+)").findall(header))[0]
    height = (re.compile("H(\d+)").findall(header))[0]

    framesize = int(width)*int(height)*3/2;
    print("{0}x{1} framesize={2}".format(width,height,framesize))

    c=0

    #FIXME this needs to support other formats than 420
    while True:
        frame_header = in_file.readline()
        if(frame_header.startswith('FRAME')==False): 
            print('End of Sequence')
            return
        frame = in_file.read(framesize)
        out_file.write(frame)

        sys.stdout.write("\r{0}".format(c));
        sys.stdout.flush()
        c+=1

    print("")
    in_file.close()
    out_file.close()
    return



def fromyuv2y4m(options):
    #open out file
    out_file = open(options.outfile, 'wb')
    in_file = open(options.infile, 'rb' )

    if options.width==None or options.height==None:
        print("Must provide width and height for y4m output")
        return

    if options.num==None or options.den==None:
        options.num=25
        options.den=1


    #write header
    out_file.write("YUV4MPEG2 W{width} H{height} F{num}:{den} Ip A0:0 C420jpeg\n".format(width=options.width,height=options.height,num=options.num,den=options.den))

    framesize = int(options.width)*int(options.height)*3/2;
    print("frame size is {0}".format(framesize))
    print("writing frame ... ")
    c=0;

    while True:
        frame = in_file.read(framesize)
        if(frame==""):
            break;
        out_file.write("FRAME\n");
        out_file.write(frame);
        sys.stdout.write("\r{0}".format(c));
        sys.stdout.flush()
        c+=1

    print("")
    in_file.close()
    out_file.close()
    return


def main(argv):
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="infile", help="the input file")
    parser.add_option("-o", "--output", dest="outfile", help="the output file")
    parser.add_option("-w", "--width", dest="width", help="the width")
    parser.add_option("-e", "--height", dest="height", help="the height")
    parser.add_option("-f", "--format", dest="format", help="the format")
    parser.add_option("-n", "--num", dest="num", help="the numerator of framerate")
    parser.add_option("-d", "--den", dest="den", help="the denominator of framerate")

    (options, args) = parser.parse_args()

    if options.infile == None or options.outfile==None:
        print("and input and output file must be provided")
        return


    if options.infile.find('.y4m')== -1:
        try:
            fromyuv2y4m(options)
        except:
            print("there was a problem reading the y4m file")
    else:
        try:
            fromy4m2yuv(options)
        except:
            print("there was a problem converting the yuv file")


if __name__ == "__main__":
    main(sys.argv)



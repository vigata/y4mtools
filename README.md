y4mtools 
========
ffmpeg-less, pure python, y4m conversion tools

## Y4MCONV ##
Y4M is an increasingly popular format for yuv sequences due to the fact that it includes the basic format data embedded in the file. Old style YUV files are just raw pixel data which has always carried challenges in terms of metadata management. 
Y4MCONV is a utility to convert from yuv to y4m. 


## Y4M to YUV conversion ##
Use y4mconv to convert from Y4M files to raw YUV files. For example:

```
y4mconv.py -i input.y4m -o output.yuv 
```

It's important to note that yuv files are raw pixel data so all information about resolution and framerate is lost in this conversion.
Y4MCONV however, generates a metadata file in json format with the same name of the output yuv file that contains all the relevant format information about the sequence.

To query information about a Y4M file simply do:

```
y4mconf.py -i input.y4m
```



## YUV to Y4M conversion ##

To create Y4M files from a yuv you can:

```
y4mconv.py -i input.yuv -o output.y4m -w WIDTH -e HEIGHT -num 25 -den 1
```

Because YUV files are naked you need to explicitely set the width and the height. Notice that the height parameter is set with the '-e' option due the fact that '-h' brings up the help. The framerate of the file is determined by num/den 

## Help ##

For all supported options type:

```
y4mconv.py -h
```

## Author ##
Check my other projects like [codecbench], [CABSscore specification], or my very own [linked in profile](http://www.linkedin.com/in/vigata)


[CABSscore specification]:http://codecbench.nelalabs.com/cabs
[codecbench]:http://github.com/vigata/codecbench
[alberto vigata]:http://www.linkedin.com/in/vigata
[Image Quality Assessment (IQA)]:http://tdistler.com/iqa/

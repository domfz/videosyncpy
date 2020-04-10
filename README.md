# videosyncpy
Videosyncpi will be able to sync a mp4 to the beat of a mp3 file. It will use [ffmpeg](https://www.ffmpeg.org/) and probably [something from here](https://wiki.python.org/moin/PythonInMusic).

## Requirements

You need to have [ffmpeg](https://www.ffmpeg.org/) on your machine. How to install it on windows you can find [here](https://www.youtube.com/watch?v=qjtmgCb8NcE). This can change, I will try to include everything needed in this repository.

## QuickStart
You need a mp4 and mp3 file *having the same length*

Put your files in the **same** directory and simply call
`videosyncpy -v  'videofile.mp4' -m 'musicfile.mp3'`

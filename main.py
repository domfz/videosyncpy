import argparse
import ffmpeg

parser = argparse.ArgumentParser(description='Sync your mp4 file to the beat of a mp3.')
parser.add_argument('-v', metavar='--videofile', type=str, help='The videofile you want to sync')
args = parser.parse_args()

stream = ffmpeg.input(args.v)

stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')

ffmpeg.run(stream)

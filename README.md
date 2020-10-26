I had a bunch of wav files I had smapled from various sources.

However, in order to use them in the AKAI MPC 2500 and 1000 models,
including JJOS, the file names must be 16 characters max, and the
file must be WAV at 44.1k smaple rate.

The only dependency is ffmpeg, otherwise, this is currently built
with only python3 standard libraries.

TODO:
- sometimes this doesn't work!  What?!  First try isn't perfect?
- make a real argument parser
- add more saftey to avoid overwriting the provided file

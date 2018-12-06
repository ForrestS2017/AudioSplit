#!/usr/bin/env python

"""
AudioSplit takes in audio files and
corresponding text files with times
and names of where to split the audio
file and what to name the new file(s)

Parameters
----------
first :
    directory containing audio files
    and text files

Returns
-------
directory
    contains subdirectories of each
    audio file

Raises
------
...
"""

__author__ = "Forrest Smith"
__credits__ = ["Rob Knight"]

__version__ = "0.0.1"
__maintainer__ = "Forrest Smith"
__email__ = "fsmith2017@gmail.com"
__status__ = "Development"

import sys
import os.path

class Track(object):
    def __init__(self, trackName, length):
        self.trackName = trackName
        self.length = length

def SplitTracks(inputPath, outputPath):
    print('test')


def getFiles(inputPath, outputPath):
    result = []
    result.append(sorted([file for file in os.listdir(inputPath) if file.endswith('.mp3')]))
    result.append(sorted([file for file in os.listdir(inputPath) if file.endswith('.mp3')]))

    return result

def getInOutPath():
    """
    Validate user input and set input path

    Args:
        None
    Returns:
        directory
    Raises:
        TypeError: if n is not a number.
        ValueError: if n is negative.
    """

    # Error check
    if len(sys.argv) < 2:
        exit('Please enter input folder containing audio file and timings')

    # Return [input, output]
    return [os.path.join( os.path.dirname(__file__) ,sys.argv[1]+'/'),
            os.path.join( os.path.dirname(__file__) , 'Output/')]


def main():
    # Set input and output paths
    inputPath, outputPath = getInOutPath()

    # Get and verify file names
    audioFiles, audioTracks = getFiles(inputPath, outputPath)

    print(audioFiles)
    print(audioTracks)


    #SplitTracks(inputPath, outputPath)

    exit('Successfully Split')

if __name__ == '__main__':
    main()




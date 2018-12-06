#!/usr/bin/env python
# pylint: disable=unbalanced-tuple-unpacking
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
__credits__ = ["Forrest Smith"]

__version__ = "0.0.1"
__maintainer__ = "Forrest Smith"
__email__ = "fsmith2017@gmail.com"
__status__ = "Development"

from fileutils import *

class Track(object):
    def __init__(self, trackName, length, metadata):
        self.trackName = trackName
        self.length = length
        self.metadata = metadata

    def export(self):
        print('exporting...')


def SplitTrack(inPath, AudioPath, ListPath):

    """Returns a list of valid audio files and track listings

    Keyword arguments:
        AudioPath -- the path of the audio file
        ListingPath -- the path of the listing file
    """
    print('vv' + '---'*20 + 'vv')
    print(AudioPath + ' | ' + ListPath)

    ## Handle Listings First ##
    Listings = dict()
    with open(inPath+ListPath, 'r') as ListFile:
        lines = [line for line in ListFile]
        if not parseLine(lines):
            exit('Could not read anything in: ' + ListPath)





def main():
    print('\n')
    # Set input and output paths
    inputPath, outputPath = getInOutPath()

    # Get and verify file names
    audioFiles, audioLists = getFiles(inputPath)

    #print(audioFiles)
    #print(audioTracks)

    for i in range(len(audioFiles)):
        SplitTrack(inputPath, audioFiles[i], audioLists[i])

    exit('Successfully Split')


if __name__ == '__main__':
    main()




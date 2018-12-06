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
import subprocess as sp

class Track(object):
    def __init__(self, trackName, length, metadata):
        self.trackName = trackName
        self.length = length
        self.metadata = metadata

    def export(self):
        print('exporting...')


def SplitTracks(inPath, AudioFiles, AudioLists):

    """Returns a list of valid audio files and track listings

    Keyword arguments:
        AudioPath -- the path of the audio file
        ListingPath -- the path of the listing file
    """

    ## Error check
    if len(AudioFiles) < 1:
        exit('No audio files found')

    ## Handle Listings First ##
    Listings = dict()
    for i in range(len(AudioFiles)):

        ListPath = AudioLists[i]
        AudioPath = AudioFiles[i]

        # print('vv' + '---'*20 + 'vv')
        # print(AudioPath + ' | ' + ListPath)

        with open(inPath+ListPath, 'r') as ListFile:
            lines = [line for line in ListFile]
            songs = parseLines(lines)
            if not songs:
                exit('Could not read anything in: ' + ListPath)
            Listings[AudioPath] = songs
    
    printDict(Listings)





def main():
    print('\n')
    # Set input and output paths
    inputPath, outputPath = getInOutPath()

    # Get and verify file names
    audioFiles, audioLists = getFiles(inputPath)

    #print(audioFiles)
    #print(audioTracks)

    SplitTracks(inputPath, audioFiles, audioLists)

    exit('Successfully Split')


if __name__ == '__main__':
    main()




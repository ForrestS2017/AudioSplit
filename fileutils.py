import os.path
import sys
import re

def getFiles(inputPath):
    """Returns a list of valid audio files and track listings

    Keyword arguments:
        inputPath -- the directory containing input files
    """

    result = []
    result.append(sorted([file for file in os.listdir(inputPath) if file.endswith('.mp3')]))
    result.append(sorted([file for file in os.listdir(inputPath) if file.endswith('.txt')]))

    # Exit on non-existent files
    if len(result[0]) < 1: exit('No input files found')
    if len(result[1]) < 1: exit('No track listings found')

    # If some audio files don't have album listings, don't include them in your list
    for song in result[0]:
        if (song[:-4] + '.txt') not in result[1]:
            print('No track listings found for file: ', song)
            result[0].remove(song)

    return result

def getInOutPath():
    """Returns a list of valid audio files and track listings

    Keyword arguments:
        inputPath -- the directory containing input files
    """

    # Error check
    if len(sys.argv) < 2:
        exit('Please enter input folder containing audio file and timings')

    # Return [input, output]
    return [os.path.join( os.path.dirname(__file__) ,sys.argv[1]+'/'),
            os.path.join( os.path.dirname(__file__) , 'Output/')]

def parseLine(lines):
    """Takes generic Track listing (w,w/o hyphen) and returns [Title, timestamp, lenth]

        Keyword arguments:
            lines - strings of track listing
    """
    # Error check
    if len(lines) < 1 or lines == None:
        return -1
    songs = []
    # Parse each line into 
    for line in lines:
        length = len(line)
        temp = ""
        s = re.findall(r'^([0-9][0-9]):([0-9][0-9])( *-* *)([a-zA-Z0-9_ -]*$)',line)
        # [min, sec, separator, title]
        currentSong = [s[0][0]+':'+s[0][1], s[0][3]]
        songs.append(currentSong)
    
    # Get times of each song
    for i in range(len(songs)):
        if i < len(songs) -1:
            start = 60*int(songs[i][0][:2]) + int(songs[i][0][3:])
            end = 60*int(songs[i+1][0][:2]) + int(songs[i+1][0][3:])
            songs[i].append(end-start)
    print(*songs, sep='\n')

    # TODO - Get last song length

    return [lines]
import os.path, sys, re, ffmpeg, subprocess as sp

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

    dirName = 'Output'
 
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        if os.path.exists(dirName): print('Directory {} created'.format(dirName))


    # Return [input, output]
    return [os.path.join( os.path.dirname(__file__) ,sys.argv[1]+'/'),
            os.path.join( os.path.dirname(__file__) , 'Output/')]

def parseLines(lines):
    """Takes generic Track listing (w,w/o hyphen) and returns [Title, timestamp, lenth]

        Keyword arguments:
            lines - strings of track listing
    """
    # Error check
    if len(lines) < 1 or lines == None:
        return -1
    songs = []
    timing = 0
    # Parse each line into 
    for line in lines:
        length = len(line)
        temp = ""
        s = re.findall(r'^([0-9][0-9]:)*([0-9][0-9]):([0-9][0-9])( *-* *)([a-zA-Z0-9_ -]*$)',line)
        # [hour, min, sec, separator, title]
        if s[0][0] == '':
            currentSong = [s[0][4].strip(), ('00:'+s[0][1]+':'+s[0][2]).strip()]
        else:
            currentSong = [s[0][4].strip(), (s[0][0][:2]+':'+s[0][1]+':'+s[0][2]).strip()]
        songs.append(currentSong)
    
    # Get times of each song
    for i in range(len(songs)):
        if i < len(songs) -1:
            start = songs[i][1].split(':')
            start = 360*int(start[0]) + 60 * int(start[1]) + int(start[2])
            end = songs[i+1][1].split(':')
            end = 360*int(end[0]) + 60 * int(end[1]) + int(end[2])
            timing += end - start
            songs[i].append(end-start)

    # TODO - Get last song length

    return songs, timing

def splitExport(inputPath, outputPath, Listings):
    """Takes input and output path and the track list to export the individual tracks

        Keyword arguments:
            lines - strings of track listing
    """

    ## Error check
    if not inputPath or not outputPath or not Listings:
        exit('Error passing listings')

    commandString = 'ffmpeg -i {tr} -ss {st} -t {ln} -acodec copy {nm}.mp3'
    

    for key in dict.keys(Listings):
        albumTitle = key[:-4]
        albumFolder = outputPath + albumTitle
        
        ## Create album folder in Output/ if DNE
        if not os.path.exists(albumFolder):
            os.mkdir(albumFolder)

        for item in Listings[key]:
            source = '"' + inputPath + key + '"'
            start = item[1]
            length = item[2]
            name = '"' + albumFolder + '/' + item[0] + '"'
            
            ## Handle command line arguments with ffmpeg. Allow overwriting
            command = commandString.format(tr=source, st=start, ln = length, nm=name)
            with sp.Popen([command],stdin=sp.PIPE, stdout=sp.PIPE, shell=True, universal_newlines=True) as p:
                p.communicate('y') # allow overwiting

    return

def printDict(input):
    for item in input:
        print(item)
        for entry in input[item]:
            print('\t',entry)
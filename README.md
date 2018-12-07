# AudioSplit
Split an audio file int multiple audio files at user discretion.

## Deployment Instructions
Launch your terminal in the folder containing AudioSplit.py
Enter the following to clone and use the project
```sh
$ git clone https://github.com/ForrestS2017/AudioSplit.git
$ python3 AudioSplit.py <Input Folder>
```
Where <Input Folder> is the directory of the folder containing your input

## Input & Output
Your `Input Folder` Should contain your audio files with matching text files containing the track listings
In order for an audio file to be split, there must be a corresponding `.txt` file in the format below:

### Accepted File Types
Audio: `mp3` `wav` `flac`<br/>
Track Lists: `txt`

Track List format:
`HH:MM:SS - <title>` where the hours and hypen are not necessary, but are acceptable

### Examples:

Input Audio File: 
`Hyakkei - Okurimono.mp3`

Input Track Listing File:
`Hyakkei - Okurimono.txt`

`00:00 Reading<br/>
03:46 Flying Carpet<br/>
07:50 Sky Walk<br/>
12:25 Mackerel Sky<br/>
17:14 Town Light<br/>
22:40 Sea Library<br/>
27:53 Pleasant Talk<br/>
30:35 Gata Goto Gata<br/>
33:50 My Waltz<br/>
37:00 Over The Night<br/>
41:03 Nano Flower<br/>
44:37 Yellow Jackets`<br/>


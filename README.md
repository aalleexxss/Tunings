# Tunings
A python program for generating scale shapes for any guitar tuning.

## Background Info
Before getting into the code, we need to first understand a little bit about scales. Every scale comes from a set
of 12 notes known as the chromatic scale. Each scale is defined by a key and mode. The key represents the 
starting note of the scale and the mode represents the steps taken to get the rest of the notes in the scale.
For example, the C major scale can be obtained from the chromatic scale as follows:

![Scale](https://github.com/aalleexxss/Tunings/blob/main/images/scale.png?raw=true)

Thus the notes in a C major scale are C, D, E, F, G, A, and B.

## Program Flow

![Program flow](https://github.com/aalleexxss/Tunings/blob/main/images/programFlow.png?raw=true)

Upon starting the program, the user is prompted to select a guitar tuning. This can be done by manually entering
the note of each string, or by loading a saved tuning. From here, all the notes of the fretboard are generated.
Next the user can print the fretboard, save the current tuning, enter a scale, or change the tuning.

## How it Works

**Setting a tuning -** A user can set the current tuning by either entering the note of each string, or by loading
in a saved tuning. Tunings are saved in a text file where one line is the name of the tuning, and the next line is 
the notes of the tuning separated by commas. The tuning is then saved in an array as a numeric representation. The 
numeric representation simply maps the notes A through G# to the numbers 1 through 12.

**Generating the fretboard -** Once the tuning is set, the fretboard can be created. Because the current tuning is in
a numeric representation, this is very straight forward. The tuning array represents the notes of the open strings of 
the fretboard, so in order to get the notes of the first fret all we have to do is add 1 to each element of the tuning
array. This proces of adding 1 to the previous fret to get the current fret continues all the way up the fretboard. 
We run into a slight problem when trying to add 1 to 12 (G#), but this is solved with modular division.

**Setting a scale -** To get a scale, the user must input the key and mode of the scale. The key is saved as a single
integer and the mode is saved as an integer array representing the steps of the scale. From the mode and key, an integer
array of all the notes in the scale is made. After this, we can iterate through the fretboard and check if each note
is part of the scale.

## Future Improvements 

This program could be improved by making it more generalized. For example, this program can only generate scales for a
six-string guitar. This could be changed by having the user input the number of strings before entering a tuning. 
Another improvement would be adding a GUI instead of doing everything through a text interface. 

## How to Run This Program

Simply clone this repository, or just the ````/code```` directory, then open ````tunings```` in your favorite IDE.
Note that stored_tunings.txt is the text file used to save and load tunings.

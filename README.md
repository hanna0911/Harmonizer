# Harmonizer
2018 Summer, CTY CS Project



## Content

- Purpose
  - Why this project
  - Why MIDI
    - Brief intro of MIDI files
- Programming Process
  - Module ‘MIDO’
  - Structure of the code
- Demonstration
- Difficulties Solved
- Improvement



## Purpose

- Why this project
  - Finding the chords is essential in making accompaniment for a song
  - Automatically harmonizing single-note melodies is efficient 
- Why MIDI



### Brief info of MIDI files

- Musical Instrument Digital Interface
- 19c 80s
- Gives information of (with bytes, instead of Audio)
  - Type of instrument (Single/Multiple tracks)
  - Tempo, time signature…
  - Notes
    - Pitch, velocity, lasting time (ticks)…
- Why MIDI (Advantages)
  - small file size
  - ease of modification and manipulation
  - wide choice of electronic instruments



## Programming Process  

- Module ‘MIDO’
  - Converts the original format into a much more readable format
- Structure of the code
  - Import module
  - Setup
  - Greetings/Instructions
  - Input Melody
  - Track down information of the Melody
  - Process the information
    - Find every bar
    - Find the chord for each bar
  - Apply the information into the Harmony
    - Multiple sound tracks based on the chord
  - Output



## Demonstration



## Difficulties Solved

- How to mark down certain notes
  - Using lists tracking down the value of the note per time of a sixteenth note
- How to find the time (ticks) of each bar
  - Ticks per beat
    - Ticks per quarter note = ticks per beat
    - Ticks per sixteenth note = ticks per beat / 4
  - The number of ‘sixteenth notes’ per bar = Numerator / Denominator * 16
  - The time of each bar = The number of ‘sixteenth notes’ per bar * ticks per sixteenth note
- Assigning variables
  - a = b
    - if change b; a will change (different from JAVA, C)
  - Import copy; a = copy.deepcopy (b)



## Improvement

- Add more sound tracks
  - Available instrument in this program
    - Piano, Guitar, Violin
  - Existing instruments in MIDI files
    - 128 instruments
- Add more chords
  - Available chords in this program
    - C, Dm, Em, F, G, Am, Bdim, Caug, Dm, E, G#dim
  - Existing chords
    - 144 chords


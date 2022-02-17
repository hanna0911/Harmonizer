# 〇. IMPORT MODULE
from mido import MidiFile, MidiTrack, Message, MetaMessage
import copy

notes = []
chord = [0] * 13
bar = []
mark_bar = 0

c = [0, 4, 7]
dm = [2, 5, 9]
em = [4, 7, 9]
f = [0, 5, 9]
g = [2, 7, 11]
am = [0, 4, 9]
bdim = [2, 5, 11]
caug = [0, 4, 8]
e = [4, 8, 11]
gdim = [2, 8, 11]

move = 0
mami = 1

ma = [c, dm, em, f, g, am, bdim]
mi = [am, bdim, caug, dm, e, f, gdim]

'''
mark_chord_1 = []
mark_chord_2 = []
mark_chord_3 = []
'''

def movechord():
    global move, mami
    if mel_key == 'A':
        move = -3
    if mel_key == 'A#m' or mel_key == 'Bbm':
        move = 1
        mami = 0
    if mel_key == 'Ab':
        move = -4
    if mel_key == 'Abm' or mel_key == 'G#m':
        move = -1
        mami = 0
    if mel_key == 'Am':
        mami = 0
    if mel_key == 'B' or mel_key == 'Cb':
        move = -1
    if mel_key == 'Bb':
        move = -2
    if mel_key == 'Bm':
        move = 2
        mami = 0
    if mel_key == 'C#' or mel_key == 'Db':
        move = 1
    if mel_key == 'C#m':
        move = 4
        mami = 0
    if mel_key == 'Cm':
        move = 3
        mami = 0
    if mel_key == 'D':
        move = 2
    if mel_key == 'D#m' or mel_key == 'Ebm':
        move = 6
        mami = 0
    if mel_key == 'Dm':
        move = 5
        mami = 0
    if mel_key == 'E':
        move = 4
    if mel_key == 'Eb':
        move = 3     
    if mel_key == 'Em':
        move = -5
        mami = 0
    if mel_key == 'F':
        move = 5
    if mel_key == 'F#' or mel_key == 'Gb':
        move = 6
    if mel_key == 'F#m':
        move = -3
        mami = 0
    if mel_key == 'Fm':
        move = -4
        mami = 0
    if mel_key == 'G':
        move = -5
    if mel_key == 'Gm':
        move = -2
        mami = 0
    
    
def removechord(a):
    #print("2.1 when rc", mark_chord_2)
    global ma, mi
    global c, dm, em, f, g, am, bdim, caug, dm, e, gdim
    if a == 0:
        if dm in ma:
            ma.remove(dm)
        if em in ma:
            ma.remove(em)
        if g in ma:
            ma.remove(g)
        if bdim in ma:
            ma.remove(bdim)
        if bdim in mi:
            mi.remove(bdim)
        if dm in mi:
            mi.remove(dm)
        if e in mi:
            mi.remove(e)
        if gdim in mi:
            mi.remove(gdim)
    elif a == 2:
        if c in ma:
            ma.remove(c)
        if em in ma:
            ma.remove(em)
        if f in ma:
            ma.remove(f)
        if am in ma:
            ma.remove(am)
        if am in mi:
            mi.remove(am)
        if caug in mi:
            mi.remove(caug)
        if e in mi:
           mi.remove(e)
        if f in mi:
            mi.remove(f)
    elif a == 4:
        if dm in ma:
            ma.remove(dm)
        if f in ma:
            ma.remove(f)
        if g in ma:
            ma.remove(g)
        if bdim in ma:
            ma.remove(bdim)
        if bdim in mi:
            mi.remove(bdim)
        if dm in mi:
            mi.remove(dm)
        if f in mi:
            mi.remove(f)
        if gdim in mi:
            mi.remove(gdim)
    elif a == 5:
        if c in ma:
            ma.remove(c)
        if em in ma:
            ma.remove(em)
        if g in ma:
            ma.remove(g)
        if am in ma:
            ma.remove(am)
        if am in mi:
            mi.remove(am)
        if caug in mi:
            mi.remove(caug)
        if e in mi:
            mi.remove(e)
        if gdim in mi:
            mi.remove(gdim)
    elif a == 7:
        if dm in ma:
            ma.remove(dm)
        if f in ma:
            ma.remove(f)
        if am in ma:
            ma.remove(am)
        if bdim in ma:
            ma.remove(bdim)
    elif a == 8:
        if bdim in mi:
            mi.remove(bdim)
        if am in mi:
            mi.remove(am)
        if f in mi:
            mi.remove(f)
        if dm in mi:
            mi.remove(dm)
    elif a == 9:
        if c in ma:
            ma.remove(c)
        if em in ma:
            ma.remove(em)
        if g in ma:
            ma.remove(g)
        if bdim in ma:
            ma.remove(bdim)
        if bdim in mi:
            mi.remove(bdim)
        if caug in mi:
            mi.remove(caug)
        if e in mi:
            mi.remove(e)
        if gdim in mi:
            mi.remove(gdim)
    elif a == 11:
        if c in ma:
            ma.remove(c)
        if dm in ma:
            ma.remove(dm)
        if f in ma:
            ma.remove(f)
        if am in ma:
            ma.remove(am)
        if am in mi:
            mi.remove(am)
        if caug in mi:
            mi.remove(caug)
        if dm in mi:
            mi.remove(dm)
        if f in mi:
            mi.remove(f)
    '''
    print(a)
    print('ma:', ma)
    print('mi:', mi)
    #print("2.2 when rc", mark_chord_2)
    '''

def findchord():
    global move
    move = 0
    global mami
    mami = 1
    global c, dm, em, f, g, am, bdim, caug, dm, e, gdim
    c = [0, 4, 7]
    dm = [2, 5, 9]
    em = [4, 7, 9]
    f = [0, 5, 9]
    g = [2, 7, 11]
    am = [0, 4, 9]
    bdim = [2, 5, 11]
    caug = [0, 4, 8]
    e = [4, 8, 11]
    gdim = [2, 8, 11]
    global ma
    ma = [c, dm, em, f, g, am, bdim]
    global mi
    mi = [am, bdim, caug, dm, e, f, gdim]
    

    movechord()

    maxi = 0
    p1 = -1
    p2 = -1
    p3 = -1
    
    if max(chord) > 0:
        for i in range(12):
            if chord[i] > maxi:
                maxi = chord[i];
                p1 = i
        if p1 != -1:
            chord[p1] = 0
        maxi = 0
        if max(chord) > 0:
            for i in range(12):
                if chord[i] > maxi:
                    maxi = chord[i];
                    p2 = i
            if p2 != -1:
                chord[p2] = 0
            maxi = 0
            if max(chord) > 0:
                for i in range(12):
                    if chord[i] > maxi:
                        maxi = chord[i];
                        p3 = i
                if p3 != -1:
                    chord[p3] = 0
    #print (p1, p2, p3)
    place_mark = -1
    #global mark_chord_1, mark_chord_2, mark_chord_3
    mark_chord_1 = []
    mark_chord_2 = []
    mark_chord_3 = []

    if p1 >= 0:
        p1 = p1 - move
        if p1 < 0:
            p1 = p1 + 12
        removechord(p1)
        if mami == 1:
            mark_chord_1 = copy.deepcopy(ma)
        else:
            mark_chord_1 = copy.deepcopy(mi)
        
        #
        #print('1: ', mark_chord_1)
        if p2 >= 0:
            p2 = p2 - move
            if p2 < 0:
                p2 = p2 + 12
            #
            #print('1 before rc: ', mark_chord_1)

            removechord(p2)
            #
            #print('1 after rc: ', mark_chord_1)

            if mami == 1:
                mark_chord_2 = copy.deepcopy(ma)
            else:
                mark_chord_2 = copy.deepcopy(mi)
            #
            #print('2: ', mark_chord_2)

            if len(mark_chord_2) >= 1:
                #
                #print('2.1 before rc: ', mark_chord_2)
                if p3 >= 0:
                    p3 = p3 - move
                    if p3 < 0:
                        p3 = p3 + 12
                    #
                    #print('2.2 before rc: ', mark_chord_2)

                    removechord(p3)
                    #
                    #print('2 after rc: ', mark_chord_2)
                    if mami == 1:
                        mark_chord_3 = copy.deepcopy(ma)
                    else:
                        mark_chord_3 = copy.deepcopy(mi)
                    #
                    #print('3: ', mark_chord_3)
                    #print(len(mark_chord_3))

                    if len(mark_chord_3) >= 1:
                        n1 = mark_chord_3[0][0] + move
                        n2 = mark_chord_3[0][1] + move
                        n3 = mark_chord_3[0][2] + move
                    else:
                        #
                        #print('2 last check: ', mark_chord_2)
                        n1 = mark_chord_2[0][0] + move
                        n2 = mark_chord_2[0][1] + move
                        n3 = mark_chord_2[0][2] + move
                else:
                    n1 = mark_chord_2[0][0] + move
                    n2 = mark_chord_2[0][1] + move
                    n3 = mark_chord_2[0][2] + move
            else:
                n1 = mark_chord_1[0][0] + move
                n2 = mark_chord_1[0][1] + move
                n3 = mark_chord_1[0][2] + move
        else:
            n1 = mark_chord_1[0][0] + move
            n2 = mark_chord_1[0][1] + move
            n3 = mark_chord_1[0][2] + move
    return([n1, n2, n3])
    #
    '''
    print('1', mark_chord_1)
    print('2', mark_chord_2)
    print('3', mark_chord_3)
    '''


def appendchordv1(a):
    t.append(Message('note_on', note = 36 + a[0], velocity = 64, time = 0))
    t.append(Message('note_on', note = 36 + a[1], velocity = 64, time = 0))
    t.append(Message('note_on', note = 36 + a[2], velocity = 64, time = 0))
    t.append(Message('note_on', note = 48 + a[0], velocity = 64, time = 0))
    t.append(Message('note_on', note = 48 + a[1], velocity = 64, time = 0))
    t.append(Message('note_on', note = 48 + a[2], velocity = 64, time = 0))
    t.append(Message('note_on', note = 36 + a[0], velocity = 0, time = sixteenth * spb))
    t.append(Message('note_on', note = 36 + a[1], velocity = 0, time = 0))
    t.append(Message('note_on', note = 36 + a[2], velocity = 0, time = 0))
    t.append(Message('note_on', note = 48 + a[0], velocity = 0, time = 0))
    t.append(Message('note_on', note = 48 + a[1], velocity = 0, time = 0))
    t.append(Message('note_on', note = 48 + a[2], velocity = 0, time = 0))

def appendchordv2(a):
    t.append(Message('note_on', note = 60 + a[0], velocity = 64, time = sixteenth * spb // 4))
    t.append(Message('note_on', note = 60 + a[1], velocity = 64, time = 0))
    t.append(Message('note_on', note = 60 + a[2], velocity = 64, time = 0))
    t.append(Message('note_on', note = 60 + a[0], velocity = 0, time = sixteenth * spb // 4))
    t.append(Message('note_on', note = 60 + a[1], velocity = 0, time = 0))
    t.append(Message('note_on', note = 60 + a[2], velocity = 0, time = 0))
    t.append(Message('note_on', note = 48 + a[2], velocity = 64, time = sixteenth * spb // 4))
    t.append(Message('note_on', note = 48 + a[0], velocity = 64, time = 0))
    t.append(Message('note_on', note = 48 + a[1], velocity = 64, time = 0))
    t.append(Message('note_on', note = 48 + a[2], velocity = 0, time = sixteenth * spb // 4))
    t.append(Message('note_on', note = 48 + a[0], velocity = 0, time = 0))
    t.append(Message('note_on', note = 48 + a[1], velocity = 0, time = 0))

def appendchordg(a):
    t.append(Message('note_on', note = 60 + a[0], velocity = 64, time = 0))
    t.append(Message('note_on', note = 60 + a[0], velocity = 0, time = sixteenth * spb // 8))
    t.append(Message('note_on', note = 60 + a[1], velocity = 64, time = 0))
    t.append(Message('note_on', note = 60 + a[1], velocity = 0, time = sixteenth * spb // 8))
    t.append(Message('note_on', note = 60 + a[2], velocity = 64, time = 0))
    t.append(Message('note_on', note = 60 + a[2], velocity = 0, time = sixteenth * spb // 8))
    t.append(Message('note_on', note = 72 + a[0], velocity = 64, time = 0))
    t.append(Message('note_on', note = 72 + a[0], velocity = 0, time = sixteenth * spb // 8))
    t.append(Message('note_on', note = 72 + a[1], velocity = 64, time = 0))
    t.append(Message('note_on', note = 72 + a[1], velocity = 0, time = sixteenth * spb // 8))
    t.append(Message('note_on', note = 72 + a[0], velocity = 64, time = 0))
    t.append(Message('note_on', note = 72 + a[0], velocity = 0, time = sixteenth * spb // 8))
    t.append(Message('note_on', note = 60 + a[2], velocity = 64, time = 0))
    t.append(Message('note_on', note = 60 + a[2], velocity = 0, time = sixteenth * spb // 8))
    t.append(Message('note_on', note = 60 + a[1], velocity = 64, time = 0))
    t.append(Message('note_on', note = 60 + a[1], velocity = 0, time = sixteenth * spb // 8))

# I. SETUP
from mido import MidiFile, MidiTrack, Message, MetaMessage
print("Welcome to the Harmonizer 1.0")
print()
print("To start the program, please put the melody file you want to harmonize in the same folder as this program.")
print()
hi = input("Type in 'HELP' if you can't find the path of the program: ")
print()
if hi == "HELP" or hi == "help" or hi == "Help":
    print (__file__)
    print()

# II. INPUT MELODY
hi = input("Once you finished putting the file in the correct place, please type in the name of your file: ")
l = len(hi)
if hi[l - 4] == "." and hi[l - 3] == "m":
    filename = hi
else:
    filename = hi + ".mid"
mel = MidiFile(filename)

# III. CORE (Single track melody[not including the head track] & single note per beat)

# 1. Basic Information
mel_numerator = 4
mel_denominator = 4
mel_clocks_per_click = 24
mel_notated_32nd_notes_per_beat = 8
mel_key = 'C'
mel_tempo = 500000
quarter = mel.ticks_per_beat
whole = quarter * 4
half = quarter * 2
eighth = quarter//2
sixteenth = quarter//4

for i, track in enumerate(mel.tracks):
    dtt = 0
    curnote = -1
    prevnote = -1
    curmes = '-1'
    prevmes = 'note_on'
    for msg in track:
        #print(msg)
        if msg.is_meta:
            if msg.type == 'time_signature':
                mel_numerator = msg.numerator
                mel_denominator = msg.denominator
                mel_clocks_per_click = msg.clocks_per_click
                mel_notated_32nd_notes_per_beat = msg.notated_32nd_notes_per_beat
            if msg.type == 'key_signature':
                mel_key = msg.key
            if msg.type == 'set_tempo':
                mel_tempo = msg.tempo
        else:
            if msg.type == 'note_on' or msg.type == 'note_off':
                curmes = msg.type
                if curmes == prevmes:
                    curnote = msg.note
                    if curnote == prevnote:
                        dtt = dtt + msg.time
                    else:
                        dtt = dtt + msg.time
                        for j in range(dtt // sixteenth):
                            notes.append(prevnote)
                        dtt = 0
                    prevnote = msg.note
                else:
                    for j in range(dtt // sixteenth):
                        notes.append(prevnote)
                    dtt = 0
                prevmes = msg.type
    if prevmes == 'note_on' or 'note_off':
        for j in range(dtt // sixteenth):
            notes.append(prevnote)
        dtt = 0
                
len_notes = len(notes)
spb = mel_numerator * 16 // mel_denominator
#print('spb: ' , spb)
#print('16: ', sixteenth)

# 2. Track 0 (Head Track)


t = MidiTrack()
mel.tracks.append(t)
t.append(MetaMessage('time_signature', numerator = mel_numerator, denominator = mel_denominator, clocks_per_click = mel_clocks_per_click, notated_32nd_notes_per_beat = mel_notated_32nd_notes_per_beat))
t.append(MetaMessage('key_signature', key = mel_key))
t.append(MetaMessage('set_tempo', tempo = mel_tempo))
t.append(MetaMessage('end_of_track', time = 0))




# 3. Track 1 (Violin)
t = MidiTrack()
mel.tracks.append(t)
t.append(Message('program_change', program = 49, time = 0))
for i in range(0, len_notes, spb):
    chord = [0] * 12
    mark = 0
    while mark <= spb and i + mark < len_notes:
        chord[notes[i + mark] % 12] += 1
        mark = mark + 1
    bar.append(findchord())
    #print(mark_bar, '---', bar[mark_bar])
    appendchordv1(bar[mark_bar])
    mark_bar += 1
#
#print(bar)
t.append(MetaMessage('end_of_track'))
'''
    t.append(Message('note_on', note = notes[i], velocity = 64, time = 0))
    t.append(Message('note_on', note = notes[i], velocity = 0, time = half))
'''

# 4. Track 2 (Guitar)
t = MidiTrack()
mel.tracks.append(t)
t.append(Message('program_change', program = 25, time = 0))
for i in range(mark_bar):
    appendchordg(bar[i])

# 5. Track 3 (Violin)
t = MidiTrack()
mel.tracks.append(t)
t.append(Message('program_change', program = 49, time = 0))
for i in range(mark_bar):
    appendchordv2(bar[i])

# IV. OUTPUT HARMONY

mel.save(filename + '(harmony version).mid')

import os
import sys
import time
if( sys.platform  == 'win32' ):
    toname = '\\\\.\\pipe\\ToSrvPipe'
    fromname = '\\\\.\\pipe\\FromSrvPipe'
    EOL = '\r\n\0'

print( "Write to  \"" + toname +"\"" )
#if not os.path.exists( toname ) :
   #sys.exit();
    
print( "Read from \"" + fromname +"\"")
#if not os.path.exists( fromname ) :
#   sys.exit();

tofile = open( toname, 'wt+' )
fromfile = open( fromname, 'rt')
print( "done" )

#%%

def sendCommand( command ) :
    print( "Send: >>> "+command )
    tofile.write( command + EOL )	
    tofile.flush()

def getResponse() :
    result = ''
    line = ''
    while line != '\n' :
        result += line
        line = fromfile.readline()
	#print(" I read line:["+line+"]")
    return result

def doCommand( command ) :
    sendCommand( command )
    response = getResponse()
    print( "Rcvd: <<< " + response )
    return response

def do( command ) :
    doCommand( command )
    

def SelectAmongTracks():
    do("CollapseAllTracks:")
    buffer="0"
    while True:
            inputplayer=str(input("Play sample 0 to 5:\n{0,1,2,3,4,5}\nQuit:\n{close}\nSave latest played sample:\n{save}\nInput:\n"))
            do("Select: Track="+buffer)
            do("SelTrackStartToEnd:")
            do("SetTrackAudio: Solo=0")
            if inputplayer in ["0","1","2","3","4","5"]:
                buffer=inputplayer
                do("Select: Track="+inputplayer)
                do("SelectTracks: Track="+inputplayer+" Mode=Set")
                do("SetTrackStatus: Selected=1 Focused=1")
                do("SelTrackStartToEnd:")
                do("SetTrackAudio: Solo=1")
                do("PlayStopSelect:")
            elif inputplayer=="close":
                break
            elif inputplayer=="save":
                do("SelectTracks: Track="+buffer+" Mode=Set")
                do("Toggle:")                
                do("SetTrackStatus: Selected=1 Focused=1")                
                do("SelTrackStartToEnd:")
                time.sleep(0.1)
                do("TrackMoveBottom:")
                time.sleep(0.4)
                for i in range (5):
                    do("FirstTrack:")
                    time.sleep(0.2)
                    do("TrackClose:")
                break

def Amplify():
    print("Amplifying...")
    time.sleep(0.4)
    Duplicate(5)
    time.sleep(0.1)
    for k in range (1,6):
        do("Select: Track="+str(k))
        do("SelTrackStartToEnd:")
        do("Amplify: Ratio="+str(0.5+0.25*k)+" AllowClipping=1")
    time.sleep(0.5)
    SelectAmongTracks()
                
    
    
def Pitch():
    print("Changing pitch...")
    time.sleep(0.4)
    Duplicate(5)
    time.sleep(0.1)
    for k in range (1,6):
        do("Select: Track="+str(k))
        do("SelTrackStartToEnd:")
        do("ChangePitch: Percentage="+str(-30+15*k))
    time.sleep(0.5)
    SelectAmongTracks()


def Tempo():
    print("Changing Tempo")
    time.sleep(0.4)
    Duplicate(5)
    time.sleep(0.1)
    for k in range (1,6):
        do("Select: Track="+str(k))
        do("SelTrackStartToEnd:")
        do("ChangeTempo: Percentage="+str(-30+15*k))
    time.sleep(0.5)
    SelectAmongTracks()

def Wahwah():
    print("Wahwah...")
    time.sleep(0.4)
    Duplicate(5)
    time.sleep(0.1)
    for k in range (1,6):
        do("Select: Track="+str(k))
        do("SelTrackStartToEnd:")
        do("Wahwah: Freq="+str(0.7*k)+" Phase=0 Depth="+str(50+10*k)+" Resonance="+str(2+0.2*k)+" Offset="+str(20+5*k)+" Gain="+str((-6)+k))
    time.sleep(0.5)
    SelectAmongTracks()
    
def PaulStretch():
    print("Paul Stretching...")
    time.sleep(0.4)
    Duplicate(5)
    time.sleep(0.1)
    for k in range (1,6):
        do("Select: Track="+str(k))
        do("SelTrackStartToEnd:")
        do("Paulstretch: StretchFactor="+str(1+0.2*k)+" Time Resolution="+str(0.01*k))
    time.sleep(0.5)
    SelectAmongTracks()

def Echo():
    print("Echoing...")
    time.sleep(0.4)
    Duplicate(5)
    time.sleep(0.1)
    for k in range (1,6):
        do("Select: Track="+str(k))
        do("SelTrackStartToEnd:")
        do("Echo: Delay="+str(0.1*k)+" Decay="+str(0.15*k))
    time.sleep(0.5)
    SelectAmongTracks()

def Fadein():
    print("Fade in...")
    time.sleep(0.4)
    Duplicate(5)
    time.sleep(0.1)
    for k in range (1,6):
        do("Select: Track="+str(k))
        do("SelTrackStartToEnd:")
        do("Fade in:")
    time.sleep(0.5)
    SelectAmongTracks()

def Fadeout():
    print("Fade out...")
    time.sleep(0.4)
    Duplicate(5)
    time.sleep(0.1)
    for k in range (1,6):
        do("Select: Track="+str(k))
        do("SelTrackStartToEnd:")
        do("Fade out:")
    time.sleep(0.5)
    SelectAmongTracks()

def Reverb():
    print("Reverb...")
    time.sleep(0.4)
    Duplicate(5)
    time.sleep(0.1)
    for k in range (1,6):
        do("Select: Track="+str(k))
        do("SelTrackStartToEnd:")
        do("Reverb: RoomSize="+str(35+10*k)+" Delay=10 Reverberance="+str(20+13*k)+" HfDamping="+str(40+5*k))
    time.sleep(0.5)
    SelectAmongTracks()

def main(SoundFile):
    do("Import2: Filename="+sound)
    time.sleep(0.2)
    do("Select: Track=0")
    do("SelTrackStartToEnd:")
    time.sleep(0.2)
    do("PlayStopSelect:")
    ListeEffets=["amplify","pitch","tempo","wahwah","echo","fadein","fadeout","reverb","paulstretch","play"]
    SavedProject=0
    while True:
        if SavedProject==0:
            inputhello=str(input("Hello !\nType hi to start:\n"))
            inputhello=inputhello.lower().replace(" ","")
            if inputhello=="hi":
                while True:
                    input1=str(input("Apply an effect:\n{"+ ",".join(ListeEffets)+"}\nExport the sound file:\n{export}\nClose the project:\n{close}\nInput: "))
                    input1=input1.lower().replace(" ","")
                    if input1 in ListeEffets:
                        if input1=="amplify":
                            Amplify()
                            break
                        elif input1=="pitch":
                            Pitch()
                            break
                        elif input1=="tempo":
                            Tempo()
                            break
                        elif input1=="wahwah":
                            Wahwah()
                            break
                        elif input1=="echo":
                            Echo()
                            break
                        elif input1=="fadein":
                            Fadein()
                            break
                        elif input1=="fadeout":
                            Fadeout()
                            break
                        elif input1=="reverb":
                            Reverb()
                            break
                        elif input1=="paulstretch":
                            PaulStretch()
                            break
                        elif input1=="play":
                            do("Select: Track=0")
                            do("SelTrackStartToEnd:")
                            time.sleep(0.1)
                            do("PlayStopSelect:")
                                                    
                    elif input1=="export":
                        time.sleep(0.2)
                        do("Export:")
                        SavedProject=1
                        break
                    elif input1=="close":
                        SavedProject=1                        
                        break                    
    
                    else:
                        print("Effect not in library")
#            elif inputhello=="close":
#                do("Exit:")
#                break
            elif inputhello=="close":
                break
        else:
#            do("Exit:")
            break
def Duplicate(n):
    time.sleep(0.1)
    for k in range (n):
        do("Select: Track=0")
        do("SetTrackStatus: Selected=1 Focused=1")
        do("SelTrackStartToEnd:")
        do("Duplicate:")
    




os.chdir("C:\\Users\\max\\Desktop\\3_sisters_music")
#sound="C:\\Users\\max\\Desktop\\3_sisters_music\\Violin_2_FLAC2.flac"
#sound="C:\\Users\\max\\Desktop\\API_gun.wav"
sound="C:\\Users\\max\\Desktop\\WhitneyHoustonAPI.wav"
#sound="C:\\Users\\max\\Desktop\\SpartaAPI.wav"

main(sound)
#%%
'''author : Prabhat
   B.Tech (CSE) Hons.
   Graphic Era University'''
   
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog
from pygame import mixer 
from mutagen.mp3 import MP3
from datetime import timedelta
from time import sleep

paused = False
muted = False
i=-1
mixer.init()
volume=0.5
def  playnext():
    global i,x,ProgressbarSlide,FileLabel
    i=i+1
    if i==len(x):i=0
    mixer.music.stop()
    mixer.music.load(x[i])
    FileLabel.configure(textvariable=StringVar(root,x[i]))
    mixer.music.set_volume(volume)
    ProgressbarSlide['maximum']=int(MP3(x[i]).info.length)
    mixer.music.play()

def  playprev():
    global i,x,ProgressbarSlide
    i=i-1
    if i<0:i=len(x)-1
    mixer.music.stop()
    mixer.music.load(x[i])
    FileLabel['textvariable']=StringVar(root,x[i])
    mixer.music.set_volume(volume)
    ProgressbarSlide['maximum']=int(MP3(x[i]).info.length)  
    mixer.music.play()

def playpause():
    global pbutton
    global paused
    if paused==False :
        mixer.music.pause()
        pbutton['text']="play"
        paused=True
    else :
        mixer.music.unpause()
        pbutton['text']='pause'
        paused=False

def volume_up():
    global volume,VolumebarSlide,VolumebarSlide,muteun,muted
    muted=False
    muteun['text']='mute'
    if volume<1:volume+=.05
    volume=round(volume,2)
    mixer.music.set_volume(volume)
    VolumebarLabel['text']=f'{int(volume*100)}%'
    VolumebarSlide['value']=volume


def volume_down():
    global volume,VolumebarSlide,VolumebarSlide,muteun,muted
    muted=False
    muteun['text']='mute'
    if volume>0:volume-=.05
    volume=round(volume,2)
    mixer.music.set_volume(volume)
    VolumebarLabel['text']=f'{int(volume*100)}%'
    VolumebarSlide['value']=volume

def muteunmute():
    global muteun,muted
    if muted == False:
        mixer.music.set_volume(0)
        muteun['text']='unmute'
        muted = True
    else:
        mixer.music.set_volume(volume)
        muteun['text']='mute'
        muted = False


def updatepb():
    try:
        global ProgressbarSlide,ProgressbarEt,ProgressbarSt
        sec=mixer.music.get_pos()//1000
        ProgressbarSlide['value']=sec
        ProgressbarEt['text']=f'{timedelta(seconds=int(MP3(x[i]).info.length))}'
        ProgressbarSt['text']=f'{timedelta(seconds=int(sec))}'
    except Exception:
        pass


root = Tk()
root.title('Music Player')
root.iconphoto(False,PhotoImage(file='icon.png'))
root.geometry("1000x233+100+100")
root.resizable(False,False)

# pause-play button
pbutton = Button(root,text="pause",width=15,command=playpause,state=DISABLED)
pbutton.place(x=70,y=130)

# filename & playlist extension container
Label(root,text="File Name :").place(x=50,y=8)


Button(root,text='add music',width=15,command=lambda : x.extend(filedialog.askopenfilename(parent=root,title='Select music file',filetypes=[("Audio Files","*.mp3")],multiple=True))).place(x=780,y=8)

#stop button
Button(root,text="stop",width=15,command=root.destroy).place(x=310,y=93)

# next button
nexts = Button(root,text="next",width=15,command=playnext,state=DISABLED)
nexts.place(x=550,y=55)

# mute unmute button
muteun=Button(root,text='mute',width=15,command=muteunmute)
muteun.place(x=550,y=130)

# previous button
prevs = Button(root,text="previous",width=15,command=playprev,state=DISABLED)
prevs.place(x=70,y=55)

#volume buttons
Button(root,text='volume +',width=15,command=volume_up).place(x=750,y=75)
Button(root,text='volume -',width=15,command=volume_down).place(x=750,y=115)

# Progressbar Setup
ProgressbarContainer=Label(root,bg='pale turquoise')
ProgressbarContainer.place(x=50,y=190)
ProgressbarSlide=Progressbar(ProgressbarContainer,length=825)
ProgressbarSlide.grid(row=0,column=1)
ProgressbarEt=Label(ProgressbarContainer)
ProgressbarEt.grid(row=0,column=2)
ProgressbarSt=Label(ProgressbarContainer)
ProgressbarSt.grid(row=0,column=0)

# Volume Bar setup
VolumebarSlide=Progressbar(root,length=100,orient=VERTICAL,value=volume,maximum=1.0)
VolumebarSlide.place(x=935,y=55)
VolumebarLabel=Label(root,text=f'{int(volume*100)}%',font=('Agency FB',9),width=4)
VolumebarLabel.place(x=935,y=155)

x=list()
FileLabel=Entry(root,bg='cyan',width = 100,state=DISABLED,justify=CENTER)
FileLabel.place(x=127,y=10)
while True:    
    updatepb()

    if  mixer.music.get_busy()==True:
        pass
    elif len(x)>0:
        nexts['state']=ACTIVE
        prevs['state']=ACTIVE
        pbutton['state']=ACTIVE
        playnext()
    try:
        root.update_idletasks()
        root.update()
    except Exception:
        quit()
        pass

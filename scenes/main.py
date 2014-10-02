
import bge
from bge import render, logic

import aud

def activate_mouse():
	cont = logic.getCurrentController()
	own = cont.owner
	mPosi = cont.sensors['MousePosi']

	if own['init']:
	    render.setMousePosition( render.getWindowWidth() // 2, render.getWindowHeight() // 2 )
	    own['init'] = 0
	    
	### move cursor to mouse position
	own.localPosition = mPosi.raySource

def init_audio():
	device = aud.device()
	bge.logic.globalDict['sound'] = aud.Factory( bge.logic.expandPath("//../audios/") + 'bg-music-intro.mp3' )
	bge.handle = device.play( bge.logic.globalDict['sound'] )

def stop_audio():
	bge.handle.stop()

def init_intro_scene():
	init_audio()

def init_game_scene():
	stop_audio()



import bge

from mathutils import Vector

indicatorPosition = None

def initialize( menu ):
	print( "Initializing..." )
	global indicatorPosition
	indicatorPosition = Vector((-3.1266, 0.8124, 0.0000))
	menu['initialized'] = True

def keyboardHandler():
	global indicatorPosition
	
	currentScene = bge.logic.getCurrentScene()

	if not currentScene.objects['MENU_SRT']['initialized']:
		initialize( currentScene.objects['MENU_SRT'] )

	currentController = bge.logic.getCurrentController()
	sensor = currentController.sensors['keyboardSensor']

	#menuOpciones = currentScene.objects['MENU_OPCIONES']
	menuIndicador = currentScene.objects['MENU_INDICADOR']

	for key, status in sensor.events:
		if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
			if key == bge.events.UPARROWKEY:
				menuIndicador.position += Vector((0,0,0.2)) 
			if key == bge.events.DOWNARROWKEY:
				menuIndicador.position -= Vector((0,0,0.2)) 
				# menuOpciones.meshes[0].materials = [ 'M_BLANCO' ]
			if key in [  bge.events.ENTERKEY, bge.events.RIGHTARROWKEY ]:
				print('Activate Right!')


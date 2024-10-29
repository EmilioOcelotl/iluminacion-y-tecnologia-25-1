# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
    state = int(op('limit1')[0])  # 1 o 0
    red = int(op('rChannel')[0])  # Canal con el valor de rojo
    green = int(op('gChannel')[0])  # Canal con el valor de verde
    blue = int(op('bChannel')[0])  # Canal con el valor de azul   
    # Crear el mensaje en el formato correcto

    op('serial1').send(str(state) +','+str(red)+','+str(green)+','+str(blue)+'\n')

    return
	
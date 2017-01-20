import GPIO24 as G
import sys
#main program
pin = G.GpioForLights(sys.argv[1],1)


pin.off()
pin.clean()


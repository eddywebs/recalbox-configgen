#!/usr/bin/env python
import Command
import recalboxFiles
from generators.Generator import Generator
import os.path


class ScummVMGenerator(Generator):
    # Main entry of the module
    # Configure mupen and return a command
    def generate(self, system, rom, playersControllers):
        # Settings recalbox default config file if no user defined one
        if not system.config['configfile']:
            # Using recalbox config file
            #system.config['configfile'] = recalboxFiles.mupenCustom
            pass
        
        # Find rom path
        romPath = os.path.dirname(rom)
        romName = os.path.splitext(os.path.basename(rom))[0]
        # Get rom name without extension
        print romPath
        print romName
        commandArray = ["scummvm", 
			"--joystick=0", 
			"--screenshotspath="+recalboxFiles.screenshotsDir, 
			"--extrapath=/usr/share/scummvm",
			"--savepath="+recalboxFiles.savesDir+"scummvm",
			"--path=""{}""".format(romPath),
			"""{}""".format(romName)]
			
        return Command.Command(videomode='default', array=commandArray, env={"SDL_VIDEO_GL_DRIVER":"/usr/lib/libGLESv2.so"})

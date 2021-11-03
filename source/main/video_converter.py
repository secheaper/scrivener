from re import sub
import subprocess

class video_converter():

    def convert_video(self, input, output):
        try:
            command = 'ffmpg -i' + input + ' ' + output
            subprocess.run(command)
        except:
            print("Some Exception")
    

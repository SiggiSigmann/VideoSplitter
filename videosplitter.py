import cv2      #used for video handling
import os       #used for check and crate folder
import sys      #used for progressbar

videoInPath = "./tobi.mp4"
pictureOutPath = "./data1"
maxNumberOfImages = 100
progressBarLen = 40

def progressBar(current, total, comment=''):
    progress = int(round(progressBarLen * current / float(total)))

    percents = round(100.0 * current / float(total), 1)
    fillerString = '=' * progress + '-' * (progressBarLen - progress)

    sys.stdout.write('[%s] %s%% %s\r' % (fillerString, percents, comment))
    sys.stdout.flush()

if  os.path.exists(videoInPath):
    cam = cv2.VideoCapture(videoInPath)
    print("Open: " + videoInPath)
else:
    print("Video don't exists")
    exit(1)

length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))     #get amount of frames
setSkipper= int(length/maxNumberOfImages)
setSkipper+=1                                       # every setSkipper frame will be used

print(length," frames in total.")
print("Use ever " + str(setSkipper) + "frame.")

try: 
    if not os.path.exists(pictureOutPath):          #check if dir already exists
        os.makedirs(pictureOutPath) 

except OSError:                                     # if not created then raise error 
    print ('Error: Creating directory of data') 
  

currentframe = 0
skipper=0

#process Video
while(True): 
    exits,frame = cam.read()  # reading from frame 
  
    if skipper >= setSkipper:
        if exits: 
            # if video is still left continue creating images 
            name = pictureOutPath+'/frame' + str(currentframe) + '.jpg' 
            cv2.imwrite(name, frame) 
            currentframe += 1
            skipper = 0
            progressBar(currentframe,maxNumberOfImages, "create: frame"+str(currentframe-1)+".jpg")
        else: 
            break
    skipper +=1
    
arprogressBar(maxNumberOfImages,maxNumberOfImages,"create: frame"+str(currentframe-1)+".jpg")
print()

# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows()

print("finished")
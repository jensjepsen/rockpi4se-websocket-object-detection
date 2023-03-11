import asyncio
import base64
import websockets
import cv2
import time

# define a video capture object
vid = cv2.VideoCapture(0)

async def echo(websocket):
    
    while True:
        ret, frame = vid.read()
        frame = cv2.resize(frame, dsize=(800, 600))
        _, buff = cv2.imencode('.png', frame)
        message = base64.b64encode(buff).decode()
        await websocket.send(message)
        #await asyncio.sleep(0.05)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())



"""
while(True):
    
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    #breakpoint()
    # Display the resulting frame
    cv2.imshow('frame', frame)
    encoded = _, buff = cv2.imencode('.png', frame)
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

"""

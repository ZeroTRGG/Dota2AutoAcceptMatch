import cv2
from vidgear.gears import ScreenGear
import numpy as np
import pyautogui

lower_green = (88, 109, 67)
upper_green = (90, 111, 69)

lower_orange = (22, 63, 96)
upper_orange = (73, 197, 212)


stream = ScreenGear()

# Start the screen capture
stream.start()


while True:
    frame = stream.read()

    if frame is None:
        break

    # Convert the frame to the HSV color spaceq
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask2 = cv2.inRange(hsv, lower_orange, upper_orange)

    # Create a mask to isolate the green color
    green_pixels = cv2.findNonZero(mask)
    orange_pixels = cv2.findNonZero(mask2)


    
    if green_pixels is not None:
        for pixel in green_pixels:
            x, y = pixel[0]
            print(f"Green pixel found at coordinates (x={x}, y={y})")
            # Calculate the middle coordinates
            middle_x = 960
            middle_y = 540
            # Simulate a click in the middle
            # Note: You may need to adjust the delay and the number of clicks as needed
            pyautogui.click(middle_x, middle_y, clicks=1, interval=2)
            if orange_pixels is not None:
                print("script finish")
                break
        break

    prev_frame = mask.copy()  # Store the current frame for comparison

    # Display the frame with green pixels highlighted
    cv2.imshow("Screen Capture with Green Pixels", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
stream.stop()
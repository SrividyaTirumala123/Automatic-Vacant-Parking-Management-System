import cv2
import os

# Path to your video file
video_path = 'carPark.mp4'  # Make sure this file is in the same folder as your script
output_folder = 'frames'    # Folder where extracted frames will be saved

# Create folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the video
cap = cv2.VideoCapture(video_path)
frame_num = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    # Save each frame as image
    frame_filename = os.path.join(output_folder, f'frame{frame_num:03}.jpg')
    cv2.imwrite(frame_filename, frame)
    frame_num += 1

cap.release()
print(f"✅ Extracted {frame_num} frames into '{output_folder}' folder.")

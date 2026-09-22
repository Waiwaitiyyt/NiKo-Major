import cv2 
import os
from pathlib import Path

video_path = r"./niko_clip.mp4"
cap = cv2.VideoCapture(video_path)
save_path = r"./niko_frames/"

frame_count = 0


while frame_count <= 1:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imwrite(save_path + rf"frame_{frame_count}.png", frame)
    frame_count += 1

print("finished")
    
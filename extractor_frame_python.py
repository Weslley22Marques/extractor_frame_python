import cv2
from PIL import Image

video = "C:/Users/WESLLEY/Downloads/zve10.2849.MP4"
image_frame = "C:/Users/WESLLEY/Downloads/segundo_frame.png"

cap = cv2.VideoCapture(video)

if not cap.isOpened():
    print("Não deu pra abrir")
else:
    cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
    success, frame = cap.read()

    if success:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame_rgb)
        image.save(output_image_path)
        print(f"Segundo frame salvo com sucesso - {image_frame}")
    else:
        print("Não foi possível.")

cap.release()
import argparse
from deepface import DeepFace

if __name__ == "__main__":
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--image", required = True, help = "Path to input image")
  args = vars(ap.parse_args())

  img_path = args["image"]

  face_analysis = DeepFace.analyze(img_path = img_path)

  print ("gender:", face_analysis["gender"])
  print ("age:", face_analysis["age"])
  print ("dominant_race:", face_analysis["dominant_race"])
  print ("dominant_emotion", face_analysis["dominant_emotion"])
  print (face_analysis)

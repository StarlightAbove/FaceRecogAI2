import cv2
# to edit
def detect_face(img_path):
# Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_cascade_2 = cv2.CascadeClassifier('secondary_recog.xml')
    face_cascade_3 = cv2.CascadeClassifier('tertiary_recog.xml')
    # Read the input image
    img = cv2.imread(img_path)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    faces2 = face_cascade_2.detectMultiScale(gray, 1.2, 4)
    faces3 = face_cascade_3.detectMultiScale(gray, 1.2, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)
    for (x, y, w, h) in faces2:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)
    for (x, y, w, h) in faces3:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)
    # Display the output
    cv2.imshow('Processed Image', img)
    cv2.imwrite('processed_img.png',img)
    cv2.waitKey()

def face_block(img_path):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_cascade_2 = cv2.CascadeClassifier('secondary_recog.xml')
    face_cascade_3 = cv2.CascadeClassifier('tertiary_recog.xml')
    # Read the input image
    img = cv2.imread(img_path)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    faces2 = face_cascade_2.detectMultiScale(gray, 1.2, 4)
    faces3 = face_cascade_3.detectMultiScale(gray, 1.2, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), -1)
    for (x, y, w, h) in faces2:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), -1)
    for (x, y, w, h) in faces3:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), -1)
    # Display the output
    cv2.imshow('Processed Image', img)
    cv2.imwrite('processed_img.png',img)
    cv2.waitKey()

def face_blur(img_path):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_cascade_2 = cv2.CascadeClassifier('secondary_recog.xml')
    face_cascade_3 = cv2.CascadeClassifier('tertiary_recog.xml')
    # Read the input image
    img = cv2.imread(img_path)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    faces2 = face_cascade_2.detectMultiScale(gray, 1.2, 4)
    faces3 = face_cascade_3.detectMultiScale(gray, 1.2, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:     
        face = img[x:x+w, y:y+h]
        face = cv2.GaussianBlur(face,(23,23), 30)
        img[y:y+face.shape[0], x:x+face.shape[1]] = face
    for (x, y, w, h) in faces2:     
        face = img[x:x+w, y:y+h]
        face = cv2.GaussianBlur(face,(23,23), 30)
        img[y:y+face.shape[0], x:x+face.shape[1]] = face
    for (x, y, w, h) in faces3:
        face = img[x:x+w, y:y+h]
        face = cv2.GaussianBlur(face,(23,23), 30)
        img[y:y+face.shape[0], x:x+face.shape[1]] = face
    # Display the output
    cv2.imshow('Processed Image', img)
    cv2.imwrite('processed_img.png',img)
    cv2.waitKey()

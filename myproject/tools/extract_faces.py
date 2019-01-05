import sys
import os
import cv2
import glob

try:
    cascade_path = sys.argv[1]
except IndexError:
    print('顔検出用の、特徴量ファイルのパスを、引数にセットする必要がある', file=sys.stderr)
    exit(1)

output_dir = 'outdir'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
assert os.path.exists(cascade_path)

classifier = cv2.CascadeClassifier(cascade_path)
for image_path in glob.glob(sys.argv[2:][0]):
    print('Processing', image_path, file=sys.stderr)

    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray_image)

    image_name = os.path.splitext(os.path.basename(image_path))[0]

    for i, (x, y, w, h) in enumerate(faces):
        face_image = image[y:y + h, x:x + w]
        output_path = os.path.join(output_dir, '{0}_{1}.jpg'.format(image_name, i))
        cv2.imwrite(output_path, face_image)
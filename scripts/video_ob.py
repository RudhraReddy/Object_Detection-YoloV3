import numpy as np
import cv2
import random
from imutils.video import FPS
from imutils.video import VideoStream


def vid_obj_dection(image1, op):

    n = random.randint(1, 10)
    OUTPUT_FILE = f'./outputs/videos/video_output_{n}.avi'

    H = None
    W = None

    fps = FPS().start()

    fourcc = cv2.VideoWriter_fourcc(*"MJPG")

    LABELS = open('./confg/coco.names').read().strip().split("\n")

    np.random.seed(4)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

    net = cv2.dnn.readNet('./confg/yolov3.weights', './confg/yolov3.cfg')

    vs = cv2.VideoCapture(image1)
    op_h = 1200
    op_w = 800

    if op:
        writer = cv2.VideoWriter(OUTPUT_FILE, fourcc, 30, (1200, 800), True)

    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    cnt = 0
    while True:
        cnt += 1
        try:
            (grabbed, image) = vs.read()
        except:
            break
        blob = cv2.dnn.blobFromImage(
            image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        if W is None or H is None:
            (H, W) = image.shape[:2]

        layerOutputs = net.forward(ln)

        # initialize our lists of detected bounding boxes, confidences, and
        # class IDs, respectively
        boxes = []
        confidences = []
        classIDs = []

        # loop over each of the layer outputs
        for output in layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability) of
                # the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                # filter out weak predictions by ensuring the detected
                # probability is greater than the minimum probability
                if confidence > 0.7:
                    # scale the bounding box coordinates back relative to the
                    # size of the image, keeping in mind that YOLO actually
                    # returns the center (x, y)-coordinates of the bounding
                    # box followed by the boxes' width and height
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")

                    # use the center (x, y)-coordinates to derive the top and
                    # and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    # update our list of bounding box coordinates, confidences,
                    # and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        # apply non-maxima suppression to suppress weak, overlapping bounding
        # boxes
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.7, 0.7)

        # ensure at least one detection exists
        if len(idxs) > 0:
            # loop over the indexes we are keeping
            for i in idxs.flatten():
                # extract the bounding box coordinates
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])

                color = [int(c) for c in COLORS[classIDs[i]]]

                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
                cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, color, 2)

        # show the output image
        cv2.imshow("output", cv2.resize(image, (op_h, op_w)))
        if op:
            writer.write(cv2.resize(image, (op_h, op_w)))
        fps.update()
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    fps.stop()

    # do a bit of cleanup
    cv2.destroyAllWindows()

    # release the file pointers
    writer.release()
    vs.release()

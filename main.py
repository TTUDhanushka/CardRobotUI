#!/usr/env/bin python3

import cv2


def main():
    cap = cv2.VideoCapture(0, cv2.CAP_ANY)

    while cap.isOpened():
        ret, cv_image = cap.read()

        cv2.imshow('Out', cv_image)

        cv2.waitKey(30)
        

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

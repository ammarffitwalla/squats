import datetime

import pickle
import time
import numpy
import cv2
# import face_recognition
# import imutils
import requests
# from bottle import Response, response
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators import gzip
import json
import datetime

# from win32com.test.testPersist import now
from ipcamapp.csv_writer import csv_writer_func

process_start = False
filename = 'faces.jpg'
video_file_name = ''
curr_mod = 'demo'
video_file = 0
start_counter = 10
process_stand = False
countdown_started = False
process_finish = False
raise_hand = True
total_time_remaining = 0
total_time = 50
total_squat = 0
start_ymin = 0
end_ymin = 0
list_miny = []
xMid = 10
yMid = 10


# def detect_objects(filename):
#     POWER_AI_VISION_API_URL = "https://195.229.90.114/powerai-vision/api/dlapis/d7e44755-d781-4588-bb9c-91e81708f649"
#     # with open(filename, 'rb') as f:
#     #     # WARNING! verify=False is here to allow an untrusted cert!
#     #     r = s.post(POWER_AI_VISION_API_URL,
#     #                files={'files': (filename, f)},
#     #                verify=False)
#     #
#     # return r.status_code, json.loads(r.text)
#     rc1 = 0
#     resp_value = None
#
#     retry_count = 0
#     while (rc1 != 200) and (retry_count < 5):
#         # print("retry_count=%d" % retry_count)
#         if retry_cocunt != 0:
#             print("retrying upload for  attempt %d" % retry_count)
#
#         # r = requests.post(endpoint, files=myfiles, verify=False)
#         # rc = r.status_code
#         with open(filename, 'rb') as f:
#             try:
#                 r = s.post(POWER_AI_VISION_API_URL,
#                               files={'files': (filename, f)},
#                               verify=False, timeout=10)
#                 rc1 = r.status_code
#                 # print("status code = %d " %rc1)
#             except Exception as exc:
#                 print('generated an exception: %s' % exc)
#                 rc1 = 0
#                 retry_count = retry_count + 1
#                 continue
#             # WARNING! verify=False is here to allow an untrusted cert!
#
#         retry_count = retry_count + 1
#         resp_value = json.loads(r.text)
#     # finally:
#     # lock.release()  # release lock, no matter what
#     if r != None:
#         rc1 = r.status_code
#     else:
#         rc1 = 409
#     # rs_value = ''
#     # if resp_value.get(' != None:
#     #     rs_value = resp_value['classified']
#     # print(rc)
#     return rc1, resp_value


def do_something(image):
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    global process_start
    global countdown_started
    global start_counter
    global total_time_remaining
    global xMid, yMid
    global raise_hand
    # global total_squat
    requests.packages.urllib3.disable_warnings()
    # now = datetime.now()
    # dt_string = now.strftime("%d%m%Y_%H%M%S")
    # print("date and time =", dt_string)
    from random import randint
    file_name = "Test" + str(randint(0, 5)) + ".jpg"
    cv2.imwrite(file_name, image)
    if raise_hand == True:
        cv2.putText(image, "Please raise your hand above head", (50, 60), fontface, 1, (255, 0, 0), 1, cv2.LINE_AA)
    # coke
    # api_url = "https://195.229.90.114/powerai-vision/api/dlapis/84870dd3-7fa8-49ef-98de-3b0e8ee11ae1"
    # solar
    # api_url = "https://195.229.90.114/powerai-vision/api/dlapis/d3ef4bc8-3f46-4e88-a36d-28702ec761c6"
    # xray
    # api_url = "https://195.229.90.114/powerai-vision/api/dlapis/72750b26-e20b-425e-a979-d4eb25253214"
    # driving lane
    # api_url = "https://10.150.20.61/powerai-vision/api/dlapis/8952d6d4-af97-4fb7-9ce7-4ebfa52787e4"
    # api_url = "https://10.150.20.61/powerai-vision/api/dlapis/e9b61ba4-bf7e-47b5-88a2-282ba1323871"
    # api person polygon
    # api_url = "https://195.229.90.114/powerai-vision/api/dlapis/e1a8f988-d46a-434c-995f-1846af346558"
    # _grab_data(stream=request.get["api_url"])
    # # received_json_data = json.loads(request.body.decode("utf-8"))
    # print(received_json_data)
    # api_url = "https://195.229.90.114/powerai-vision/api/dlapis/f779fa1e-5b55-4d74-ae05-368309ed8af5"
    # api_url = "https://195.229.90.114/powerai-vision/api/dlapis/c6f875eb-ccc7-4bf4-a098-98c38171b3d8"  # Face and Hand Scott IBM Summit
    # api_url_person = "https://195.229.90.114/powerai-vision/api/dlapis/9cb838e7-1297-40b3-948a-69162668b239"  #Person IBM SUMMit
    # api_url_hands = "https://195.229.90.114/powerai-vision/api/dlapis/ddc170e9-370d-458e-ac5c-c9b04fb7c2bb" # Hands

    # api_url = "https://10.150.20.61/powerai-vision/api/dlapis/0495da4d-bfa1-494c-9f06-190564e43d1e"  # Face and Hand Scott IBM Summit
    api_url = "https://195.229.90.114/powerai-vision/api/dlapis/e5ba4636-8790-4e44-aa2c-1eebcd4f71b9"

    # api_url_head = "https://10.150.20.61/powerai-vision/api/dlapis/0495da4d-bfa1-494c-9f06-190564e43d1e"  # Person IBM SUMMit
    api_url_head = "https://195.229.90.114/powerai-vision/api/dlapis/e5ba4636-8790-4e44-aa2c-1eebcd4f71b9"

    # api_url_hands = "https://10.150.20.61/powerai-vision/api/dlapis/4fc722ad-e972-4dcb-8528-db85c618840a"  # Hands
    api_url_hands = "https://195.229.90.114/powerai-vision/api/dlapis/af4ecf18-9958-4365-b763-811fb77c1022"

    # print(api_url)

    # print()
    # print(testdata)
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    hminX = 0
    hminY = 0
    minX = 0
    minY = 0
    rc1 = 0
    rc11 = 0
    # hmaxX = 0
    # hmaxY = 0
    if process_start == False:
        retry_count = 0
        while (rc1 != 200) and (retry_count < 5):
            # print("retry_count=%d" % retry_count)
            if retry_count != 0:
                print("retrying upload for  attempt %d" % retry_count)

            # r = requests.post(endpoint, files=myfiles, verify=False)
            # rc = r.status_code
            try:
                with open(file_name, 'rb') as f:
                    s = requests.Session()
                    r = s.post(api_url, files={'files': (file_name, f)}, verify=False, timeout=10)
                    # print(r.status_code)
                    # print(r.text)

                rc1 = r.status_code
                # print("status code = %d " %rc1)
            except Exception as exc:
                print('generated an exception: %s' % exc)
                rc1 = 0
                retry_count = retry_count + 1
                continue
                # import os

        if retry_count == 5:
            cv2.putText(image, "N/W connectivity lost", (xMid - 200, yMid), fontface, 1, (0, 255, 255), 2, cv2.LINE_AA)
            # cv2.putText(image, "countdown begin in", (xMid - 270, yMid), fontface, 1.8, (0, 255, 255), 2, cv2.LINE_AA)
            # cv2.putText(image, str(start_counter), (xMid - 30, yMid + 50), fontface, 2, (0, 255, 255), 2, cv2.LINE_AA)
            # cv2.putText(image, "Congratulations", (xMid-250, yMid), fontface, 2, (0, 255, 255), 2, cv2.LINE_AA)
            # cv2.putText(image, "Total Squats: " + str(total_squat), (xMid-310, 100), fontface, 1, (0, 255, 255), 1, cv2.LINE_AA)
            # cv2.putText(image, "Keep trying you are the best", (xMid - 270, yMid), fontface, 1.2, (0, 255, 255), 2, cv2.LINE_AA)
            return image

        if r.text != None:
            data = json.loads(r.text)
            # print(data)
        if data['result'] != 'fail':
            print('data is calling::::')
            print(data)
            testdata = data["classified"]

            for counter in range((len(testdata))):
                # print(counter)
                # if counter == 0:
                if testdata[counter].get('label') == 'face':
                    minX = int(testdata[counter].get('xmin'))  # (x1,y1,x2,y2)
                    minY = int(testdata[counter].get('ymin'))
                    maxX = int(testdata[counter].get('xmax'))
                    maxY = int(testdata[counter].get('ymax'))
                    cv2.rectangle(image, (minX, minY), (maxX, maxY), (0, 255, 0), 2)

            retry_count = 0
            while (rc11 != 200) and (retry_count < 5):
                # print("retry_count=%d" % retry_count)
                if retry_count != 0:
                    print("retrying upload for  attempt %d" % retry_count)

                # r = requests.post(endpoint, files=myfiles, verify=False)
                # rc = r.status_code
                try:
                    with open(file_name, 'rb') as f:
                        s = requests.Session()
                        r = s.post(api_url_hands, files={'files': (file_name, f)}, verify=False, timeout=4)
                        # print(r.status_code)
                        # print(r.text)

                    rc11 = r.status_code
                    # print("status code = %d " %rc1)
                except Exception as exc:
                    print('generated an exception: %s' % exc)
                    rc1 = 0
                    retry_count = retry_count + 1
                    continue
                    # import os
            if r.text != None:
                data = json.loads(r.text)
            else:
                data = []
                # print(data)
            testdata = data["classified"]
            for counter in range((len(testdata))):
                print('hand is called')
                # print(counter)
                # if counter == 0:
                if testdata[counter].get('label') == 'hand':
                    hminX = int(testdata[counter].get('xmin'))  # (x1,y1,x2,y2)
                    hminY = int(testdata[counter].get('ymin'))
                    hmaxX = int(testdata[counter].get('xmax'))
                    hmaxY = int(testdata[counter].get('ymax'))
                    cv2.rectangle(image, (hminX, hminY), (hmaxX, hmaxY), (0, 255, 0), 2)

            if minX > hminX and minY > hminY and minX > 0 and minY > 0 and hminX > 0 and hminY > 0:
                # print("hand is above head")
                raise_hand = False
                cv2.putText(image, "Hand is above head", (minX, minY), fontface, 1, (0, 255, 255), 1, cv2.LINE_AA)
                cv2.rectangle(image, (minX, minY), (maxX, maxY), (0, 255, 0), 2)
                cv2.rectangle(image, (hminX, hminY), (hmaxX, hmaxY), (0, 255, 0), 2)
                process_start = True
    else:
        cv2.putText(image, "countdown begin in", (xMid - 270, yMid), fontface, 1.8, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, str(start_counter), (xMid - 30, yMid + 50), fontface, 2, (0, 255, 255), 2, cv2.LINE_AA)
        # cv2.putText(image, "countdown begin in", (xMid, yMid), fontface, 2, (0, 255, 255), 2, cv2.LINE_AA)
        # cv2.putText(image, str(start_counter), (xMid, yMid+50), fontface, 2, (0, 255, 255), 2, cv2.LINE_AA)
        if start_counter > 0:
            import time
            time.sleep(1)
            start_counter = start_counter - 1
            print("count down will start" + str(start_counter))
        if start_counter == 0:
            countdown_started = True
            # with open(file_name, 'rb') as f:
            #     s = requests.Session()
            #     rs = s.post(api_url_person, files={'files': (file_name, f)}, verify=False, timeout=10)
            #     # print(rs.status_code)
            #     # print(r.text)

            retry_count = 0
            while (rc1 != 200) and (retry_count < 5):
                # print("retry_count=%d" % retry_count)
                if retry_count != 0:
                    print("retrying upload for  attempt %d" % retry_count)

                # r = requests.post(endpoint, files=myfiles, verify=False)
                # rc = r.status_code

                try:
                    with open(file_name, 'rb') as f:
                        s = requests.Session()
                        rs = s.post(api_url_head, files={'files': (file_name, f)}, verify=False, timeout=4)
                        # print(r.status_code)
                        # print(r.text)

                    rc1 = rs.status_code
                    # print("status code = %d " %rc1)
                except Exception as exc:
                    print('generated an exception: %s' % exc)
                    rc1 = 0
                    retry_count = retry_count + 1
                    continue
                    # import os
            if rs.text != None:
                data_person = json.loads(rs.text)
            else:
                data_person = []

            # import os
            test_person = data_person["classified"]

            for counter in range((len(test_person))):
                # print(counter)
                # if counter == 0:
                if test_person[counter].get('label') == 'person':
                    minX = int(test_person[counter].get('xmin'))  # (x1,y1,x2,y2)
                    minY = int(test_person[counter].get('ymin'))
                    maxX = int(test_person[counter].get('xmax'))
                    maxY = int(test_person[counter].get('ymax'))
                    cv2.rectangle(image, (minX, minY), (maxX, maxY), (0, 255, 0), 2)
                    print("person")
                    print(minX, minY, maxX, maxY)

            counter = 0
    return image


# def make_rectangle(frame):
#     print("Start")
#
#     # with open('encodings.pickle', 'rb') as f:
#     #     contents = f.read()
#     # data = pickle.loads(contents)
#     # print(data)
#     rcl, response_value = detect_objects(frame)
#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     rgb = imutils.resize(frame, width=750)
#     r = frame.shape[1] / float(rgb.shape[1])
#
#     # detect the (x, y)-coordinates of the bounding boxes
#     # corresponding to each face in the input frame, then compute
#     # the facial embeddings for each face
#     boxes = face_recognition.face_locations(rgb, model="cnn")
#     print(boxes)
#     # encodings = face_recognition.face_encodings(rgb, boxes)
#     # names = []
#     # loop over the facial embeddings
#     # for encoding in encodings:
#         # attempt to match each face in the input image to our known
#         # encodings
#         # matches = face_recognition.compare_faces(data["encodings"],
#         #                                          encoding)
#         # name = "Unknown"
#
#         # check to see if we have found a match
#         # if True in matches:
#             # find the indexes of all matched faces then initialize a
#             # dictionary to count the total number of times each face
#             # was matched
#     #         matchedIdxs = [i for (i, b) in enumerate(matches) if b]
#     #         counts = {}
#     #
#     #         # loop over the matched indexes and maintain a count for
#     #         # each recognized face face
#     #         for i in matchedIdxs:
#     #             name = data["names"][i]
#     #             counts[name] = counts.get(name, 0) + 1
#     #
#     #         # determine the recognized face with the largest number
#     #         # of votes (note: in the event of an unlikely tie Python
#     #         # will select first entry in the dictionary)
#     #         name = max(counts, key=counts.get)
#     #
#     #     # update the list of names
#     #     names.append(name)
#     #
#     # # loop over the recognized faces
#     for (top, right, bottom, left) in boxes:
#         # rescale the face coordinates
#         top = int(top * r)
#         right = int(right * r)
#         bottom = int(bottom * r)
#         left = int(left * r)
#     #
#     #     # draw the predicted face name on the image
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#     # y = top - 15 if top - 15 > 15 else top + 15
#     # cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
#     return frame


class VideoCamera(object):

    def __init__(self):
        camera_port = 0  # 'http://192.168.0.101:6677/videofeed?username=&password='
        # camera_port = 'http://192.168.1.101:8080/videofeed?username=admin&password=admin'
        # camera_port = 'rtsp://admin:admin@192.168.1.101/'
        # camera_port = 'rtsp://admin:admin@192.168.1.101/H264?ch=0&subtype=0'

        self.video = cv2.VideoCapture(camera_port)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        global countdown_started, xMid, yMid
        global process_finish
        ret, image = self.video.read()
        # image = cv2.resize(image, (480, 640))
        height, width, channel = image.shape
        print(height, width)
        xMid = width // 2
        yMid = height // 2

        if countdown_started == False:
            image = do_something(image)
        else:
            if process_finish == True:
                time.sleep(5)
                process_finish = False
            image = check_squats(image)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


# def demo(request):
#     global curr_mod
#     curr_mod = 'demo'
#     request.session['url_is_video'] = '0'
#     example_pic = filename
#     request.session['test_img'] = filename
#     return render(request, 'image_display.html', {'picture':example_pic})


# def video(request):
#     return render(request, 'video_out.html')

def check_squats(image):
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    global countdown_started, start_counter, total_time_remaining, total_squat, start_ymin, end_ymin, process_start, total_time, list_miny, process_finish, xMid, yMid, process_stand, raise_hand, start_miny_list
    requests.packages.urllib3.disable_warnings()
    if total_squat >= 5 and total_time_remaining <= total_time:
        cv2.putText(image, "Congratulations", (xMid - 250, yMid), fontface, 2, (0, 255, 255), 2, cv2.LINE_AA)
        # cv2.putText(image, "Congratulations", (xMid, yMid), fontface, 5, (0, 255, 255), 1 , cv2.LINE_AA)
        print("congrats")
        raise_hand = True
        process_finish = True
        countdown_started = False
        process_start = False
        total_squat = 0
        start_counter = 5
        total_time_remaining = 0
        list_miny = []
        start_miny_list = []
    elif total_time_remaining > total_time:
        cv2.putText(image, "Keep trying you are the best", (xMid - 270, yMid), fontface, 1.2, (0, 255, 255), 2,
                    cv2.LINE_AA)
        # cv2.putText(image, "Keep trying you are the best", (xMid + 40, yMid), fontface, 1.2, (0, 255, 255), 2, cv2.LINE_AA)
        # print("Keep trying you are the best")
        process_finish = True
        countdown_started = False
        total_squat = 0
        start_counter = 5
        process_start = False
        list_miny = []
        start_miny_list = []
        total_time_remaining = 0
    else:
        from random import randint
        file_name = "Test" + str(randint(0, 100000)) + ".jpg"
        cv2.imwrite(file_name, image)
        # api_url_person = "https://195.229.90.114/powerai-vision/api/dlapis/9cb838e7-1297-40b3-948a-69162668b239"  # Person IBM SUMMit
        # api_url_head = "https://10.150.20.61/powerai-vision/api/dlapis/0495da4d-bfa1-494c-9f06-190564e43d1e"
        api_url_head = "https://195.229.90.114/powerai-vision/api/dlapis/e5ba4636-8790-4e44-aa2c-1eebcd4f71b9"
        fontface = cv2.FONT_HERSHEY_SIMPLEX
        minY = 0
        rc1 = 0
        cv2.putText(image, "Total Squats: " + str(total_squat), (xMid - 310, 100), fontface, 1, (0, 255, 255), 1,
                    cv2.LINE_AA)
        # cv2.putText(image, "Total Squats: " + str(total_squat), (xMid, 100), fontface, 2, (0, 255, 255), 1, cv2.LINE_AA)
        retry_count = 0
        while (rc1 != 200) and (retry_count < 5):
            if retry_count != 0:
                print("retrying upload for  attempt %d" % retry_count)

            # r = requests.post(endpoint, files=myfiles, verify=False)
            # rc = r.status_code
            try:
                with open(file_name, 'rb') as f:
                    s = requests.Session()
                    rs = s.post(api_url_head, files={'files': (file_name, f)}, verify=False, timeout=4)
                    # print(r.status_code)
                    # print(r.text)

                rc1 = rs.status_code
                # print("status code = %d " %rc1)
            except Exception as exc:
                print('generated an exception: %s' % exc)
                rc1 = 0
                retry_count = retry_count + 1
                continue
                # import os
        if rs.text != None:
            data_person = json.loads(rs.text)
        else:
            data_person = []
        if data_person["result"] != "fail":
            # import os
            test_person = data_person["classified"]
            if len(test_person) > 0:
                for counter in range((len(test_person))):
                    # print(counter)
                    # if counter == 0:
                    if test_person[counter].get('label') == 'face':
                        minX = int(test_person[counter].get('xmin'))  # (x1,y1,x2,y2)
                        minY = int(test_person[counter].get('ymin'))
                        maxX = int(test_person[counter].get('xmax'))
                        maxY = int(test_person[counter].get('ymax'))
                        start_miny_list.append(minY)
                        cv2.rectangle(image, (minX, minY), (maxX, maxY), (0, 255, 0), 2)
                        print("face")
                        print(minX, minY, maxX, maxY)

                        dimensions = [minX, minY, maxX, maxY, file_name, total_squat, start_ymin, end_ymin]
                        dimensions = [dimensions]
                        csv_writer_func(dimensions)

                        list_miny.append(minY)

                # Start Of Squats Counting Logic

                if len(list_miny) > 0:
                    start_ymin = list_miny[0]
                    if minY < start_ymin + 100:
                        if process_stand:
                            if start_miny_list[0]-50 < minY < start_miny_list[0]+50:
                                total_squat += 1
                                end_ymin = 0
                                process_stand = False
                                start_ymin = 0
                                list_miny = []
                        else:
                            print("pass")
                    else:
                        if minY > end_ymin:
                            end_ymin = minY
                        else:
                            process_stand = True

                # End Of Squats counting Logic

                    # if minY > start_ymin:
                    #     # print("minY:",minY)
                    #     print("minY: ", minY, " > start_ymin: \t", start_ymin)
                    #     start_ymin = minY
                    #     print('stand(start y min):\t', start_ymin)
                    # else:
                    #     # start_ymin = list_miny[0]
                    #     print('start y min:\n', start_ymin)
                    #     if minY < start_ymin + 100:
                    #         print("minY ", minY, " < start_ymin pass ", start_ymin)
                    #     else:
                    #         print("Miny\t", minY)
                    #         print("Start Miny\t", start_ymin)
                    #         total_squat += 1
                    #         cv2.putText(image, "Total Squats: " + str(total_squat), (80, 80), fontface, 1,
                    #                     (0, 255, 255), 1, cv2.LINE_AA)
                    #         # print("squat\t", total_squat)
                    #         end_ymin = 0
                    #         start_ymin = 0
                    #         minY = 1
                    #         list_miny = []
                total_time_remaining += 1
                # time.sleep(1)
        counter = 0

    return image


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def index(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted")

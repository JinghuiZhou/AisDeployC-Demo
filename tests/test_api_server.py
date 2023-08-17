import os
import cv2
import argparse
import glob
import json
import requests
import time
import base64
import cv2

def parse_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--image_path", default="", type=str, required=True, help="image_path")
    parser.add_argument("--route", default="", type=str, required=True, help="route")
    parser.add_argument("--port", default=9003, type=int, required=False, help="port")
    parser.add_argument("--ip", default="127.0.0.1", type=str, required=False, help="str")
    args = parser.parse_args()
    return args

def work(kwargs):
    filename = kwargs.get("image_path")
    route = kwargs.get("route")
    port = kwargs.get("port")
    ip = kwargs.get("ip")

    appKey = "s84dsd#7hf34r3jsk@fs$d#$dd"
    backend_host = "http://{}:{}".format(ip, port)
    headers = {'Content-Type': 'application/json'}
    iteration_number = 1
    for _ in range(iteration_number):
        image = cv2.imread(filename)

        encoded_image_byte = cv2.imencode(".jpg", image)[1].tobytes()  # bytes类型
        image_base64 = base64.b64encode(encoded_image_byte)
        image_base64 = image_base64.decode("utf-8")  # str类型
        image_base64 = "data:image/jpeg;base64," + image_base64
        url = '{}/{}'.format(backend_host, route)

        t1 = time.time()
        params = {
            "appKey": appKey,
            "image_base64":image_base64,

        }

        res=requests.post(url, json=params, headers=headers)
        t2 = time.time()
        t = "spend %.5f 秒"%(t2 - t1)
        print("[INFO] time {} {}".format(__name__, t))
        # print(t,res.status_code,res.content)
        print("[INFO] {}\n\tstatus_code:{}\n\tcontent:{}".format(__name__, res.status_code, res.content))







def main():
    args = parse_args()
    input_kwargs = dict(
        image_path = args.image_path,
        route = args.route,
        port = args.port,
        ip = args.ip,
    )
    work(input_kwargs)

if __name__ == "__main__":
    main()

import requests
from  requests.auth import HTTPBasicAuth, HTTPDigestAuth
import json
import os
from datetime import datetime

print(f'Start: {datetime.now().time()}')

BASE_URL = "https://www.gran-turismo.com/de/api/gt7sp/"
URI = ""
form_data = {}
user_no = 2581360
#user_no = 4467637


def get_profile():
    response = requests.post(BASE_URL + f"/profile/?job=1&user_no={user_no}")
    json_output = response.json()

    return json_output


def get_gt_response(url):
    response = requests.post(url)

    if response.status_code == 200:
        json_output = response.json()
        cur_time = datetime.now().time()
        print(f'{cur_time}: Add data from {url}')
    elif response.status_code == 400:
        print(f"Answer of {url} is 400, data is not added")
        json_output = {"response": "400: page not found"}
    else:
        print(f"Data not added, recieve status code: {response.status_code}")
        json_output = {"response": f"{response.status_code}: Uups I don't know this status code!"}

    return json_output


def get_track_records(course_id, category_id, is_category) -> json:

    param_url = f'/course_record/?job=1&user_no={str(user_no)}&course_id={str(course_id)}&' \
                f'category_id={category_id}&is_category={str(is_category)}'
    response = requests.post(BASE_URL + param_url)
    if response.status_code == 200:
        json_output = response.json()
        cur_time = datetime.now().time()
        print(f'{cur_time}: Add data from {BASE_URL+param_url}')
    elif response.status_code == 400:
        print(f"Answer of {BASE_URL+param_url} is 400, data is not added")
        json_output = {"response": "400: page not found"}
    else:
        print(f"Data not added, recieve status code: {response.status_code}")
        json_output = {"response": f"{response.status_code}: Uups I don't know this status code!"}

    return json_output


def get_tags():
    return get_gt_response("https://www.gran-turismo.com/us/gtsport/module/community/tags/")


def get_localize():
    return get_gt_response('https://www.gran-turismo.com/us/gtsport/module/community/localize/')


def get_meta():
    return get_gt_response('https://www.gran-turismo.com/us/gtsport/module/community/meta/')


def save_json(filename, json_input, folder='data'):
    if not os.path.exists(folder):
        os.makedirs(folder)

    complete_path = os.path.join(folder, filename)
    with open(complete_path, "w", encoding='utf-8') as writer:
        gt_json = json.dumps(json_input, indent=2)
        writer.write(str(gt_json) + "\n")


def save_course_records(course_id, category_id, is_category):
    filename = f'course_record_course_{course_id}_category_{category_id}_is_category_{is_category}.txt'
    course_json = get_track_records(course_id=course_id, category_id=category_id, is_category=is_category)
    # Add Parameter to JSON
    course_json["parameter"] = [{"course_id": course_id, "category_id": category_id, "is_category": is_category}]

    save_json(filename, course_json)


def get_replay():
    #f"/profile/?job=1&user_no={user_no}
    response = requests.post(BASE_URL+f"/profile/?job=4")
    print(response)

def request_with_data():
    response = requests.post("https://www.gran-turismo.com/de/api/gt7sp/profile", data={"user_no": user_no, "job": 1})
    print(json.dumps(response.json(), indent=2))
# for i in range(40):
#     save_course_records(course_id=i, category_id=13, is_category=0)
#     save_course_records(course_id=i, category_id=13, is_category=1)


# save_json('gt_tags.txt', get_tags())
# save_json('gt_localize.txt', get_localize())
# save_json('gt_meta.txt', get_meta())

#print(json.dumps(get_profile(), indent=2))
# x()

request_with_data()

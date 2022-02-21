import os
import sys
import json


if not("data2.json" in os.listdir(os.getcwd())):
    sys.exit("[!] Unable to find 'data.json' in current working direcitroy")
filename = os.path.join(os.getcwd(), "data2.json")


def updateJson(data):
    with open(filename, "w", encoding="utf-8") as wf:
        json.dump(data, wf)


def getJson():
    with open(filename, "r", encoding="utf-8") as rf:
        data = json.load(rf)
    return data


def main():
    data = getJson()
    data["DOCUMENT"]["title"] = input("Document Title: ")

    data["CONTENT"]["title"]["first_name"] = input("Title -> First Name: ")
    data["CONTENT"]["title"]["last_name"] = input("Title -> Last Name: ")
    data["CONTENT"]["title"]["subtopic"] = input("Title -> Sub Topic: ")

    # ["CONTENT"]["topics"]["topics"]
    print("Topics (Enter in format name:link) : ")
    temp_data = {}
    while True:
        temp = input("")
        temp_formatted = temp.strip().split(":")
        if temp.strip() == "done":
            break
        if (len(temp_formatted) == 1):
            print(
                f"The above entry has not ':'. {temp}. Entry will continue")
            continue
        else:
            temp_data[temp_formatted[0]] = temp_formatted[1]
    data["CONTENT"]["topics"]["topics"] = temp_data

    data["CONTENT"]["left_side"]["start"] = input("Left Side -> Start: ")
    data["CONTENT"]["left_side"]["subtopic"] = input("Left Side -> Subtopic: ")
    data["CONTENT"]["left_side"]["face_image"] = input(
        "Left Side -> Image URL: ")
    data["CONTENT"]["left_side"]["contact_details"] = input(
        "Left Side -> Contact Details: ")
    data["CONTENT"]["left_side"]["subtopic"] = input("Left Side -> Subtopic: ")


main()

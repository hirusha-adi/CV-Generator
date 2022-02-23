import os
import sys
import json


if not("data.json" in os.listdir(os.getcwd())):
    sys.exit("[!] Unable to find 'data.json' in current working direcitroy")
filename = os.path.join(os.getcwd(), "data.json")


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
        if temp.strip().lower() == "done":
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
    data["CONTENT"]["left_side"]["contact_details"]["topic"] = input(
        "Left Side -> Contact Details: ")

    # ["CONTENT"]["left_side"]["contact_details"]["fields"]
    print("Left Side -> Contact Details: ")
    temp_data = {}
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data[temp_formatted[0]] = temp_formatted

    data["CONTENT"]["left_side"]["contact_details"]["fields"] = temp_data

    data["CONTENT"]["left_side"]["email_button"]["show"] = input(
        "Left Side -> Email -> Show Button: ").strip().lower().startswith("y")
    data["CONTENT"]["left_side"]["email_button"]["email"] = input(
        "Left Side -> Email -> Address: ")
    data["CONTENT"]["left_side"]["email_button"]["button_text"] = input(
        "Left Side -> Email -> Button Text[default='Send me a message']: ")

    data["CONTENT"]["left_side"]["social"]["title"] = input(
        "Left Side -> Social -> Title: ")

    print("Left Side -> Social -> Facebook: ")
    temp_data = []
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data.append(temp_formatted)
    data["CONTENT"]["left_side"]["social"]["facebook"] = temp_data

    print("Left Side -> Social -> Twitter: ")
    temp_data = []
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data.append(temp_formatted)
    data["CONTENT"]["left_side"]["social"]["twitter"] = temp_data

    print("Left Side -> Social -> Linkedin: ")
    temp_data = []
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data.append(temp_formatted)
    data["CONTENT"]["left_side"]["social"]["linkedin"] = temp_data

    data["CONTENT"]["main"]["top_first"]["topic"] = input(
        "Body -> Top -> Topic: ")

    print("Body -> Top -> Body: ")
    temp_data = []
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data.append(temp_formatted)
    data["CONTENT"]["main"]["top_first"]["body"] = temp_data

    data["CONTENT"]["main"]["mid_first"]["topic"] = input(
        "Body -> Mid First -> Topic: ")

    print("Body -> Mid First -> Paragraph: ")
    temp_data = []
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data.append(temp_formatted)
    data["CONTENT"]["main"]["mid_first"]["body"] = temp_data

    data["CONTENT"]["main"]["mid_last"]["topic"] = input(
        "Body -> Mid Last -> Topic: ")

    print("Body -> Mid Last -> Paragraph Top: ")
    temp_data = []
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data.append(temp_formatted)
    data["CONTENT"]["main"]["mid_last"]["paragraph_top"] = temp_data

    print("Body -> Mid Last -> Paragraph Left: ")
    temp_data = []
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data.append(temp_formatted)
    data["CONTENT"]["main"]["mid_last"]["paragraph_left"] = temp_data

    print("Body -> Mid Last -> Points Right: ")
    temp_data = []
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data.append(temp_formatted)
    data["CONTENT"]["main"]["mid_last"]["points_right"] = temp_data

    data["CONTENT"]["main"]["last"]["topic"] = input(
        "Body -> Last -> Topic: ")

    print("Body -> Last -> Paragraphs: ")
    temp_data = []
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data.append(temp_formatted)
    data["CONTENT"]["main"]["last"]["paragraphs"] = temp_data

    print("Body -> Last -> Points: ")
    temp_data = []
    while True:
        temp = input("")
        temp_formatted = temp.strip()
        if temp_formatted.lower() == "done":
            break
        else:
            temp_data.append(temp_formatted)
    data["CONTENT"]["main"]["last"]["unordered_list"] = temp_data

    data["CONTENT"]["footer"] = input(
        "Footer: ")

    updateJson(data=data)


if __name__ == "__main__":
    main()

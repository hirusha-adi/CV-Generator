from flask import Flask, render_template
import os
import sys, json

app = Flask(__name__)

def loadSettings():
    if not("data.json" in os.listdir(os.getcwd())):
        sys.exit("error: 'data.json' is missing in the current working directory")
    
    with open("data.json", "r", encoding="utf-8") as jsonfile:
        jsondata = json.load(jsonfile)
    
    return jsondata

@app.route("/")
def index():
    jsondata = loadSettings()
    return render_template("index.html",
                           document_title = jsondata["DOCUMENT"]["title"],
                           content_title_first_name = jsondata["CONTENT"]["title"]["first_name"],
                           content_title_last_name = jsondata["CONTENT"]["title"]["last_name"],
                           content_title_subtopic = jsondata["CONTENT"]["title"]["subtopic"],
                           content_topics_dict_list = jsondata["CONTENT"]["topics"],
                           content_left_side_start = jsondata["CONTENT"]["left_side"]["start"],
                           content_left_side_subtopic = jsondata["CONTENT"]["left_side"]["subtopic"],
                           content_left_side_contact_details_topic = jsondata["CONTENT"]["left_side"]["contact_details"]["topic"],
                           content_left_side_contact_details_fields_dict_list = jsondata["CONTENT"]["left_side"]["contact_details"]["fields"],
                           content_left_side_contact_details_fields_dict_list = jsondata["CONTENT"]["left_side"]["contact_details"]["fields"]
                           )


if __name__ == "__main__":
    app.run("0.0.0.0", port=3338, debug=False)
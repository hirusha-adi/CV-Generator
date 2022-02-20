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
                           content_left_side_email_button_show = jsondata["CONTENT"]["left_side"]["email_button"]["show"],
                           content_left_side_email_button_email = jsondata["CONTENT"]["left_side"]["email_button"]["email"],
                           content_left_side_email_button_button_text = jsondata["CONTENT"]["left_side"]["email_button"]["button_text"],
                           content_left_side_social_title = jsondata["CONTENT"]["left_side"]["social"]["title"],
                           content_left_side_social_facebook = jsondata["CONTENT"]["left_side"]["social"]["facebook"],
                           content_left_side_social_twitter = jsondata["CONTENT"]["left_side"]["social"]["twitter"],
                           content_left_side_social_linkedin = jsondata["CONTENT"]["left_side"]["social"]["linkedin"],
                           content_main_top_first_topic = jsondata["CONTENT"]["main"]["top_first"]["topic"],
                           content_main_top_first_body_list = jsondata["CONTENT"]["main"]["top_first"]["body"],
                           content_main_mid_first_topic = jsondata["CONTENT"]["main"]["mid_first"]["topic"],
                           content_main_mid_first_body_list = jsondata["CONTENT"]["main"]["mid_first"]["body"],
                           content_main_mid_last_topic = jsondata["CONTENT"]["main"]["mid_last"]["topic"],
                           content_main_mid_last_paragraph_top= jsondata["CONTENT"]["main"]["mid_last"]["paragraph_top"],
                           content_main_mid_last_paragraph_left = jsondata["CONTENT"]["main"]["mid_last"]["paragraph_left"],
                           content_main_mid_last_points_right = jsondata["CONTENT"]["main"]["mid_last"]["points_right"],
                           content_main_last_topic = jsondata["CONTENT"]["main"]["last"]["topic"],
                           content_main_last_paragraphs = jsondata["CONTENT"]["main"]["last"]["paragraphs"],
                           content_main_last_unordered_list = jsondata["CONTENT"]["main"]["last"]["unordered_list"],
                           content_footer = jsondata["CONTENT"]["footer"]
                           )


if __name__ == "__main__":
    app.run("0.0.0.0", port=3338, debug=False)
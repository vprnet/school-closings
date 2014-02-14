from index import app
from flask import render_template, request
from config import BASE_URL
from closings import closings


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    page_title = 'School Closings'
    school_closings, timestamp = closings()

    social = {
        'title': "",
        'subtitle': "",
        'img': "",
        'description': "",
        'twitter_text': "",
        'twitter_hashtag': ""
    }

    return render_template('content.html',
        page_title=page_title,
        school_closings=school_closings,
        social=social,
        timestamp=timestamp,
        page_url=page_url)

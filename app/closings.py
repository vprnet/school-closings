#!/usr/bin/python
import requests
import xml.etree.ElementTree as ET


def closings():
    """Takes all school closings and returns a JSON-like dictionary:
    {'Vermont':
        [{'Bennington': {
            'school': school_name,
            'condition': condition}
        },
        ...
        ]
    }"""

    url = 'http://www.vabdayoff.com/cgi-bin/schoolclosings.cgi?returnbody=xml'
    r = requests.get(url)
    root = ET.fromstring(r.text)
    timestamp = root[0].text
    school_closings = {}
    for children in root[1]:
        school_dict = {}
        for child in children:
            school_dict[child.tag] = child.text
        state = school_dict['state']
        county = school_dict['county']
        closed_school = {'school': school_dict['school'],
            'condition': school_dict['condition']}
        if state in school_closings:
            if county in school_closings[state]:
                school_closings[state][county].append(closed_school)
            else:
                school_closings[state][county] = [closed_school]
        else:
            school_closings[state] = {county: [closed_school]}

    return school_closings, timestamp

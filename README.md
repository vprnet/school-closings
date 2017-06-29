# VPR's School Closings Page

This project contains the code for VPR's School Closings page.


## One-time set-up work:

1. Make sure you have Python 2.7 installed.
1. Clone the repo locally. `git clone git@github.com:vprnet/school-closings.git`
1. [Install `pip`](https://pip.pypa.io/en/latest/installing.html)
1. Install virtualenv. `pip install virtualenv`
1. Create a virtual environment for the app. `virtualenv venv`
1. Install the app requirements. `pip install -r requirements.txt`
1. Duplicate `_config.py` as `config.py`, which will be your private, git-ignored file of keys.
1. Grab the secret `homepage.json` file from someone on the VPR team.


## Regular updates, start here:

1. Enter the virtual environment. `source venv/bin/activate`
1. To run locally, just hit a quick	`python app/index.py` and head to `127.0.0.1:5000`


## Pushing to production:

This project runs on a cron job in Webfaction. The cron is currently set to run every ten minutes, pushing up to Amazon S3. To update the production code, SSH into our Webfaction server and update changes to the production code.

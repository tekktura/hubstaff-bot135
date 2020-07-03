# Project hubstaff-bot135
This is a Hubstaff API v1 example application based on Django web framework created
for Reef Technologies as part of the interview process.

## How to install and run the app

1. You must have Python 3 and `virtualenv` installed in your system. For example in Debian based
 Linux you would invoke `apt-get install python3-dev python-virtualenv` to obtain it.

2. Extract provided ZIP package to a local directory or check it out from GitHub using
`git clone https://github.com/tekktura/hubstaff-bot135.git`

3. Create local Python environment, activate it and install all dependencies using following
 commands:

   <pre>
   cd hubstaff-bot135
   virtualenv .
   source bin/activate
   pip install -r requirements.txt
   </pre>

4. Start the development server using:

   <pre>
   python hubstaff/manage.py runserver 127.0.0.1:8000
   </pre>

5. Visit http://127.0.0.1:8000 in your browser of choice to start using the app

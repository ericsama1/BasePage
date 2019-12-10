import locale


# URL to automatize
url = "https://www.saucedemo.com/"

# Name of available browsers
browsers = ['Chrome', 'Firefox', 'Ie', 'Opera', 'Edge']
browser = browsers[0]

# Path of the evidence
evidence_path = None

# Get the os language
language = locale.getdefaultlocale()[0]
language = language[:2]

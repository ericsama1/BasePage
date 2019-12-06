import locale
import ctypes


# URL to automatize
url = "https://www.saucedemo.com/"

# Name of available browsers
browsers = ['Chrome', 'Firefox', 'Ie', 'Opera', 'Edge']
browser = browsers[0]

# Path of the evidence
evidence_path = None

# Get the os language
windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
language = locale.windows_locale[windll.GetUserDefaultUILanguage()][:2]
# language = 'es'

import re, pyperclip


emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+ # name part
@      # @ symbol
[a-zA-Z0-9_.+]+ #domain name part
''', re.VERBOSE)


text = pyperclip.paste()

extractedEmail = emailRegex.findall(text)




results = '\n'.join(extractedEmail)

pyperclip.copy(results)

print(extractedEmail)

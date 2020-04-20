import re, pyperclip





text = pyperclip.paste()

extractedText = re.findall("Offert",text)

results = '\n'.join(extractedText)

pyperclip.copy(results)

print(len(extractedText))


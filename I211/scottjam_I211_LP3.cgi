#! /usr/bin/env python

import cgi

print('Content-type: text/html\n')

form = cgi.FieldStorage()
translations = {'lapse':'baby', 'wilin':'bird', 'parma':'book', 'yanta':'bridge', 'liikuma':'candle', 'meoi':'cat', 'lanne':'cloth', 'yulma':'cup', 'huo':'dog', 'fenume':'dragon', 'hen':'eye', 'taal':'foot', 'quaare':'hand', 'silmo':'moon', 'amon':'mountain', 'olva':'plant', 'malle':'road', 'lunte':'ship', 'alda':'tree'}

form_tag = """<form method="post" action="scottjam_I211_LP3.cgi">
	<p>Select a word to translate:
		<select name="elvish_word">
			<option>lapse</option>
			<option>wilin</option>
			<option>parma</option>
			<option>yanta</option>
			<option>liikuma</option>
			<option>meoi</option>
			<option>lanne</option>
			<option>yulma</option>
			<option>huo</option>
			<option>fenume</option>
			<option>hen</option>
			<option>taal</option>
			<option>quaare</option>
      <option>silmo</option>
      <option>amon</option>
      <option>olva</option>
      <option>malle</option>
      <option>lunte</option>
      <option>alda</option>
      <option>ramba</option>
		</select>
	</p>
	<p>Enter your translation:
    <input type="text" name="english_word">
	</p>
	<button type="submit">Submit</button>
</form>"""

html = """
<!doctype html>
<html>
<head><meta charset='utf-8'>
<title>Elvish Language Practice</title></head>
    <body>
    <img src="lp3img/{correct_word}.jpg" height="300" >
    <h2>{guess}</h2>
    <p>{form_tag}</p>
    </body>
</html>"""

elvish = form.getfirst('elvish_word', 'alda')
english = form.getfirst('english_word', '')

guess = ""
correct_word = str(translations[elvish])

if translations[elvish] == english:
  guess += "That's Correct!"
else:
  guess += "Sorry, the correct word was " + translations[elvish]

print(html.format(guess = guess, correct_word = correct_word, form_tag = form_tag))

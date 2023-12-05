"""
Responsivity Screenshot Saver for Hootel v3
Authors: Veronika Dudas, Adam Farkas, Zoltan Foldes, Adorjan Meszaros

Specifikacio:
	- a weboldal minden elerheto tipusu aloldalarol kapjunk screenshotot
	- megadott felbontasokban, allo es landscape modban is vizsgalja az oldalt
	- screenshotot ment el minden oldalrol, raadasul folyamatosan legorgetve

	Extrak:
	- potencialisan tobb bongeszo tipusban
	- screencapture felvetele oldalankent

Tervezes:
	- lista az osszes aloldalrol
	- lista a felbontasokrol
	- fajlnevek/mappaelnevezesek
	- github repo

Pszeudokod:
	for url in url_list:
		create_webdriver()
		get_to_url()
		for res in res_list:
			for actual_res in [res, res[::-1]]:
				while not at the bottom of the page:
					create_path()
					take_screenshot()
					screenshot.save(path)
					scroll_down(actual_res[1])
				create_path()
				take_screenshot()
				screenshot.save(path)
				scroll_to_top()
		close_webdriver()

Adatstrukturak:
	res : {
		'width' : int,
		'height' : int,
		'device' : string
	}
	res_list : [tuple]
	url : {
		'url_text' : string,
		'method' : function,
		'mappanev' : string
	}
	url_list : [url]
"""
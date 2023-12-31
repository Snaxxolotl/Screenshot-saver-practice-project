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
	- regisztráció popupban való görgetés

Tervezes:
	- lista az osszes aloldalrol
	- lista a felbontasokrol
	- fajlnevek/mappaelnevezesek
	- github repo

Pszeudokod:
	for url in url_list: x
		create_webdriver() x
		get_to_url() x
		for res in res_list: x
			for actual_res in [res, res[::-1]]: x
				while not at the bottom of the page: x
					create_path()  x
					take_screenshot() x
					screenshot.save(path) x
					scroll_down(actual_res[1]) x
		close_webdriver() x

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
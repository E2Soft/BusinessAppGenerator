Instalacija/pokretanje:
	- GeneratorSpecPlugin:
		- skinuti biblioteke navedene u /GeneratorSpecPlugin/lib/dependencies.txt i kopirati u /GeneratorSpecPlugin/lib/
		- kreirati /GeneratorSpecPlugin/build.properties sa sledecim sadrzajem (postoji i primer u build.xml):
			MAGICDRAW_EXECUTABLE=<putanja do magicdraw.exe>
			MAGICDRAW_HOME=<putanja do magicdraw root direktorijuma>
			PLUGIN_NAME=tim1.generator_spec
		- pokrenuti ant skriptu build.xml sa default ciljem (run) - plugin se kompajlira, pakuje, kopira u magicdraw i pokrece se instanca magicdraw
	- AppGenerator:
		- potrebne python biblioteke:
			- Django (1.7.6)
			- Jinja2 (2.7.3)
			- lxml (3.4.2)
			- reportlab (3.1.44)
		- generisanje:
			- preko komandne linije: 
				- pokrenuti /AppGenerator/bin/generate_app.py
				- opcija --help za nacine upotrebe
			- generisanje test projekta:
				- pokrenuti /AppGenerator/test/run_test_project.py:
					- generise se aplikacija u /AppGenerator/test/test_gen na osnovu xml modela iz /AppGenerator/test/test_data.py (generisanog na osnovu uml modela)
					- inicijalno se kreira baza i primenjuje prva migracija (kasnije regenerisanje ne dira bazu)
					- kreira se superuser username: a, password: a
					- pokrece se django test server
				- kopirati custom fajlove iz /AppGenerator/test/custom u /AppGenerator/test/test_gen/StorageApp/business_app 
				i ponovo pokrenuti /AppGenerator/test/run_test_project.py ako se django test server restartovao ili rucno pokrenuti django test server
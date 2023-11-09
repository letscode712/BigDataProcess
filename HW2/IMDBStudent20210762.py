import csv

def read_movies(filepath):
	Ani = Child = Comedy = Adv = Fant = Rom = Dra = Act = Cri = Thri = Horr = Sci = Doc = 0

	with open(filepath, 'r', encoding='utf-8') as fp:
		while True:
			line = fp.readline()

			Ani += line.count("Animation")
			Child += line.count("Children's")
			Comedy += line.count("Comedy")
			Adv += line.count("Adventure")
			Fant += line.count("Fantasy")
			Rom += line.count("Romance")
			Dra += line.count("Drama")
			Act += line.count("Action")
			Cri += line.count("Crime")
			Thri += line.count("Thriller")
			Horr += line.count("Horror")
			Sci += line.count("Sci-Fi")
			Doc += line.count("Documentary")

			if not line: break

		genre = {
			"Animation" : Ani,
			"Children's" : Child,
			"Comedy" : Comedy,
			"Adventure" : Adv,
			"Fantasy" : Fant,
			"Romance" : Rom,
			"Drama" : Dra,
			"Action" : Act,
			"Crime" : Cri,
			"Thriller" : Thri,
			"Horror" : Horr,
			"Sci-Fi" : Sci,
			"Documentary" : Doc
		}

	return genre

	
filepath = "./moives_exp.txt"
result = read_movies(filepath)
for i in result:
	print("{} {}".format(i, result[i]))
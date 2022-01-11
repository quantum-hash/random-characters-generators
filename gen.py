import random

specials = ["!","@","#","$","%","&","_"]
letters = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]


def generate():
	x = [*random.choice(specials), *random.sample([*random.choices(letters, k=6), *random.choices(numbers, k=2)], len([*random.choices(letters, k=6), *random.choices(numbers, k=2)])), *random.choice(specials), *random.choice(numbers), *random.choice(specials)]

	fi = str("").join(x)
	return("key : "+fi+"\n"+"len : "+str(len(fi)))


if __name__ == "__main__":
	print(generate())
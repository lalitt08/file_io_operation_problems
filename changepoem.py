def make_poem(poemfile, outputfile, animal, sound):
    with open('poem.txt', "r") as f1:
        poem = f1.read()

    animal = poem.replace("%ANIMAL%", animal)
    sound = animal.replace("%SOUND%", sound)
    with open('outputfile.txt', "w") as outfile:
        outfile.write(sound) 

poemfile='poem.txt'
outputfile='outputfile.txt'
animal='Dog'
sound='bow' 

make_poem(poemfile, outputfile, animal, sound)
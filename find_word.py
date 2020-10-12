import random

list = ["nada", "bahaa ", "munzer", "maram"]
word = random.choice(list)
list2 = []
count = 6
t = input("enter any char you choose")
while t not in word:

    count = count - 1
    if count == 0:
        print("game over")
    t = input("enter any char you choose")

while t in word:
    x = word.find(t)
    while len(list2) != len(word):
        if t in word:
            list2.insert(x, t)
            print(list2)
        else:
            count = count - 1
            if count == 0:
                print("game over")
        t = input("enter any char you choose")
        x = word.find(t)

    print("you success the word is {}".format(word))
    if t in word:
        break
print("thanks for your try ")

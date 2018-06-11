age = input("Enter your age: ")
gender = input("Male or Female: ")
pushups = input("Enter the number of pushup repetitions completed: ")
pushups = int(pushups)
situps = input("Enter the number of situp repetitions completed: ")
situps = int(situps)
female17_21PUScore = [29,30,32,34,36,37,39,41,43,44,46,48,50,51,53,55,57,58,60,62,63,65,67,69,70,72,74,76,77,79,81,83,84,86,88,90,91,93,95,97,98,100]
female17_21PUReps = [i for i in range (1,51)]
reps = female17_21PUReps.index(pushups)
score = female17_21PUScore[reps]
print (score)





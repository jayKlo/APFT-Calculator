#Situps
maleFemale17_21SUScore = [9,10,12,14,15,17,18,20,22,23,25,26,28,30,31,33,34,36,38,39,41,42,44,46,47,49,50,52,54,55,57,58,60,62,63,65,66,68,70,71,73,74,76,78,79,81,82,84,86,87,89,90,92,94,95,97,98,100]
maleFemale22_26SUScore = [21,23,24,25,27,28,29,31,32,33,35,36,37,39,40,41,43,44,45,47,48,49,50,52,53,55,56,57,59,60,61,63,64,65,67,68,69,71,72,73,75,76,77,79,80,81,83,84,85,87,88,89,91,92,93,95,96,97,99,100]
maleFemale27_31SUScore = [34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,90,91,92,94,95,96,97,98,99,100]
maleFemale32_36SUScore = [35,36,38,39,40,41,42,44,45,46,47,48,49,50,52,53,54,55,56,58,59,60,61,62,64,65,66,67,68,69,71,72,73,74,75,76,78,79,80,81,82,84,85,86,87,88,89,91,92,93,94,95,96,98,99,100]
maleFemale37_41SUScore = [42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100]
maleFemale42_46SUScore = [49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
maleFemale47_51SUScore = [50,51,52,53,54,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,93,94,96,97,98,99,100]
maleFemale52_56SUScore = [53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100]
maleFemale57_61SUScore = [54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,90,91,92,94,95,96,97,98,99,100]
maleFemale62SUScore = [55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,90,91,92,94,95,96,97,98,99,100]

#Situp Reps
SitupReps = [i for i in range(21,82)]

def SitUpCalc(situps,AgeGroup):
    if (AgeGroup == '17-21'):
        SUScore = maleFemale17_21SUScore[int(SitupReps.index(situps))]
    if (AgeGroup == '22-26'):
        SUScore = maleFemale22_26SUScore[int(SitupReps.index(situps))]
    if (AgeGroup == '27-31'):
        SUScore = maleFemale27_31SUScore[int(SitupReps.index(situps))]
    if (AgeGroup == '32-36'):
        SUScore = maleFemale32_36SUScore[int(SitupReps.index(situps))]
    if (AgeGroup == '37-41'):
        SUScore = maleFemale37_41SUScore[int(SitupReps.index(situps))]
    if (AgeGroup == '42-46'):
        SUScore = maleFemale42_46SUScore[int(SitupReps.index(situps))]
    if (AgeGroup == '47-51'):
        SUScore = maleFemale47_51SUScore[int(SitupReps.index(situps))]
    if (AgeGroup == '52-56'):
        SUScore = maleFemale52_56SUScore[int(SitupReps.index(situps))]
    if (AgeGroup == '57-61'):
        SUScore = maleFemale57_61SUScore[int(SitupReps.index(situps))]
    if (AgeGroup == '62+'):
        SUScore = maleFemale62SUScore[int(SitupReps.index(situps))]
    return SUScore


if __name__ == "__main__":
    main()

def AgeGroup(age):
    if ((age >=17) and (age < 22)):
        AgeGroup = '17-21'
    if ((age >=22) and (age < 27)):
        AgeGroup = '22-26'
    if ((age >= 27) and (age < 31)):
        AgeGroup = '27-31'
    if ((age >= 32) and (age < 37)):
        AgeGroup = '32-36'
    if ((age >= 37) and (age < 42)):
        AgeGroup = '37-41'
    if ((age >= 42) and (age < 47)):
        AgeGroup = '42-46'
    if ((age >= 47) and (age < 52)):
        AgeGroup = '47-51'
    if ((age >= 52) and (age < 57)):
        AgeGroup = '52-56'
    if ((age >= 57) and (age < 62)):
        AgeGroup = '57-61'
    if (age == 62):
        AgeGroup = '62+'
    if (age > 62):
        AgeGroup = "Retire already!!"
    return AgeGroup

if __name__ == "__main__":
    main()
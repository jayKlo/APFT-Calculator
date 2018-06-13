import PushUpCalc
import SitUpCalc
import RunCalc
import AgeGroup

def main():
    age = int(input("Enter your age: "))
    gender = []
    genders = ['M','m','F','f']
    while(True):
        if gender not in genders:
            gender = input("Male or Female (M/F): ")
        else:
            break
    pushups = int(input("Enter the number of pushup repetitions completed: "))
    situps = int(input("Enter the number of situp repetitions completed: "))
    runtime = input("Enter the 2 mile run time (MM:SS): ")
    AgeBracket = AgeGroup.AgeGroup(age)
    PUscore = PushUpCalc.PushUpCalc(pushups,AgeBracket)
    SUscore = SitUpCalc.SitUpCalc(situps,AgeGroup)
    Runscore = RunCalc.RunCalc(runtime,AgeGroup)
    print ("Age Group #{}".format(AgeBracket))
    print ("Pushup score {} ".format(PUscore))
    print ("Situp score {} ".format(SUscore))
    print ("Run score {} ".format(Runscore))

if __name__ == "__main__":
    main()
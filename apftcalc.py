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
    runtimeM = int(input("Enter minutes for 2 mile run time (MM): "))
    runtimeS = int(input("Enter seconds for 2 mile run time (SS): "))
    runtime = ((runtimeM*60)+(runtimeS))
    AgeBracket = AgeGroup.AgeGroup(age)
    PUscore = PushUpCalc.PushUpCalc(pushups,AgeBracket)
    SUscore = SitUpCalc.SitUpCalc(situps,AgeBracket)
    Runscore = RunCalc.RunCalc(runtime,AgeBracket)
    print ("Age Group #{}".format(AgeBracket))
    print ("Gender is: {}".format(gender))
    print ("Pushup score {} ".format(PUscore))
    print ("Situp score {} ".format(SUscore))
    print ("Run score {} ".format(Runscore))

if __name__ == "__main__":
    main()
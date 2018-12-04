import re
from datetime import datetime

with open('4.input') as f:
    input = f.readlines()

input.sort()

# Let's go object oriented for this one
class Guard:
    def __init__(self):
        self.sleepSched = {}
    def addSleep(self, day, minutes):
        self.sleepSched[day] = minutes

    def totalTimeAsleep(self):
        totalTime = 0
        for minutes in self.sleepSched.values():
            totalTime += len(minutes)
        return totalTime

    def mostCommonSleepMin(self):
        commonMins = [0 for x in range(60)]
        for minutes in self.sleepSched.values():
            for m in minutes:
                commonMins[m] += 1
        return commonMins.index(max(commonMins)), max(commonMins)


# Regexes to grab useful pieces from the log lines
guardRegex = re.compile(r'.*Guard #(\d*) begins')
asleepRegex = re.compile(r'\[(.*)\] falls asleep')
wakeRegex = re.compile(r'\[(.*)\] wakes up')


# Dict of guard objects
guards = {}

def processUntilNextGuard(guardID, logSection):
    for i, x in enumerate(logSection):
        if 'begins' in x:
            return # found next guard
        if 'asleep' in x: #process this line and the next line
          sleepTime = datetime.strptime(asleepRegex.match(x).group(1), "%Y-%m-%d %H:%M")
          wakeupTime = datetime.strptime(wakeRegex.match(logSection[i+1]).group(1), "%Y-%m-%d %H:%M")
          if guardID in guards:
            guards[guardID].addSleep(sleepTime.date, list(range(sleepTime.minute, wakeupTime.minute)))
          else:
              newGuard = Guard()
              newGuard.addSleep(sleepTime.date, list(range(sleepTime.minute, wakeupTime.minute)))
              guards[guardID] = newGuard

# Fill in guard dictionary
for i, x in enumerate(input):
    if 'begins' in x:
        processUntilNextGuard(int(guardRegex.match(x).group(1)), input[i+1:])


# Calculate part 1 from dict
myGuard = None
myGuardID = None
for guardID, guard in guards.items():
    if myGuard == None:
        myGuard = guard
        myGuardID = guardID
    elif myGuard.totalTimeAsleep() < guard.totalTimeAsleep():
        myGuard = guard
        myGuardID = guardID

asleepMin, minFreq = myGuard.mostCommonSleepMin()
print("Part 1:", asleepMin*myGuardID)


# Calculate part 2 from dict
myGuardID = None
myGuardMin = None
myGuardMinFreq = None
for guardID, guard in guards.items():
    asleepMin, minFreq = guard.mostCommonSleepMin()
    if myGuardID == None:
        myGuardID = guardID
        myGuardMin = asleepMin
        myGuardMinFreq = minFreq
    elif myGuardMinFreq < minFreq:
        myGuardID = guardID
        myGuardMin = asleepMin
        myGuardMinFreq = minFreq

print("Part 2:", myGuardMin*myGuardID)


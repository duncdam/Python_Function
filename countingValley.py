'''Gary is an avid hiker. He tracks his hikes meticulously, 
paying close attention to small details like topography. 
During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, U , or a downhill, D  step. 
Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. 
We define the following terms:
    A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
    A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
    Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
For example, if Gary's path is s =[DDUUUUUDD], he first enters a valley 2 units deep. 
Then he climbs out an up onto a mountain 2 units high. Finally, he returns to sea level and ends his hike.'''

from collections import Counter
def countingValley (string):
    '''n: the number of steps Gary takes, s: a string describing his path'''
    level = 0 #at sea level
    count = 0
    for i in range(len(string)):
        if string[i] == 'D':
            level -= 1  
            if level == -2:
                count +=1 
        else:
            level += 1 
       
    print(count,level)


string = 'DDUUDUUDDDUUUUDDDDUUDDDUUUUUDDUDDD'

countingValley(string)
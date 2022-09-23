'''
Hui Wang
SoftDev
K04 -- Dictionary
2022-09-22
time spent: 0.7 hrs
'''

"""
DISCO:
there is a random module in python, there are many functions/methods that come with
that library
dictionaries are iterable, but they are not sequences because you can't refer to the
keys as indeces, they are hashes
QCC:
How does random work? we think it refernces the time or mouse movement perhaps?
Do we have to change the devos into actual names later?
OPS SUMMARY:
Our code first picks a random key from a list of the available keys and then we pick a random person
from the list value associated with the key, then it returns that random person and the period 
"""

from pprint import pprint
import random as rng

krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
         }

# fill in the dictionary
# for key in krewes:
#     for num in range(35):
#         krewes[key].append('devo' + str(num))

def pick_rand(peeps: dict):
    
    # get random period
    periods = []
    for key in peeps:
        periods.append(key)
    rand_period = rng.choice(periods)
    
    # get random person from the chosen period
    rand_devo = rng.choice(peeps[rand_period])
    
    return (str(rand_devo) + ' from period ' + str(rand_period))
    
    

print (pick_rand(krewes))

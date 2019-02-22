
from random import choice
import sys

# Accepts .txt files as N parameters
# Outputs random words from the files in a sentence
with open(sys.argv[1], encoding="utf-8") as lo_hk, open(sys.argv[2], encoding="utf-8") as no_hk, open(sys.argv[3], encoding="utf-8") as no_kk:
    lo_list = [word.strip() for word in lo_hk]
    no_hk_list = [word.strip() for word in no_hk]
    no_kk_list = [word.strip() for word in no_kk]

print(f'Tilvera okkar er {choice(lo_list)} {choice(no_hk_list)}. Við erum {choice(no_kk_list)} og {choice(no_hk_list)} okkar er {choice(no_hk_list)}.')
#Tilvera okkar er hálflofað tuskuílag. Við erum hitahlaup og hljóðfræðirit okkar er hallklæmt.
#Tilvera okkar er handfornskt músamálverk. Við erum óhrím og akurpúlt okkar er varfeilmult.
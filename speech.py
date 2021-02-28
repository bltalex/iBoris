import random
import playsound

GS_files = [
  'GS_1.wav',
  'GS_2_great-supine-protoplasmic-invertebrate-jellies.wav',
  'GS_3 bombastic.wav',
  'GS_4_Testing.wav',
  'GS_5 my-job-is-to-protect-you-or-your-parents-or-grandparents.wav',
  'GS_6 my-job-is-to-make-sure-you-dont-have-to-wait-three-weeks-to-see-your-gp.wav',
  'GS_7_Shield.wav',
  'GS_8_Irreversible.wav',
  'GS_9-Gov.wav',
  'GS_10_Whysteps.wav',
  'GS_11_Retreat.wav',
  'GS_12_Education.wav',
  'GS_13_help.wav',
  'GS_14_reasonwhy.wav',
  'GS_15_savelives.wav'
]

GS_files = [f"snd\{i}" for i in GS_files]  # add folder location before every filename
GS_files = [i.replace(".wav",".mp3") for i in GS_files]

# Speech opening
IS_files = [
  "IS_5_Infectionshospitalsdeaths.wav",
  "IS_6_Positivetests.wav",
  "IS_7-Utmost-Care.wav",
  "IS_9_New_variant.wav",
  "IS_10_Badnews.wav",
  "IS_11_Deaths.wav",
  "IS_12_Invisiblekiller.wav",
  "IS_13_Threat.wav"
]

IS_files = [f"snd\{i}" for i in IS_files]
IS_files = [i.replace(".wav",".mp3") for i in IS_files]

# Main body - measures
MS_files = [
  "MS_5_Freedomroad.wav",
  "MS_6_addplace_reopen.wav",
  "MS_7_ruleof_addnumber.wav",
  "MS_8_University.wav",
  "MS_9_Picnic_addplace.wav",
  "MS_10_Shielding.wav",
  "MS_11_Lockdown.wav",
  "MS_12_Schools.wav",
  "MS_13_Lockdownfull.wav"
]

MS_files = [f"snd\{i}" for i in MS_files]
MS_files = [i.replace(".wav",".mp3") for i in MS_files]

# CN files are connectives
CN_files = [
  "CN_1_tellyouthebritishpeople.wav",
  "CN_2 no-ifs-or-butts.wav",
  "CN_3-Monday 8th March.wav",
  "CN_4-Step1.wav",
  "CN_5-and.wav",
  "CN_6-otherchanges.wav",
  "CN_7_Because_stressful.wav",
  "CN_8_gofurther.wav",
  "CN_9_bigmoment.wav",
  "CN_10_Dithering.wav",
  "CN_11_timetable.wav",
  "CN_12_Answer.wav",
  "CN_13_Scientists.wav",
  "CN_14_catchit.wav",
  "CN_15_Speaktonight.wav",
  "CN_16_record.wav",
  "CN_17_Letter.wav",
  "CN_18_wehaveto.wav"
]

CN_files = [f"snd\{i}" for i in CN_files]
CN_files = [i.replace(".wav",".mp3") for i in CN_files]

CC_files = [
  "CC_1 - NHS Vaccines_addnumber.wav",
  "CC_2 Unparalleled national effort.wav",
  "CC_3_National_effort.wav"
]

CC_files = [f"snd\{i}" for i in CC_files]
CC_files = [i.replace(".wav",".mp3") for i in CC_files]

#CL files, whatever they are. and some CQ also idk ahhhh ?
CL_files = [
  "CL_10_Stress.wav",
  "CL_11_Exams.wav",
  "CL_12_Decision.wav",
  "CL_13_cope.wav",
  "CQ_11_police.wav",
  "CQ_13_hanging.wav"
]

CL_files = [f"snd\{i}" for i in CL_files]
CL_files = [i.replace(".wav",".mp3") for i in CL_files]

#Numberfiles
Numberfiles = [
  "1 (number).wav",
  "17.7 million.wav",
  "2.wav",
  "27000.wav",
  "80000.wav",
  "Fifty.wav",
  "Seventy.wav",
  "Six.wav"
]

Numberfiles = [f"snd\{i}" for i in Numberfiles]
Numberfiles = [i.replace(".wav",".mp3") for i in Numberfiles]

Placefiles = [
  "classrooms.wav",
  "earlyyears.wav",
  "hairdressersnailsalons.wav",
  "Park.wav",
  "pubsrestaurants.wav",
  "Schoolscolleges.wav",
  "Shops.wav"
]

Placefiles = [f"snd\{i}" for i in Placefiles]
Placefiles = [i.replace(".wav",".mp3") for i in Placefiles]


def sound(threatlevel):

  ccn = int(round(2.9999*random.random()-0.5,0))
  gsna = int(round(-0.5+7.9999*random.random(),0))
  gsnb = int(round(7.5+6.9999*random.random(),0))
  cnna = int(round(-0.5+17.9999*random.random(),0))
  cnnb = int(round(-0.5+17.9999*random.random(),0))
  cnnc = int(round(-0.5+17.9999*random.random(),0))
  isn = int(round(threatlevel+3.9999*random.random()-1.5,0))
  msn = int(round(threatlevel+3.9999*random.random()-1.5,0))
  cln = int(round(threatlevel+1.9999*random.random()-1.5,0))
  numbernumber = int(round(8.9999*random.random()-0.5,0))
  numbernumbera = int(round(8.9999*random.random()-0.5,0))
  numbernumberb = int(round(8.9999*random.random()-0.5,0))
  placeplace = int(round(7.9999*random.random()-0.5,0))

  #Let the speech begin!
  playsound.playsound("snd\START.mp3")
  #Introduction
  if isn == 1:
    playsound.playsound(Numberfiles[numbernumber])
    playsound.playsound(IS_files[isn])
  else:
    playsound.playsound(IS_files[isn])
  #connective
  playsound.playsound(CN_files[cnna])
  #general statement
  playsound.playsound(GS_files[gsna])
  #CC Statement
  if ccn == 0:
    playsound.playsound("snd\CC_1 - NHS Vaccines_addnumber.mp3")
    playsound.playsound(Numberfiles[numbernumbera])
  else:
    playsound.playsound(CC_files[ccn])
  #connective
  playsound.playsound(CN_files[cnnb])
  #Main
  if msn == 1:
    playsound.playsound(Placefiles[placeplace])
    playsound.playsound(MS_files[1])
  elif msn == 2:
   playsound.playsound(MS_files[2])
   playsound.playsound(Numberfiles[numbernumberb])
  elif msn == 4:
    playsound.playsound(MS_files[4])
    playsound.playsound(Placefiles[placeplace])
  else:
    playsound.playsound(MS_files[msn])
  #connective
  playsound.playsound(CN_files[cnnc])
  #conclusion
  playsound.playsound(CL_files[cln])
  #general
  playsound.playsound(GS_files[gsnb])
  #end
  playsound.playsound("snd\END.mp3")
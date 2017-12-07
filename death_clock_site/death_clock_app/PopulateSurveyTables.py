from .models import *

def populateSurveyTables():
    causesOfDeath = [
        [0,"Heart Disease"],            #0
        [1,"Non-Melanoma Cancer"],      #1
        [2,"Lung Cancer"],              #2
        [3,"Breast Cancer"],            #3
        [4,"Colorectal Cancer"],        #4
        [5,"Bladder Cancer"],           #5
        [6,"Melanoma Cancer"],          #6
        [7,"Non-Hodgkins Lymphoma"],    #7
        [8,"Kidney Cancer"],            #8
        [9,"Chronic Leukemia"],         #9
        [10,"Acute Myeloid Leukemia"],   #10
        [11,"Liver Cancer"],             #11
        [12,"Ovarian Cancer"],           #12
        [13,"Esophegeal Cancer"],        #13
        [14,"Asthma"],                   #14
        [15,"COPD"],                     #15
        [16,"Accidents"],                #16
        [17,"Stroke"],                   #17
        [18,"Alzheimer's"],              #18
        [19,"Diabetes"],                 #19
        [20,"Kidney Disease"],           #20
        [21,"Suicide"],                  #21
        [22,"Prostate Cancer"]           #22
    ]
    for cause in causesOfDeath:
        c = CauseOfDeath(id=cause[0],name=cause[1])
        c.save()

    symptoms = [
        [0,"Poor Exercise", -8, False, 0],
        [1,"Poor Diet", -15, False, 0],
        [2,"Diabetes", -18, False, 0],
        [3,"Overweight", -5, False, 0],
        [4,"Alcoholic",-6,False, 0],
        [5,"Smoking", -5, False, 0],
        [6,"CHD History", 2, True, 0],
        [7,"Coronary Heart Disease", 2, True, 0],
        [8,"Congenital Heart Disease", -21, False, 0],
        [9,"Sun Exposure", -1, False, 1],
        [10,"No sunscreen", -1, False, 1],
        [11,"Tanning", -1, False, 1],
        [12,"Smoking", -21, False, 2],
        [13,"City dweler", -3, False, 2],
        [14,"Asbestos", -30, False, 2],
        [15,"Lung Cancer Stage 1", 2, True, 2],
        [16,"Lung Cancer Stage 2", 3, True, 2],
        [17,"Lung Cancer Stage 3", 4, True, 2],
        [18,"Lung Cancer Stage 4", 6, True, 2],
        [19,"Breast Cancer History -F", -8, False, 3],
        [20,"Breast Cancer History -M", -1, False, 3],
        [21,"Previous Breast Cancer", -21, False, 3],
        [22,"Ass Cancer History", -13, False, 4],
        [23,"Ass Cancer", -30, False, 4],
        [24,"Chronic Bladder Infection", -3, False, 5],
        [25,"Bladder Cancer History", -2, False, 5],
        [26,"Bladder Cancer", -16, False, 5],
        [27,"Prostate Cancer", -13, False, 22],
        [28,"Tanning", -1, False, 6],
        [29,"Melanoma Cancer History", -2, False, 6],
        [30,"Melanoma Cancer", -9, False, 6],
        [31,"AIDS", -13, False, 7],
        [32,"Non-Hodgkins Lymphoma history", -5, False, 7],
        [33,"Non-Hodgkins Lymphoma", -21,False, 7],
        [34,"Kidney Cancer History", -5, False, 8],
        [35,"Asbestos & Chemicals", -21, False, 8],
        [36,"Overweight", -3, False, 8],
        [37,"Tobacco", -8, False, 8],
        [38,"Kidney Cancer", -21, False, 8],
        [39,"Chronic Leukemia history", -5, False, 9],
        [40,"Chemical exposure", -8, False, 9],
        [41,"Chronic Leukemia", 2, True, 9],
        [42,"Acute Myeloid Leukemia History", -8, False, 10],
        [43,"Chemical exposure", -13, False, 10],
        [44,"Smoking", -21, False, 10],
        [45,"Acute Myeloid Leukemia", 4, True, 10],
        [46,"Alcoholic", -3, False, 11],
        [47,"Hep B || C || Cirrhosis", -21, False, 11],
        [48,"Liver Cancer", -56, False, 11],
        [49,"Ovarian Cancer history -F", -13, False, 12],
        [50,"Obesity -F", -2, False, 12],
        [51,"Hormone Therapy -F", -5, False, 12],
        [52,"Colorectal Cancer -F", -5, False, 12],
        [53,"Breast Cancer -F", -5, False, 12],
        [54,"Kidney Cancer -F", -5, False, 12],
        [55,"Liver Cancer -F", -5, False, 12],
        [56,"Bladder Cancer -F", -5, False, 12],
        [57,"Lung Cancer -F", -5, False, 12],
        [58,"Ovarian Cancer -F", -50, False, 12],
        [59,"Birth Control -F", 1, False, 12],
        [60,"Alcoholic", -8, False, 13],
        [61,"Smoking", -8, False, 13],
        [62,"Reflux Disorder", -2.5, False, 13],
        [63,"Poor Diet", -2.5, False, 13],
        [64,"Overweight", -1, False, 13],
        [65,"Esophageal Cancer", -73, False, 13],
        [66,"Asthma History", -1, False, 14],
        [67,"Smoking", -5, False, 14],
        [68,"Pollutants", -5, False, 14],
        [69,"Respiratory Infections", -1, False, 14],
        [70,"Asthma", 1, False, 14],
        [71,"Chronic Symptoms", -2, False, 14],
        [72,"COPD History", -8, False, 15],
        [73,"Smoking", -8, False, 15],
        [74,"Pollutants", -8, False, 15],
        [75,"Respiratory Infections", -2, False, 15],
        [76,"COPD", 2, False, 15],
        [77,"Chronic Symptoms", -8, False, 15],
        [78,"Opioid Painkillers Legal", -3, False, 16],
        [79,"Opioids || Amphetamines Illegal", -8, False, 16],
        [80,"Natural Gas", -1, False, 16],
        [81,"Driving", -2, False, 16],
        [82,"Around Cars", -2, False, 16],
        [83,"Dentures", -1, False, 16],
        [84,"Near Water", -2, False, 16],
        [85,"Can't swim", -2, False, 16],
        [86,"Pass Out || Seizures", -8, False, 16],
        [87,"-F", 0.5, True, 16],
        [88,"Forrest Fires", -1, False, 16],
        [89,"Enclosed Spaces", -1, False, 16],
        [90,"Martial Arts", -1, False, 16],
        [91,"Dangling objects", -1, False, 16],
        [92,"Fire Arms", -8, False, 16],
        [93,"Extreme Climates", -1, False, 16],
        [94,"Ladders", -1, False, 16],
        [95,"Overweight", -5, False, 17],
        [96,"Poor Diet", -3, False, 17],
        [97,"Exercise", -2, False, 17],
        [98,"Smoking", -8, False, 17],
        [99,"Stroke History", -2, False, 17],
        [100,"Prior Stroke", -5, False, 17],
        [101,"Dimentia || Mem Loss", -2, False, 18],
        [102,"Loss in problem solving", -2, False, 18],
        [103,"-F", 2, False, 18],
        [104,"Alzheimer's", 4, True, 18],
        [105,"Exercise", -2, False, 19],
        [106,"Poor Diet", -3, False, 19],
        [107,"Smoking", -1, False, 19],
        [108,"Diabetes", 2, True, 19],
        [109,"Diabetes", -5, False, 20],
        [110,"High Blood Pressure", -5, False, 20],
        [111,"Kidney Disease History", -2, False, 20],
        [112,"Kidney Damage", -2, False, 20],
        [113,"Frequent Kidney Disease", -3, False, 20],
        [114,"Suicide History", -5, False, 21],
        [115,"Child Abuse", -8, False, 21],
        [116,"Previous Attempts", -13, False, 21],
        [117,"Depression", -8, False, 21],
        [118,"Bipolar Disorder", -13, False, 21],
        [119,"PTSD", -8, False, 21],
        [120,"Schizophrenia", -5, False, 21],
        [121,"Local Epidemics", -2, False, 21],
        [122,"Suicidal Thoughts", -5, False, 21],
        [123,"Combat Vet", -21, False, 21],
        [124,"Access to Lethal", 1.5, True, 21],
        [125,"Alcoholic", 1.5, True, 21],
        [126,"Age 0-55", 1.5, True, 21],         #SPECIAL CASE
        [127,"-F", 0.25, True, 21]
    ]

    for symptom in symptoms:
        causes = CauseOfDeath.objects.filter(id=symptom[4])
        s = Symptom(id=symptom[0],name=symptom[1],impact=symptom[2],multiplier=symptom[3],cause=causes[0])
        s.save()

    questions = [
        [7,"Do you have Coronary Heart Disease?"],
        [8,"Do you have Congenital Heart Disease (CHD)?"],
        [40,"Do you have hepatitis B or C or Cirrhosis?"],
        [54,"Do you have COPD?"],
        [51,"Do you have asthma?"],
        [28,"Do you have AIDS?"],
        [84,"Do you have clinical depression?"],
        [85,"Do you have bipolar disorder?"],
        [86,"Do you have post traumatic stress disorder (PTSD)?"],
        [87,"Do you have schizophrenia?"],
        [2,"Do you have diabetes?"],
        [64,"Do you pass out or experience seizures?"],
        [76,"Do you have alzheimer's?"],
        [74,"Do you have dementia or memory loss?"],
        [46,"Do you have a reflux disorder?"],
        [77,"Do you have high blood pressure?"],
        [30,"Do you have Non-Hodgkins Lymphoma?"],
        [14,"Do you have stage 1 lung cancer?"],
        [15,"Do you have stage 2 lung cancer?"],
        [16,"Do you have stage 3 lung cancer?"],
        [17,"Do you have stage 4 lung cancer?"],
        [21,"Do you have colorectal cancer?"],
        [24,"Do you have bladder cancer?"],
        [25,"Do you have prostate cancer?"],
        [27,"Do you have melanoma cancer?"],
        [39,"Do you have acute myeloid leukemia?"],
        [37,"Do you have Chronic Leukemia?"],
        [41,"Do you have liver cancer?"],
        [45,"Do you have ovarian cancer?"],
        [47,"Do you have esophageal cancer?"],
        [34,"Do you have kidney cancer?"],
        [19,"Have you had breast cancer in the past, or do you currently have breast cancer?"],
        [18,"Do you have a family history of breast cancer?"],
        [20,"Do you have a family history of colorectal cancer?"],
        [23,"Do you have a family history of bladder cancer?"],
        [26,"Do you have a family history of melanoma cancer?"],
        [42,"Do you have a family history of ovarian cancer?"],
        [35,"Do you have a family history of chronic leukemia?"],
        [38,"Do you have a family history of acute myeloid leukemia?"],
        [29,"Do you have a family history of Non-Hodgkins Lymphoma?"],
        [31,"Do you have a family history of kidney cancer?"],
        [78,"Do you have a family history of kidney disease?"],
        [6,"Do you have a family history of congenital heart disease?"],
        [72,"Do you have a family history of strokes?"],
        [53,"Do you have a family history of COPD?"],
        [48,"Do you have a family history of asthma?"],
        [81,"Do you have a family history of suicide?"],
        [22,"Do you get chronic bladder infections?"],
        [0,"Do you exercise less than 3 hours a week?"],
        [1,"Do you eat less than 1 serving of both fruits or vegetables per day?"],
        [3,"Are you overweight?"],
        [4,"Do you consume greater than 1 alcoholic beverage per day?"],
        [5,"Do you smoke more than 1 pack of cigarettes or 1 cigar per day?"],
        [33,"Do you use tobacco products?"],
        [82,"Were you mistreated as a child?"],
        [90,"Are you a veteran that has been awarded a combat action ribbon?"],
        [10,"Do you use sunscreen on a regular basis?"],
        [9,"Do you spend greater than 30 hours a week in the sun?"],
        [11,"Do you tan one time a week or more?"],
        [70,"Do you live in an area that gets below 0 frequently in the winter or over 100 frequently in the summer?"],
        [12,"Do you live in a city?"],
        [13,"Do you come into contact with exposed asbestos on a regular basis?"],
        [32,"Do you come into contact with exposed asbestos, cadmium, benzene, solvents or herbicides on a regular basis?"],
        [36,"Do you come into contact with radioactive chemicals on a regular basis?"],
        [49,"Are you regularly exposed to air pollutants?"],
        [58,"Are you regularly exposed to natural gas?"],
        [43,"Are you partaking in hormone therapy?"],
        [44,"Are you on birth control?"],
        [50,"Do you frequently get respiratory infections?"],
        [52,"Do you get chronic asthma attacks?"],
        [55,"Do you get chronic COPD attacks?"],
        [61,"Do you use dentures?"],
        [56,"Do you take prescribed opioid painkillers?"],
        [57,"Have you taken unprescribed opioids or amphetamines in the last month?"],
        [62,"Do you frequently take baths, go swimming or boating?"],
        [63,"Are you unable to swim?"],
        [68,"Are you often around dangling objects?"],
        [65,"Do you live in an area at risk of forest fires?"],
        [66,"Are you frequently in enclosed spaces?"],
        [71,"Are you often on or around ladders?"],
        [73,"Have you previously had a stroke?"],
        [79,"Have you had traumatic injuries to your kidneys?"],
        [80,"Do you frequently get kidney disease?"],
        [75,"Have your problem solving skills gotten worse?"],
        [83,"Have you previously attempted suicide?"],
        [88,"Have there been recent local suicide epidemics?"],
        [89,"Have you had suicidal thoughts?"],
        [67,"Do you frequently practice martial arts?"],
        [91,"Do you have access to knives, drugs (including prescriptions), rope, or high voltage?"],
        [69,"Do you own, have access to, or are frequently around firearms?"],
        [59,"Do you drive more than 7 hours a week?"],
        [60,"Are you near vehicles for more than 3 hours a week (excluding driving)?"],
    ]

    for question in questions:
        q = Question(id=question[0],question=question[1])
        q.save()
    
    maps = [
        [0,0],
        [97,0],
        [105,0],
        [1,1],
        [63,1],
        [96,1],
        [106,1],
        [2,2],
        [108,2],
        [109,2],
        [3,3],
        [36,3],
        [64,3],
        [95,3],
        [4,4],
        [46,4],
        [60,4],
        [125,4],
        [5,5],
        [12,5],
        [44,5],
        [61,5],
        [67,5],
        [73,5],
        [98,5],
        [107,5],
        [6,6],
        [7,7],
        [8,8],
        [9,9],
        [10,10],
        [11,11],
        [28,11],
        [13,12],
        [14,13],
        [15,14],
        [16,15],
        [17,16],
        [18,17],
        [57,14],
        [57,15],
        [57,16],
        [57,17],
        [57,18],
        [19,18],
        [20,18],
        [21,19],
        [22,20],
        [23,21],
        [52,21],
        [24,22],
        [25,23],
        [26,24],
        [56,24],
        [27,25],
        [29,26],
        [30,27],
        [31,28],
        [32,29],
        [33,30],
        [34,31],
        [35,32],
        [37,33],
        [38,34],
        [54,34],
        [39,35],
        [40,36],
        [43,36],
        [41,37],
        [42,38],
        [45,39],
        [47,40],
        [48,41],
        [55,41],
        [49,42],
        [51,43],
        [59,44],
        [58,45],
        [53,19],
        [62,46],
        [65,47],
        [66,48],
        [68,49],
        [74,49],
        [69,50],
        [75,50],
        [70,51],
        [71,52],
        [72,53],
        [76,54],
        [77,55],
        [78,56],
        [79,57],
        [80,58],
        [81,59],
        [82,60],
        [83,61],
        [84,62],
        [85,63],
        [86,64],
        [88,65],
        [89,66],
        [90,67],
        [91,68],
        [92,69],
        [124,69],
        [93,70],
        [94,71],
        [87,56],
        [87,57],
        [87,58],
        [87,59],
        [87,60],
        [87,61],
        [87,62],
        [87,63],
        [87,64],
        [87,65],
        [87,66],
        [87,67],
        [87,68],
        [87,69],
        [87,70],
        [87,71],
        [99,72],
        [100,73],
        [101,74],
        [102,75],
        [104,76],
        [103,74],
        [103,75],
        [103,76],
        [110,77],
        [111,78],
        [112,79],
        [113,80],
        [114,81],
        [115,82],
        [116,83],
        [117,84],
        [118,85],
        [119,86],
        [120,87],
        [121,88],
        [122,89],
        [123,90],
        [127,4],
        [127,69],
        [127,81],
        [127,82],
        [127,83],
        [127,84],
        [127,85],
        [127,86],
        [127,87],
        [127,88],
        [127,89],
        [127,90],
        [127,91],
        [124,91]
    ]

    for map in maps:
        m = QuestionSymptomMapper(symptom=Symptom.objects.filter(id=map[0])[0],question=Question.objects.filter(id=map[1])[0])
        m.save()
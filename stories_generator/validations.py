from pyformlang.fst import FST

transducer = FST()
transducer.add_transitions([

    ('q0','H','q1',['']),
    ('q1','a','q2',['']),
    ('q2','b','q3',['']),
    ('q3','l','q4',['']),
    ('q4','a','q5',['']),
    ('q5','r','q6',['']),

    ('q6',' ','q7',['']),

    ('q7','c','q8',['']),
    ('q8','o','q9',['']),
    ('q9','n','q10',['']),

    ('q10',' ','q11',['']),

    ('q11','a','q12',['']),
    ('q12','l','q13',['']),
    ('q13','g','q14',['']),
    ('q14','u','q15',['']),
    ('q15','i','q16',['']),
    ('q16','e','q17',['']),
    ('q17','n','q18',['1']),

    ('q0','S','q19',['']),
    ('q19','e','q20',['']),
    ('q20','l','q21',['']),
    ('q21','e','q22',['']),
    ('q22','c','q23',['']),
    ('q23','c','q24',['']),
    ('q24','i','q25',['']),
    ('q25','o','q26',['']),
    ('q26','n','q27',['']),
    ('q27','a','q28',['']),
    ('q28','r','q29',['']),

    ('q29',' ','q30',['']),

    ('q30','o','q31',['']),
    ('q31','p','q32',['']),
    ('q32','c','q33',['']),
    ('q33','i','q34',['']),
    ('q34','o','q35',['']),
    ('q35','n','q36',['']),

    ('q36',' ','q37',['']),
    ('q36',' ','q39',['']),

    ('q37','1','q18',['2']),
    ('q39','2','q18',['3']),

    ('q0','I','q40',['']),
    ('q40','n','q41',['']),
    ('q41','i','q42',['']),
    ('q42','c','q43',['']),
    ('q43','i','q44',['']),
    ('q44','a','q45',['']),
    ('q45','r','q46',['']),

    ('q46',' ','q47',['']),

    ('q47','j','q48',['']),
    ('q48','u','q49',['']),
    ('q49','e','q50',['']),
    ('q50','g','q51',['']),
    ('q51','o','q18',['4']),

    ('q0','P','q52',['']),
    ('q52','e','q53',['']),
    ('q53','r','q54',['']),
    ('q54','s','q55',['']),
    ('q55','o','q56',['']),
    ('q56','n','q57',['']),
    ('q57','a','q58',['']),
    ('q58','l','q59',['']),
    ('q59','i','q60',['']),
    ('q60','z','q61',['']),
    ('q61','a','q62',['']),
    ('q62','r','q63',['']),

    ('q63',' ','q64',['']),

    ('q64','n','q65',['']),
    ('q65','o','q66',['']),
    ('q66','m','q67',['']),
    ('q67','b','q68',['']),
    ('q68','r','q69',['']),
    ('q69','e','q18',['5']),


    ('q0','V','q70',['']),
    ('q70','o','q71',['']),
    ('q71','l','q72',['']),
    ('q72','v','q73',['']),
    ('q73','e','q74',['']),
    ('q74','r','q75',['']),

    ('q75',' ','q76',['']),

    ('q76','a','q77',['']),

    ('q77',' ','q78',['']),

    ('q78','j','q79',['']),
    ('q79','u','q80',['']),
    ('q80','g','q81',['']),
    ('q81','a','q82',['']),
    ('q82','r','q18',['6']),

    ('q0','F','q83',['']),
    ('q83','i','q84',['']),
    ('q84','n','q85',['']),
    ('q85','a','q86',['']),
    ('q86','l','q87',['']),
    ('q87','i','q88',['']),
    ('q88','z','q89',['']),
    ('q89','a','q90',['']),
    ('q90','r','q91',['']),

    ('q91',' ','q92',['']),

    ('q92','j','q93',['']),
    ('q93','u','q94',['']),
    ('q94','e','q95',['']),
    ('q95','g','q96',['']),
    ('q96','o','q18',['7']),

    ('q0','D','q97',['']),
    ('q97','e','q98',['']),
    ('q98','s','q99',['']),
    ('q99','c','q100',['']),
    ('q100','r','q101',['']),
    ('q101','i','q102',['']),
    ('q102','p','q103',['']),
    ('q103','c','q104',['']),
    ('q104','i','q105',['']),
    ('q105','o','q106',['']),
    ('q106','n','q107',['']),

    ('q107',' ','q108',['']),

    ('q108','d','q109',['']),
    ('q109','e','q110',['']),
    ('q110','t','q111',['']),
    ('q111','a','q112',['']),
    ('q112','l','q113',['']),  
    ('q113','l','q114',['']),
    ('q114','a','q115',['']),
    ('q115','d','q116',['']),
    ('q116','a','q18',['8'])

])

transducer.add_start_state('q0')
transducer.add_final_state('q18')

def validate(input):
  try:
    result = "".join(list(transducer.translate(input))[0])
  except:
    return 0
  return int(result)

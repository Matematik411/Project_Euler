import math 
import itertools

def fakulteta(n):
    '''Produkt naravnih stevil do n.'''
    if n <= 1:
        return 1
    else:
        return n * fakulteta(n-1)

def binomski(n, k):
    '''Binomski simbol.'''
    return int((fakulteta(n))/(fakulteta(n-k) * fakulteta(k)))

def je_palindrom(n):
    '''Preveri ali je stevilo n palindrom.'''
    return n == int(str(n)[::-1])

def binomski_zapis(n):
    '''Transforms a number in a base 10 into base 2.'''
    binomsko = 1
    if n == 0:
        return 0
    while n > 0:
        ostanek = n % 2
        binomsko = 10*binomsko + ostanek
        n //= 2
    return int(str(binomsko)[::-1]) // 10

def je_prastevilo(n):
    '''Preveri ali je stevilo n prastevilo.'''
    if n > 1:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        return False

def je_pitagorejska_trojica(trojica):
    '''Preveri ali dana stevila ustrezajo Pitagorovem izreku.'''
    return trojica[0] ** 2 + trojica[1] ** 2 == trojica[2] ** 2

def stevilo_prafaktorjev(n):
    '''Returns the number of distinct prime factors.'''
    stevec = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            stevec += 1
            n //= i
            while n % i == 0:
                n //= i
    return max(stevec, 1)

def mnozica_stevk(str):
    '''Vrne znake niza v mnozici.'''
    mnozica = set()
    for a in str:
        mnozica.add(a)
    return mnozica

def naslednje_prastevilo(n):
    '''Vrne naslednje prastevilo.'''
    while True:
        n += 1
        if je_prastevilo(n):
            return n

def poker_roka(karte):
    '''Vnesi roko oblike [8, 'C', 'T', 'S', 'K', 'C', 9, 'H', 4, 'S'].'''
    for n, i in enumerate(karte):
        if i == 'H':
            karte[n] = 0
        elif i == 'D':
            karte[n] = 1
        elif i == 'S':
            karte[n] = 2
        elif i == 'C':
            karte[n] = 3
        elif i == 'A':
            karte[n] = 14
        elif i == 'T':
            karte[n] = 10
        elif i == 'J':
            karte[n] = 11
        elif i == 'Q':
            karte[n] = 12
        elif i == 'K':
            karte[n] = 13
    stevila = sorted([karte[i] for i in range(0, 10, 2)])
    barve = [karte[i] for i in range(1,10, 2)]
    b0 = barve[0]
    b1 = barve[1]
    b2 = barve[2]
    b3 = barve[3]
    b4 = barve[4]
    s0 = stevila[0]
    s1 = stevila[1]
    s2 = stevila[2]
    s3 = stevila[3]
    s4 = stevila[4]

    #Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if b0 == b1 == b2 == b3 == b4 and [10,11,12,13,14] == stevila:
        a = s4
        return [9,a]
    #Straight Flush: All cards are consecutive values of same suit.
    elif (b0 == b1 == b2 == b3 == b4 and s4 == s3 + 1 == s2 + 2 == s1 + 3 == s0 + 4):
        a = s4
        return [8,a]
    elif (b0 == b1 == b2 == b3 == b4 and [2,3,4,5,14] == stevila):
        a = s3
        return [8,a]
    #Four of a Kind: Four cards of the same value.
    elif s0 == s1 == s2 == s3 or s1 == s2 == s3 == s4:
        a = s1
        return [7,a]
    #Full House: Three of a kind and a pair.
    elif (s0 == s1 == s2 and s3 == s4) or (s0 == s1 and s2 == s3 == s4):
        a = s2
        return [6,a]
    #Flush: All cards of the same suit.
    elif b0 == b1 == b2 == b3 == b4:
        a = s4
        return [5,a]
    #Straight: All cards are consecutive values.
    elif s4 == s3 + 1 == s2 + 2 == s1 + 3 == s0 + 4:
        a = s4
        return [4,a]
    elif [2,3,4,5,14] == stevila:
        a = s3
        return [4,a]
    #Three of a Kind: Three cards of the same value. 
    elif s0 == s1 == s2 or s1 == s2 == s3 or s2 == s3 == s4:
        a = s2
        return [3,a]
    #Two Pairs: Two different pairs.
    elif (s0 == s1 and s2 == s3) or (s1 == s2 and s3 == s4) or (s0 == s1 and s3 == s4):
        a = s3
        return [2,a]
    #One Pair: Two cards of the same value.
    elif s0 == s1 or s1 == s2:
        a = s1
        return [1,a]
    elif s2 == s3 or s3 == s4:
        a = s3
        return [1,a]
    #High Card: Highest value card.
    else:
        a = s4
        return [0,a]

def katera_roka_zmaga(poker1, poker2):
    '''Vnesi roko oblike [8, 'C', 'T', 'S', 'K', 'C', 9, 'H', 4, 'S'].'''
    if poker_roka(poker1)[0] > poker_roka(poker2)[0]:
        return 0
    elif poker_roka(poker1)[0] < poker_roka(poker2)[0]:
        return 1
    elif poker_roka(poker1)[1] > poker_roka(poker2)[1]:
        return 0
    elif poker_roka(poker1)[1] < poker_roka(poker2)[1]:
        return 1
    else:
        for n, i in enumerate(poker1):
            if i == 'A':
                poker1[n] = 14
            elif i == 'T':
                poker1[n] = 10
            elif i == 'J':
                poker1[n] = 11
            elif i == 'Q':
                poker1[n] = 12
            elif i == 'K':
                poker1[n] = 13
        stevila1 = sorted([poker1[i] for i in range(0, 10, 2)])
        for n, i in enumerate(poker2):
            if i == 'A':
                poker2[n] = 14
            elif i == 'T':
                poker2[n] = 10
            elif i == 'J':
                poker2[n] = 11
            elif i == 'Q':
                poker2[n] = 12
            elif i == 'K':
                poker2[n] = 13
        stevila2 = sorted([poker2[i] for i in range(0, 10, 2)])
        for i in range(5):
            if stevila1[4-i] > stevila2[4-i]:
                return 0
            elif stevila1[4-i] < stevila2[4-i]:
                return 1
            else:
                return 'SPLIT'

def vsota_stevk(n):
    '''Vrne vsoto stevk.'''
    vsota = 0
    while n > 0:
        vsota += n % 10
        n //= 10
    return vsota

def delitelji(n):
    '''Vrne seznam vseh deliteljev n.'''
    d = []
    zacetni = n
    for i in range(2, zacetni // 2 + 1):
        if n % i == 0:
            d.append(i)
    return d + [zacetni]

def tuji_st(a,b):
    '''Ali ste stevili tuji?'''
    for d in delitelji(a):
        if d in delitelji(b):
            return False
    return True

def k_kotno(k, n):
    '''Vrne n-to k-kotno stevilo.'''
    if k == 3:
        return n * (n + 1) // 2
    if k == 4:
        return n * n
    if k == 5:
        return n * (3 * n - 1) // 2
    if k == 6:
        return n * (2 * n - 1)
    if k == 7:
        return n * (5 * n - 3) // 2
    if k == 8:
        return n * (3 * n - 2)

def gcd(m, n):
    '''Najvecji skupni veckratnik stevil n in m.'''
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

def naloga31(vrednost, seznam):
    '''How many different ways can vrednost be made using any number of coins?'''
    if seznam == []:
        return 0
    vrednost -= seznam[0]
    if vrednost == 0:
        vrednost += seznam[0]
        return 1 + naloga31(vrednost, seznam[1:])
    elif vrednost < 0:
        vrednost += seznam[0]
        return naloga31(vrednost, seznam[1:])
    elif vrednost > 0:
        return naloga31(vrednost, seznam) + naloga31(vrednost + seznam[0], seznam[1:])

def naloga32():
    '''Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.'''
    mnozica_resitev = set()
    stevke = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # dvomestno * trimestno = stirimestno
    for a in range(10, 99):
        for b in range(102, 987):
            produkt = a * b
            if produkt < 10000:
                nase_stevke = {int(str(a)[0]), int(str(a)[1]), int(str(b)[0]), int(str(b)[1]), int(str(b)[2]), int(str(produkt)[0]), int(str(produkt)[1]), int(str(produkt)[2]), int(str(produkt)[3])}
                if stevke == nase_stevke:
                    mnozica_resitev.add(produkt)
    # enomestno * stirimestno = stirimestno
    for a in range(2, 10):
        for b in range(1023, 4987):
            produkt = a * b
            if produkt < 10000:
                nase_stevke = {int(str(a)[0]), int(str(b)[0]), int(str(b)[1]), int(str(b)[2]), int(str(b)[3]), int(str(produkt)[0]), int(str(produkt)[1]), int(str(produkt)[2]), int(str(produkt)[3])}
                if stevke == nase_stevke:
                    mnozica_resitev.add(produkt)
    return sum(mnozica_resitev)

def naloga34(n):
    '''Find the sum of all numbers which are equal to the sum of the factorial of their digits.'''
    vsota_zeljenih_stevil = 0
    for stevilo in range(3,n):
        a = stevilo
        fakultete = 0
        while stevilo > 0:
            stevka = stevilo % 10
            fakultete += fakulteta(stevka)
            stevilo //= 10
        if fakultete == a:
            vsota_zeljenih_stevil += a
    return vsota_zeljenih_stevil

def naloga35(n):
    '''How many circular primes are there below n?'''
    stevilo_stevil = 0
    for a in range(n):
        kazalec = True
        if je_prastevilo(a):
            string = str(a)
            for i in range(1, len(string)):
                vrednost_permutacije = int(string[i:] + string[:i])
                if not je_prastevilo(vrednost_permutacije):
                    kazalec = False
                    break
                i += 1
            if kazalec:
                stevilo_stevil += 1
    return stevilo_stevil

def naloga36(n):
    '''Find the sum of all numbers, less than n, which are palindromic in base 10 and base 2.'''
    zeljena_vsota = 0
    for a in range(n):
        if je_palindrom(a) and je_palindrom(binomski_zapis(a)):
            zeljena_vsota += a
    return zeljena_vsota

def naloga37(n):
    '''Find the sum of the only eleven primes that are both truncatable from left to right and right to left.'''
    mnozica = []
    for stevilo in range(8,n):
        kazalec = False
        iz_leve = stevilo
        iz_desne = stevilo

        if je_prastevilo(stevilo):
            kazalec = True
            while iz_leve >= 10:
                iz_leve = int(str(iz_leve)[1:])
                if not je_prastevilo(iz_leve):
                    kazalec = False

        
        if je_prastevilo(stevilo) and kazalec:
            while iz_desne >= 10:
                iz_desne = int(str(iz_desne)[:-1])
                if not je_prastevilo(iz_desne):
                    kazalec = False

        if kazalec:
            mnozica.append(stevilo)
        #ker jih je le 11, preverim in ugotovim, da je najvecje 739397, izpisem vsoto mnozice do tega n
    return sum(mnozica)

def naloga38():
    '''What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?'''
    stevke = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    #preverim za n = 2
    zacetek = 9876
    while zacetek > 0:
        prvo = str(zacetek)
        drugo = str(2 * zacetek)
        stevke_tu = {int(prvo[0]), int(prvo[1]), int(prvo[2]), int(prvo[3]), int(drugo[0]), int(drugo[1]), int(drugo[2]), int(drugo[3]), int(drugo[4])}
        if stevke == stevke_tu:
            resitev = int(prvo + drugo)
            break
        zacetek -= 1
    return resitev

def naloga39(n):
    '''For which value of p ≤ n, is the number of solutions maximised?'''
    resitev = 0
    for vsota in range(12, n + 1):
        stevilo_trojic = 0
        for a in range(vsota // 2):
            for b in range(vsota // 3):
                if je_pitagorejska_trojica([a, b, vsota - a - b]):
                    stevilo_trojic += 1
        if stevilo_trojic > resitev:
            odklikovan_primer = vsota
            resitev = stevilo_trojic
    return odklikovan_primer

def naloga40(n):
    '''If dn represents the nth digit of the fractional part, find the value of the following expression.
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000'''
    zaporedje_stevil = ''
    stevilo = 1
    while len(zaporedje_stevil) < n:
        zaporedje_stevil += str(stevilo)
        stevilo += 1
    d1 = int(zaporedje_stevil[0])
    d10 = int(zaporedje_stevil[10 - 1])
    d100 = int(zaporedje_stevil[100 - 1])
    d1000 = int(zaporedje_stevil[1000 - 1])
    d10000 = int(zaporedje_stevil[10000 - 1])
    d100000 = int(zaporedje_stevil[100000 - 1])
    d1000000 = int(zaporedje_stevil[1000000 - 1])
    return d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

def naloga41():
    '''What is the largest n-digit pandigital prime that exists?'''
    stevke = {1, 2, 3, 4, 5, 6, 7}
    #s preverjanjem po stevilu mest pridem do 7 mestnega stevila
    stevilo = 7654321
    while True:
        if je_prastevilo(stevilo):
            zapis = str(stevilo)
            izbrane_stevke = {int(zapis[0]), int(zapis[1]), int(zapis[2]), int(zapis[3]), int(zapis[4]), int(zapis[5]), int(zapis[6])}
            if izbrane_stevke == stevke:
                break
        stevilo -= 1
    return stevilo

def naloga42():
    '''Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?'''
    besede = ["A","ABILITY","ABLE","ABOUT","ABOVE","ABSENCE","ABSOLUTELY","ACADEMIC","ACCEPT","ACCESS","ACCIDENT","ACCOMPANY","ACCORDING","ACCOUNT","ACHIEVE","ACHIEVEMENT","ACID","ACQUIRE","ACROSS","ACT","ACTION","ACTIVE","ACTIVITY","ACTUAL","ACTUALLY","ADD","ADDITION","ADDITIONAL","ADDRESS","ADMINISTRATION","ADMIT","ADOPT","ADULT","ADVANCE","ADVANTAGE","ADVICE","ADVISE","AFFAIR","AFFECT","AFFORD","AFRAID","AFTER","AFTERNOON","AFTERWARDS","AGAIN","AGAINST","AGE","AGENCY","AGENT","AGO","AGREE","AGREEMENT","AHEAD","AID","AIM","AIR","AIRCRAFT","ALL","ALLOW","ALMOST","ALONE","ALONG","ALREADY","ALRIGHT","ALSO","ALTERNATIVE","ALTHOUGH","ALWAYS","AMONG","AMONGST","AMOUNT","AN","ANALYSIS","ANCIENT","AND","ANIMAL","ANNOUNCE","ANNUAL","ANOTHER","ANSWER","ANY","ANYBODY","ANYONE","ANYTHING","ANYWAY","APART","APPARENT","APPARENTLY","APPEAL","APPEAR","APPEARANCE","APPLICATION","APPLY","APPOINT","APPOINTMENT","APPROACH","APPROPRIATE","APPROVE","AREA","ARGUE","ARGUMENT","ARISE","ARM","ARMY","AROUND","ARRANGE","ARRANGEMENT","ARRIVE","ART","ARTICLE","ARTIST","AS","ASK","ASPECT","ASSEMBLY","ASSESS","ASSESSMENT","ASSET","ASSOCIATE","ASSOCIATION","ASSUME","ASSUMPTION","AT","ATMOSPHERE","ATTACH","ATTACK","ATTEMPT","ATTEND","ATTENTION","ATTITUDE","ATTRACT","ATTRACTIVE","AUDIENCE","AUTHOR","AUTHORITY","AVAILABLE","AVERAGE","AVOID","AWARD","AWARE","AWAY","AYE","BABY","BACK","BACKGROUND","BAD","BAG","BALANCE","BALL","BAND","BANK","BAR","BASE","BASIC","BASIS","BATTLE","BE","BEAR","BEAT","BEAUTIFUL","BECAUSE","BECOME","BED","BEDROOM","BEFORE","BEGIN","BEGINNING","BEHAVIOUR","BEHIND","BELIEF","BELIEVE","BELONG","BELOW","BENEATH","BENEFIT","BESIDE","BEST","BETTER","BETWEEN","BEYOND","BIG","BILL","BIND","BIRD","BIRTH","BIT","BLACK","BLOCK","BLOOD","BLOODY","BLOW","BLUE","BOARD","BOAT","BODY","BONE","BOOK","BORDER","BOTH","BOTTLE","BOTTOM","BOX","BOY","BRAIN","BRANCH","BREAK","BREATH","BRIDGE","BRIEF","BRIGHT","BRING","BROAD","BROTHER","BUDGET","BUILD","BUILDING","BURN","BUS","BUSINESS","BUSY","BUT","BUY","BY","CABINET","CALL","CAMPAIGN","CAN","CANDIDATE","CAPABLE","CAPACITY","CAPITAL","CAR","CARD","CARE","CAREER","CAREFUL","CAREFULLY","CARRY","CASE","CASH","CAT","CATCH","CATEGORY","CAUSE","CELL","CENTRAL","CENTRE","CENTURY","CERTAIN","CERTAINLY","CHAIN","CHAIR","CHAIRMAN","CHALLENGE","CHANCE","CHANGE","CHANNEL","CHAPTER","CHARACTER","CHARACTERISTIC","CHARGE","CHEAP","CHECK","CHEMICAL","CHIEF","CHILD","CHOICE","CHOOSE","CHURCH","CIRCLE","CIRCUMSTANCE","CITIZEN","CITY","CIVIL","CLAIM","CLASS","CLEAN","CLEAR","CLEARLY","CLIENT","CLIMB","CLOSE","CLOSELY","CLOTHES","CLUB","COAL","CODE","COFFEE","COLD","COLLEAGUE","COLLECT","COLLECTION","COLLEGE","COLOUR","COMBINATION","COMBINE","COME","COMMENT","COMMERCIAL","COMMISSION","COMMIT","COMMITMENT","COMMITTEE","COMMON","COMMUNICATION","COMMUNITY","COMPANY","COMPARE","COMPARISON","COMPETITION","COMPLETE","COMPLETELY","COMPLEX","COMPONENT","COMPUTER","CONCENTRATE","CONCENTRATION","CONCEPT","CONCERN","CONCERNED","CONCLUDE","CONCLUSION","CONDITION","CONDUCT","CONFERENCE","CONFIDENCE","CONFIRM","CONFLICT","CONGRESS","CONNECT","CONNECTION","CONSEQUENCE","CONSERVATIVE","CONSIDER","CONSIDERABLE","CONSIDERATION","CONSIST","CONSTANT","CONSTRUCTION","CONSUMER","CONTACT","CONTAIN","CONTENT","CONTEXT","CONTINUE","CONTRACT","CONTRAST","CONTRIBUTE","CONTRIBUTION","CONTROL","CONVENTION","CONVERSATION","COPY","CORNER","CORPORATE","CORRECT","COS","COST","COULD","COUNCIL","COUNT","COUNTRY","COUNTY","COUPLE","COURSE","COURT","COVER","CREATE","CREATION","CREDIT","CRIME","CRIMINAL","CRISIS","CRITERION","CRITICAL","CRITICISM","CROSS","CROWD","CRY","CULTURAL","CULTURE","CUP","CURRENT","CURRENTLY","CURRICULUM","CUSTOMER","CUT","DAMAGE","DANGER","DANGEROUS","DARK","DATA","DATE","DAUGHTER","DAY","DEAD","DEAL","DEATH","DEBATE","DEBT","DECADE","DECIDE","DECISION","DECLARE","DEEP","DEFENCE","DEFENDANT","DEFINE","DEFINITION","DEGREE","DELIVER","DEMAND","DEMOCRATIC","DEMONSTRATE","DENY","DEPARTMENT","DEPEND","DEPUTY","DERIVE","DESCRIBE","DESCRIPTION","DESIGN","DESIRE","DESK","DESPITE","DESTROY","DETAIL","DETAILED","DETERMINE","DEVELOP","DEVELOPMENT","DEVICE","DIE","DIFFERENCE","DIFFERENT","DIFFICULT","DIFFICULTY","DINNER","DIRECT","DIRECTION","DIRECTLY","DIRECTOR","DISAPPEAR","DISCIPLINE","DISCOVER","DISCUSS","DISCUSSION","DISEASE","DISPLAY","DISTANCE","DISTINCTION","DISTRIBUTION","DISTRICT","DIVIDE","DIVISION","DO","DOCTOR","DOCUMENT","DOG","DOMESTIC","DOOR","DOUBLE","DOUBT","DOWN","DRAW","DRAWING","DREAM","DRESS","DRINK","DRIVE","DRIVER","DROP","DRUG","DRY","DUE","DURING","DUTY","EACH","EAR","EARLY","EARN","EARTH","EASILY","EAST","EASY","EAT","ECONOMIC","ECONOMY","EDGE","EDITOR","EDUCATION","EDUCATIONAL","EFFECT","EFFECTIVE","EFFECTIVELY","EFFORT","EGG","EITHER","ELDERLY","ELECTION","ELEMENT","ELSE","ELSEWHERE","EMERGE","EMPHASIS","EMPLOY","EMPLOYEE","EMPLOYER","EMPLOYMENT","EMPTY","ENABLE","ENCOURAGE","END","ENEMY","ENERGY","ENGINE","ENGINEERING","ENJOY","ENOUGH","ENSURE","ENTER","ENTERPRISE","ENTIRE","ENTIRELY","ENTITLE","ENTRY","ENVIRONMENT","ENVIRONMENTAL","EQUAL","EQUALLY","EQUIPMENT","ERROR","ESCAPE","ESPECIALLY","ESSENTIAL","ESTABLISH","ESTABLISHMENT","ESTATE","ESTIMATE","EVEN","EVENING","EVENT","EVENTUALLY","EVER","EVERY","EVERYBODY","EVERYONE","EVERYTHING","EVIDENCE","EXACTLY","EXAMINATION","EXAMINE","EXAMPLE","EXCELLENT","EXCEPT","EXCHANGE","EXECUTIVE","EXERCISE","EXHIBITION","EXIST","EXISTENCE","EXISTING","EXPECT","EXPECTATION","EXPENDITURE","EXPENSE","EXPENSIVE","EXPERIENCE","EXPERIMENT","EXPERT","EXPLAIN","EXPLANATION","EXPLORE","EXPRESS","EXPRESSION","EXTEND","EXTENT","EXTERNAL","EXTRA","EXTREMELY","EYE","FACE","FACILITY","FACT","FACTOR","FACTORY","FAIL","FAILURE","FAIR","FAIRLY","FAITH","FALL","FAMILIAR","FAMILY","FAMOUS","FAR","FARM","FARMER","FASHION","FAST","FATHER","FAVOUR","FEAR","FEATURE","FEE","FEEL","FEELING","FEMALE","FEW","FIELD","FIGHT","FIGURE","FILE","FILL","FILM","FINAL","FINALLY","FINANCE","FINANCIAL","FIND","FINDING","FINE","FINGER","FINISH","FIRE","FIRM","FIRST","FISH","FIT","FIX","FLAT","FLIGHT","FLOOR","FLOW","FLOWER","FLY","FOCUS","FOLLOW","FOLLOWING","FOOD","FOOT","FOOTBALL","FOR","FORCE","FOREIGN","FOREST","FORGET","FORM","FORMAL","FORMER","FORWARD","FOUNDATION","FREE","FREEDOM","FREQUENTLY","FRESH","FRIEND","FROM","FRONT","FRUIT","FUEL","FULL","FULLY","FUNCTION","FUND","FUNNY","FURTHER","FUTURE","GAIN","GAME","GARDEN","GAS","GATE","GATHER","GENERAL","GENERALLY","GENERATE","GENERATION","GENTLEMAN","GET","GIRL","GIVE","GLASS","GO","GOAL","GOD","GOLD","GOOD","GOVERNMENT","GRANT","GREAT","GREEN","GREY","GROUND","GROUP","GROW","GROWING","GROWTH","GUEST","GUIDE","GUN","HAIR","HALF","HALL","HAND","HANDLE","HANG","HAPPEN","HAPPY","HARD","HARDLY","HATE","HAVE","HE","HEAD","HEALTH","HEAR","HEART","HEAT","HEAVY","HELL","HELP","HENCE","HER","HERE","HERSELF","HIDE","HIGH","HIGHLY","HILL","HIM","HIMSELF","HIS","HISTORICAL","HISTORY","HIT","HOLD","HOLE","HOLIDAY","HOME","HOPE","HORSE","HOSPITAL","HOT","HOTEL","HOUR","HOUSE","HOUSEHOLD","HOUSING","HOW","HOWEVER","HUGE","HUMAN","HURT","HUSBAND","I","IDEA","IDENTIFY","IF","IGNORE","ILLUSTRATE","IMAGE","IMAGINE","IMMEDIATE","IMMEDIATELY","IMPACT","IMPLICATION","IMPLY","IMPORTANCE","IMPORTANT","IMPOSE","IMPOSSIBLE","IMPRESSION","IMPROVE","IMPROVEMENT","IN","INCIDENT","INCLUDE","INCLUDING","INCOME","INCREASE","INCREASED","INCREASINGLY","INDEED","INDEPENDENT","INDEX","INDICATE","INDIVIDUAL","INDUSTRIAL","INDUSTRY","INFLUENCE","INFORM","INFORMATION","INITIAL","INITIATIVE","INJURY","INSIDE","INSIST","INSTANCE","INSTEAD","INSTITUTE","INSTITUTION","INSTRUCTION","INSTRUMENT","INSURANCE","INTEND","INTENTION","INTEREST","INTERESTED","INTERESTING","INTERNAL","INTERNATIONAL","INTERPRETATION","INTERVIEW","INTO","INTRODUCE","INTRODUCTION","INVESTIGATE","INVESTIGATION","INVESTMENT","INVITE","INVOLVE","IRON","IS","ISLAND","ISSUE","IT","ITEM","ITS","ITSELF","JOB","JOIN","JOINT","JOURNEY","JUDGE","JUMP","JUST","JUSTICE","KEEP","KEY","KID","KILL","KIND","KING","KITCHEN","KNEE","KNOW","KNOWLEDGE","LABOUR","LACK","LADY","LAND","LANGUAGE","LARGE","LARGELY","LAST","LATE","LATER","LATTER","LAUGH","LAUNCH","LAW","LAWYER","LAY","LEAD","LEADER","LEADERSHIP","LEADING","LEAF","LEAGUE","LEAN","LEARN","LEAST","LEAVE","LEFT","LEG","LEGAL","LEGISLATION","LENGTH","LESS","LET","LETTER","LEVEL","LIABILITY","LIBERAL","LIBRARY","LIE","LIFE","LIFT","LIGHT","LIKE","LIKELY","LIMIT","LIMITED","LINE","LINK","LIP","LIST","LISTEN","LITERATURE","LITTLE","LIVE","LIVING","LOAN","LOCAL","LOCATION","LONG","LOOK","LORD","LOSE","LOSS","LOT","LOVE","LOVELY","LOW","LUNCH","MACHINE","MAGAZINE","MAIN","MAINLY","MAINTAIN","MAJOR","MAJORITY","MAKE","MALE","MAN","MANAGE","MANAGEMENT","MANAGER","MANNER","MANY","MAP","MARK","MARKET","MARRIAGE","MARRIED","MARRY","MASS","MASTER","MATCH","MATERIAL","MATTER","MAY","MAYBE","ME","MEAL","MEAN","MEANING","MEANS","MEANWHILE","MEASURE","MECHANISM","MEDIA","MEDICAL","MEET","MEETING","MEMBER","MEMBERSHIP","MEMORY","MENTAL","MENTION","MERELY","MESSAGE","METAL","METHOD","MIDDLE","MIGHT","MILE","MILITARY","MILK","MIND","MINE","MINISTER","MINISTRY","MINUTE","MISS","MISTAKE","MODEL","MODERN","MODULE","MOMENT","MONEY","MONTH","MORE","MORNING","MOST","MOTHER","MOTION","MOTOR","MOUNTAIN","MOUTH","MOVE","MOVEMENT","MUCH","MURDER","MUSEUM","MUSIC","MUST","MY","MYSELF","NAME","NARROW","NATION","NATIONAL","NATURAL","NATURE","NEAR","NEARLY","NECESSARILY","NECESSARY","NECK","NEED","NEGOTIATION","NEIGHBOUR","NEITHER","NETWORK","NEVER","NEVERTHELESS","NEW","NEWS","NEWSPAPER","NEXT","NICE","NIGHT","NO","NOBODY","NOD","NOISE","NONE","NOR","NORMAL","NORMALLY","NORTH","NORTHERN","NOSE","NOT","NOTE","NOTHING","NOTICE","NOTION","NOW","NUCLEAR","NUMBER","NURSE","OBJECT","OBJECTIVE","OBSERVATION","OBSERVE","OBTAIN","OBVIOUS","OBVIOUSLY","OCCASION","OCCUR","ODD","OF","OFF","OFFENCE","OFFER","OFFICE","OFFICER","OFFICIAL","OFTEN","OIL","OKAY","OLD","ON","ONCE","ONE","ONLY","ONTO","OPEN","OPERATE","OPERATION","OPINION","OPPORTUNITY","OPPOSITION","OPTION","OR","ORDER","ORDINARY","ORGANISATION","ORGANISE","ORGANIZATION","ORIGIN","ORIGINAL","OTHER","OTHERWISE","OUGHT","OUR","OURSELVES","OUT","OUTCOME","OUTPUT","OUTSIDE","OVER","OVERALL","OWN","OWNER","PACKAGE","PAGE","PAIN","PAINT","PAINTING","PAIR","PANEL","PAPER","PARENT","PARK","PARLIAMENT","PART","PARTICULAR","PARTICULARLY","PARTLY","PARTNER","PARTY","PASS","PASSAGE","PAST","PATH","PATIENT","PATTERN","PAY","PAYMENT","PEACE","PENSION","PEOPLE","PER","PERCENT","PERFECT","PERFORM","PERFORMANCE","PERHAPS","PERIOD","PERMANENT","PERSON","PERSONAL","PERSUADE","PHASE","PHONE","PHOTOGRAPH","PHYSICAL","PICK","PICTURE","PIECE","PLACE","PLAN","PLANNING","PLANT","PLASTIC","PLATE","PLAY","PLAYER","PLEASE","PLEASURE","PLENTY","PLUS","POCKET","POINT","POLICE","POLICY","POLITICAL","POLITICS","POOL","POOR","POPULAR","POPULATION","POSITION","POSITIVE","POSSIBILITY","POSSIBLE","POSSIBLY","POST","POTENTIAL","POUND","POWER","POWERFUL","PRACTICAL","PRACTICE","PREFER","PREPARE","PRESENCE","PRESENT","PRESIDENT","PRESS","PRESSURE","PRETTY","PREVENT","PREVIOUS","PREVIOUSLY","PRICE","PRIMARY","PRIME","PRINCIPLE","PRIORITY","PRISON","PRISONER","PRIVATE","PROBABLY","PROBLEM","PROCEDURE","PROCESS","PRODUCE","PRODUCT","PRODUCTION","PROFESSIONAL","PROFIT","PROGRAM","PROGRAMME","PROGRESS","PROJECT","PROMISE","PROMOTE","PROPER","PROPERLY","PROPERTY","PROPORTION","PROPOSE","PROPOSAL","PROSPECT","PROTECT","PROTECTION","PROVE","PROVIDE","PROVIDED","PROVISION","PUB","PUBLIC","PUBLICATION","PUBLISH","PULL","PUPIL","PURPOSE","PUSH","PUT","QUALITY","QUARTER","QUESTION","QUICK","QUICKLY","QUIET","QUITE","RACE","RADIO","RAILWAY","RAIN","RAISE","RANGE","RAPIDLY","RARE","RATE","RATHER","REACH","REACTION","READ","READER","READING","READY","REAL","REALISE","REALITY","REALIZE","REALLY","REASON","REASONABLE","RECALL","RECEIVE","RECENT","RECENTLY","RECOGNISE","RECOGNITION","RECOGNIZE","RECOMMEND","RECORD","RECOVER","RED","REDUCE","REDUCTION","REFER","REFERENCE","REFLECT","REFORM","REFUSE","REGARD","REGION","REGIONAL","REGULAR","REGULATION","REJECT","RELATE","RELATION","RELATIONSHIP","RELATIVE","RELATIVELY","RELEASE","RELEVANT","RELIEF","RELIGION","RELIGIOUS","RELY","REMAIN","REMEMBER","REMIND","REMOVE","REPEAT","REPLACE","REPLY","REPORT","REPRESENT","REPRESENTATION","REPRESENTATIVE","REQUEST","REQUIRE","REQUIREMENT","RESEARCH","RESOURCE","RESPECT","RESPOND","RESPONSE","RESPONSIBILITY","RESPONSIBLE","REST","RESTAURANT","RESULT","RETAIN","RETURN","REVEAL","REVENUE","REVIEW","REVOLUTION","RICH","RIDE","RIGHT","RING","RISE","RISK","RIVER","ROAD","ROCK","ROLE","ROLL","ROOF","ROOM","ROUND","ROUTE","ROW","ROYAL","RULE","RUN","RURAL","SAFE","SAFETY","SALE","SAME","SAMPLE","SATISFY","SAVE","SAY","SCALE","SCENE","SCHEME","SCHOOL","SCIENCE","SCIENTIFIC","SCIENTIST","SCORE","SCREEN","SEA","SEARCH","SEASON","SEAT","SECOND","SECONDARY","SECRETARY","SECTION","SECTOR","SECURE","SECURITY","SEE","SEEK","SEEM","SELECT","SELECTION","SELL","SEND","SENIOR","SENSE","SENTENCE","SEPARATE","SEQUENCE","SERIES","SERIOUS","SERIOUSLY","SERVANT","SERVE","SERVICE","SESSION","SET","SETTLE","SETTLEMENT","SEVERAL","SEVERE","SEX","SEXUAL","SHAKE","SHALL","SHAPE","SHARE","SHE","SHEET","SHIP","SHOE","SHOOT","SHOP","SHORT","SHOT","SHOULD","SHOULDER","SHOUT","SHOW","SHUT","SIDE","SIGHT","SIGN","SIGNAL","SIGNIFICANCE","SIGNIFICANT","SILENCE","SIMILAR","SIMPLE","SIMPLY","SINCE","SING","SINGLE","SIR","SISTER","SIT","SITE","SITUATION","SIZE","SKILL","SKIN","SKY","SLEEP","SLIGHTLY","SLIP","SLOW","SLOWLY","SMALL","SMILE","SO","SOCIAL","SOCIETY","SOFT","SOFTWARE","SOIL","SOLDIER","SOLICITOR","SOLUTION","SOME","SOMEBODY","SOMEONE","SOMETHING","SOMETIMES","SOMEWHAT","SOMEWHERE","SON","SONG","SOON","SORRY","SORT","SOUND","SOURCE","SOUTH","SOUTHERN","SPACE","SPEAK","SPEAKER","SPECIAL","SPECIES","SPECIFIC","SPEECH","SPEED","SPEND","SPIRIT","SPORT","SPOT","SPREAD","SPRING","STAFF","STAGE","STAND","STANDARD","STAR","START","STATE","STATEMENT","STATION","STATUS","STAY","STEAL","STEP","STICK","STILL","STOCK","STONE","STOP","STORE","STORY","STRAIGHT","STRANGE","STRATEGY","STREET","STRENGTH","STRIKE","STRONG","STRONGLY","STRUCTURE","STUDENT","STUDIO","STUDY","STUFF","STYLE","SUBJECT","SUBSTANTIAL","SUCCEED","SUCCESS","SUCCESSFUL","SUCH","SUDDENLY","SUFFER","SUFFICIENT","SUGGEST","SUGGESTION","SUITABLE","SUM","SUMMER","SUN","SUPPLY","SUPPORT","SUPPOSE","SURE","SURELY","SURFACE","SURPRISE","SURROUND","SURVEY","SURVIVE","SWITCH","SYSTEM","TABLE","TAKE","TALK","TALL","TAPE","TARGET","TASK","TAX","TEA","TEACH","TEACHER","TEACHING","TEAM","TEAR","TECHNICAL","TECHNIQUE","TECHNOLOGY","TELEPHONE","TELEVISION","TELL","TEMPERATURE","TEND","TERM","TERMS","TERRIBLE","TEST","TEXT","THAN","THANK","THANKS","THAT","THE","THEATRE","THEIR","THEM","THEME","THEMSELVES","THEN","THEORY","THERE","THEREFORE","THESE","THEY","THIN","THING","THINK","THIS","THOSE","THOUGH","THOUGHT","THREAT","THREATEN","THROUGH","THROUGHOUT","THROW","THUS","TICKET","TIME","TINY","TITLE","TO","TODAY","TOGETHER","TOMORROW","TONE","TONIGHT","TOO","TOOL","TOOTH","TOP","TOTAL","TOTALLY","TOUCH","TOUR","TOWARDS","TOWN","TRACK","TRADE","TRADITION","TRADITIONAL","TRAFFIC","TRAIN","TRAINING","TRANSFER","TRANSPORT","TRAVEL","TREAT","TREATMENT","TREATY","TREE","TREND","TRIAL","TRIP","TROOP","TROUBLE","TRUE","TRUST","TRUTH","TRY","TURN","TWICE","TYPE","TYPICAL","UNABLE","UNDER","UNDERSTAND","UNDERSTANDING","UNDERTAKE","UNEMPLOYMENT","UNFORTUNATELY","UNION","UNIT","UNITED","UNIVERSITY","UNLESS","UNLIKELY","UNTIL","UP","UPON","UPPER","URBAN","US","USE","USED","USEFUL","USER","USUAL","USUALLY","VALUE","VARIATION","VARIETY","VARIOUS","VARY","VAST","VEHICLE","VERSION","VERY","VIA","VICTIM","VICTORY","VIDEO","VIEW","VILLAGE","VIOLENCE","VISION","VISIT","VISITOR","VITAL","VOICE","VOLUME","VOTE","WAGE","WAIT","WALK","WALL","WANT","WAR","WARM","WARN","WASH","WATCH","WATER","WAVE","WAY","WE","WEAK","WEAPON","WEAR","WEATHER","WEEK","WEEKEND","WEIGHT","WELCOME","WELFARE","WELL","WEST","WESTERN","WHAT","WHATEVER","WHEN","WHERE","WHEREAS","WHETHER","WHICH","WHILE","WHILST","WHITE","WHO","WHOLE","WHOM","WHOSE","WHY","WIDE","WIDELY","WIFE","WILD","WILL","WIN","WIND","WINDOW","WINE","WING","WINNER","WINTER","WISH","WITH","WITHDRAW","WITHIN","WITHOUT","WOMAN","WONDER","WONDERFUL","WOOD","WORD","WORK","WORKER","WORKING","WORKS","WORLD","WORRY","WORTH","WOULD","WRITE","WRITER","WRITING","WRONG","YARD","YEAH","YEAR","YES","YESTERDAY","YET","YOU","YOUNG","YOUR","YOURSELF","YOUTH"]
    trikotna_stevila = [(i*(i+1))//2 for i in range(1,30)]
    abeceda = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}
    stevilo_besed = 0
    for i in besede:
        tocke_besede = 0
        for j in i:
            tocke_besede += int(abeceda[j])
        if tocke_besede in trikotna_stevila:
            stevilo_besed += 1
    return stevilo_besed

def naloga43():
    '''Find the sum of all 0 to 9 pandigital numbers with this property.'''
    vsota = 0
    permutacije = list(itertools.permutations('1234567890'))
    for element in permutacije:
        string = ''.join(element)
        if int(string) > 1000000000:
            if int(string[1:4]) % 2 == 0 and int(string[2:5]) % 3 == 0 and int(string[3:6]) % 5 == 0 and int(string[4:7]) % 7 == 0 and int(string[5:8]) % 11 == 0 and int(string[6:9]) % 13 == 0 and int(string[7:10]) % 17 == 0:
                vsota += int(string)
    return vsota

def naloga44(n):
    '''Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?'''
    #ta rabi malo dlje, resitev pri n med 1500 in 2500
    resitev = 0
    petkotna_stevila = [(a*(3*a - 1))//2 for a in range(n)]
    for prvo in petkotna_stevila:
        del petkotna_stevila[0]
        for drugo in petkotna_stevila:
            i = petkotna_stevila.index(drugo)
            if prvo + drugo in petkotna_stevila[i + 1:]:
                tretje = prvo + drugo
                j = petkotna_stevila.index(tretje)
                if drugo + tretje in petkotna_stevila[j + 1:]:
                    resitev = prvo
                    break
        if resitev != 0:
            break
    return resitev

def naloga45(n):
    '''It can be verified that T285 = P165 = H143 = 40755.
    Find the next triangle number that is also pentagonal and hexagonal.'''
    trikotna = [a*(a+1)//2 for a in range (286, 2*n)]
    petkotna = [a*(3*a-1)//2 for a in range (166, n)]
    sestkotna = [a*(2*a-1) for a in range (144, n)]
    for stevilo in sestkotna:
        if stevilo in trikotna and stevilo in petkotna:
            resitev = stevilo
            break
    return resitev

def naloga46():
    '''What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'''
    stevilo = 35
    kazalec = True
    while kazalec:
        kazalec = False
        if not je_prastevilo(stevilo):
            for i in range(3, stevilo - 1):
                if je_prastevilo(i):
                    razlika = stevilo - i
                    razlika //= 2
                    razlika = math.sqrt(razlika)
                    if razlika % 1 == 0:
                        kazalec = True
                        break
        else:
            kazalec = True
        stevilo += 2
    return stevilo - 2

def naloga47(n):
    '''Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?'''
    #Takes a while xD
    prvi = stevilo_prafaktorjev(n)
    drugi = stevilo_prafaktorjev(n + 1)
    tretji = stevilo_prafaktorjev(n + 2)
    cetrti = stevilo_prafaktorjev(n + 3)
    if prvi == 4 and drugi == 4 and tretji == 4 and cetrti == 4:
        return n
    while True:
        prvi = drugi
        drugi = tretji
        tretji = cetrti
        cetrti = stevilo_prafaktorjev(n + 3)
        if prvi == 4 and drugi == 4 and tretji == 4 and cetrti == 4:
            break
        n += 1
    return n

def naloga48(n):
    '''Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.'''
    vsota = 0
    for i in range(1, n + 1):
        vsota += i ** i
    zadnjih_deset = vsota % 10 ** 10
    return zadnjih_deset

def naloga49():
    '''There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
    What 12-digit number do you form by concatenating the three terms in this sequence?'''
    for stevilo in range(1489, 10000):
        razlika = 1
        while stevilo + 2 * razlika < 10000:
            a2 = stevilo + razlika
            a3 = stevilo + 2 * razlika
            mnoz1 = mnozica_stevk(str(stevilo))
            mnoz2 = mnozica_stevk(str(a2))
            mnoz3 = mnozica_stevk(str(a3))
            if mnoz1 == mnoz2 and mnoz1 == mnoz3:
                if je_prastevilo(stevilo) and je_prastevilo(a2) and je_prastevilo(a3):
                    return stevilo * 100000000 + a2 * 10000 + a3
            razlika += 1

def naloga50(n):
    '''Which prime, below n, can be written as the sum of the most consecutive primes?'''
    max_dolzina = 0
    prvo = 2
    while prvo < n:
        vsota = 0
        dolzina = 0
        prastevilo = prvo
        while vsota < n:
            if je_prastevilo(vsota):
                if dolzina >= max_dolzina:
                    max_dolzina = dolzina
                    resitev = vsota
            vsota += prastevilo
            dolzina +=1
            prastevilo = naslednje_prastevilo(prastevilo)
        prvo = naslednje_prastevilo(prvo)
    return resitev
    
def naloga52():
    '''Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.'''
    x = 1
    while True:
        if mnozica_stevk(str(1 * x)) == mnozica_stevk(str(2 * x)) == mnozica_stevk(str(3 * x)) == mnozica_stevk(str(4 * x)) == mnozica_stevk(str(5 * x)) == mnozica_stevk(str(6 * x)):
            return x
        x += 1

def naloga53(n):
    '''How many, not necessarily distinct, values of nCr for 1≤n≤100, are greater than n?'''
    stevec = 0
    for i in range(1, 101):
        for j in range(i + 1):
            if binomski(i, j) > n:
                stevec += 1
    return stevec

def naloga54():
    seznam_rok = [[8, 'C', 'T', 'S', 'K', 'C', 9, 'H', 4, 'S'],[7, 'D', 2, 'S', 5, 'D', 3, 'S', 'A', 'C'],[5, 'C', 'A', 'D', 5, 'D', 'A', 'C', 9, 'C'],[7, 'C', 5, 'H', 8, 'D', 'T', 'D', 'K', 'S'],[3, 'H', 7, 'H', 6, 'S', 'K', 'C', 'J', 'S'],['Q', 'H', 'T', 'D', 'J', 'C', 2, 'D', 8, 'S'],['T', 'H', 8, 'H', 5, 'C', 'Q', 'S', 'T', 'C'],[9, 'H', 4, 'D', 'J', 'C', 'K', 'S', 'J', 'S'],[7, 'C', 5, 'H', 'K', 'C', 'Q', 'H', 'J', 'D'],['A', 'S', 'K', 'H', 4, 'C', 'A', 'D', 4, 'S'],[5, 'H', 'K', 'S', 9, 'C', 7, 'D', 9, 'H'],[8, 'D', 3, 'S', 5, 'D', 5, 'C', 'A', 'H'],[6, 'H', 4, 'H', 5, 'C', 3, 'H', 2, 'H'],[3, 'S', 'Q', 'H', 5, 'S', 6, 'S', 'A', 'S'],['T', 'D', 8, 'C', 4, 'H', 7, 'C', 'T', 'C'],['K', 'C', 4, 'C', 3, 'H', 7, 'S', 'K', 'S'],[7, 'C', 9, 'C', 6, 'D', 'K', 'D', 3, 'H'],[4, 'C', 'Q', 'S', 'Q', 'C', 'A', 'C', 'K', 'H'],['J', 'C', 6, 'S', 5, 'H', 2, 'H', 2, 'D'],['K', 'D', 9, 'D', 7, 'C', 'A', 'S', 'J', 'S'],['A', 'D', 'Q', 'H', 'T', 'H', 9, 'D', 8, 'H'],['T', 'S', 6, 'D', 3, 'S', 'A', 'S', 'A', 'C'],[2, 'H', 4, 'S', 5, 'C', 5, 'S', 'T', 'C'],['K', 'C', 'J', 'D', 6, 'C', 'T', 'S', 3, 'C'],['Q', 'D', 'A', 'S', 6, 'H', 'J', 'S', 2, 'C'],[3, 'D', 9, 'H', 'K', 'C', 4, 'H', 8, 'S'],['K', 'D', 8, 'S', 9, 'S', 7, 'C', 2, 'S'],[3, 'S', 6, 'D', 6, 'S', 4, 'H', 'K', 'C'],[3, 'C', 8, 'C', 2, 'D', 7, 'D', 4, 'D'],[9, 'S', 4, 'S', 'Q', 'H', 4, 'H', 'J', 'D'],[8, 'C', 'K', 'C', 7, 'S', 'T', 'C', 2, 'D'],['T', 'S', 8, 'H', 'Q', 'D', 'A', 'C', 5, 'C'],[3, 'D', 'K', 'H', 'Q', 'D', 6, 'C', 6, 'S'],['A', 'D', 'A', 'S', 8, 'H', 2, 'H', 'Q', 'S'],[6, 'S', 8, 'D', 4, 'C', 8, 'S', 6, 'C'],['Q', 'H', 'T', 'C', 6, 'D', 7, 'D', 9, 'D'],[2, 'S', 8, 'D', 8, 'C', 4, 'C', 'T', 'S'],[9, 'S', 9, 'D', 9, 'C', 'A', 'C', 3, 'D'],[3, 'C', 'Q', 'S', 2, 'S', 4, 'H', 'J', 'H'],[3, 'D', 2, 'D', 'T', 'D', 8, 'S', 9, 'H'],[5, 'H', 'Q', 'S', 8, 'S', 6, 'D', 3, 'C'],[8, 'C', 'J', 'D', 'A', 'S', 7, 'H', 7, 'D'],[6, 'H', 'T', 'D', 9, 'D', 'A', 'S', 'J', 'H'],[6, 'C', 'Q', 'C', 9, 'S', 'K', 'D', 'J', 'C'],['A', 'H', 8, 'S', 'Q', 'S', 4, 'D', 'T', 'H'],['A', 'C', 'T', 'S', 3, 'C', 3, 'D', 5, 'C'],[5, 'S', 4, 'D', 'J', 'S', 3, 'D', 8, 'H'],[6, 'C', 'T', 'S', 3, 'S', 'A', 'D', 8, 'C'],[6, 'D', 7, 'C', 5, 'D', 5, 'H', 3, 'S'],[5, 'C', 'J', 'C', 2, 'H', 5, 'S', 3, 'D'],[5, 'H', 6, 'H', 2, 'S', 'K', 'S', 3, 'D'],[5, 'D', 'J', 'D', 7, 'H', 'J', 'S', 8, 'H'],['K', 'H', 4, 'H', 'A', 'S', 'J', 'S', 'Q', 'S'],['Q', 'C', 'T', 'C', 6, 'D', 7, 'C', 'K', 'S'],[3, 'D', 'Q', 'S', 'T', 'S', 2, 'H', 'J', 'S'],[4, 'D', 'A', 'S', 9, 'S', 'J', 'C', 'K', 'D'],['Q', 'D', 5, 'H', 4, 'D', 5, 'D', 'K', 'H'],[7, 'H', 3, 'D', 'J', 'S', 'K', 'D', 4, 'H'],[2, 'C', 9, 'H', 6, 'H', 5, 'C', 9, 'D'],[6, 'C', 'J', 'C', 2, 'D', 'T', 'H', 9, 'S'],[7, 'D', 6, 'D', 'A', 'S', 'Q', 'D', 'J', 'H'],[4, 'D', 'J', 'S', 7, 'C', 'Q', 'S', 5, 'C'],[3, 'H', 'K', 'H', 'Q', 'D', 'A', 'D', 8, 'C'],[8, 'H', 3, 'S', 'T', 'H', 9, 'D', 5, 'S'],['A', 'H', 9, 'S', 4, 'D', 9, 'D', 8, 'S'],[4, 'H', 'J', 'S', 3, 'C', 'T', 'C', 8, 'D'],[2, 'C', 'K', 'S', 5, 'H', 'Q', 'D', 3, 'S'],['T', 'S', 9, 'H', 'A', 'H', 'A', 'D', 8, 'S'],[5, 'C', 7, 'H', 5, 'D', 'K', 'D', 9, 'H'],[4, 'D', 3, 'D', 2, 'D', 'K', 'S', 'A', 'D'],['K', 'S', 'K', 'C', 9, 'S', 6, 'D', 2, 'C'],['Q', 'H', 9, 'D', 9, 'H', 'T', 'S', 'T', 'C'],[9, 'C', 6, 'H', 5, 'D', 'Q', 'H', 4, 'D'],['A', 'D', 6, 'D', 'Q', 'C', 'J', 'S', 'K', 'H'],[9, 'S', 3, 'H', 9, 'D', 'J', 'D', 5, 'C'],[4, 'D', 9, 'H', 'A', 'S', 'T', 'C', 'Q', 'H'],[2, 'C', 6, 'D', 'J', 'C', 9, 'C', 3, 'C'],['A', 'D', 9, 'S', 'K', 'H', 9, 'D', 7, 'D'],['K', 'C', 9, 'C', 7, 'C', 'J', 'C', 'J', 'S'],['K', 'D', 3, 'H', 'A', 'S', 3, 'C', 7, 'D'],['Q', 'D', 'K', 'H', 'Q', 'S', 2, 'C', 3, 'S'],[8, 'S', 8, 'H', 9, 'H', 9, 'C', 'J', 'C'],['Q', 'H', 8, 'D', 3, 'C', 'K', 'C', 4, 'C'],[4, 'H', 6, 'D', 'A', 'D', 9, 'H', 9, 'D'],[3, 'S', 'K', 'S', 'Q', 'S', 7, 'H', 'K', 'H'],[7, 'D', 5, 'H', 5, 'D', 'J', 'D', 'A', 'D'],[2, 'H', 2, 'C', 6, 'H', 'T', 'H', 'T', 'C'],[7, 'D', 8, 'D', 4, 'H', 8, 'C', 'A', 'S'],[4, 'S', 2, 'H', 'A', 'C', 'Q', 'C', 3, 'S'],[6, 'D', 'T', 'H', 4, 'D', 4, 'C', 'K', 'H'],[4, 'D', 'T', 'C', 'K', 'S', 'A', 'S', 7, 'C'],[3, 'C', 6, 'D', 2, 'D', 9, 'H', 6, 'C'],[8, 'C', 'T', 'D', 5, 'D', 'Q', 'S', 2, 'C'],[7, 'H', 4, 'C', 9, 'C', 3, 'H', 9, 'H'],[5, 'H', 'J', 'H', 'T', 'S', 7, 'S', 'T', 'D'],[6, 'H', 'A', 'D', 'Q', 'D', 8, 'H', 8, 'S'],[5, 'S', 'A', 'D', 9, 'C', 8, 'C', 7, 'C'],[8, 'D', 5, 'H', 9, 'D', 8, 'S', 2, 'S'],[4, 'H', 'K', 'H', 'K', 'S', 9, 'S', 2, 'S'],['K', 'C', 5, 'S', 'A', 'D', 4, 'S', 7, 'D'],['Q', 'S', 9, 'C', 'Q', 'D', 6, 'H', 'J', 'S'],[5, 'D', 'A', 'C', 8, 'D', 2, 'S', 'A', 'S'],['K', 'H', 'A', 'C', 'J', 'C', 3, 'S', 9, 'D'],[9, 'S', 3, 'C', 9, 'C', 5, 'S', 'J', 'S'],['A', 'D', 3, 'C', 3, 'D', 'K', 'S', 3, 'S'],[5, 'C', 9, 'C', 8, 'C', 'T', 'S', 4, 'S'],['J', 'H', 8, 'D', 5, 'D', 6, 'H', 'K', 'D'],['Q', 'S', 'Q', 'D', 3, 'D', 6, 'C', 'K', 'C'],[8, 'S', 'J', 'D', 6, 'C', 3, 'S', 8, 'C'],['T', 'C', 'Q', 'C', 3, 'C', 'Q', 'H', 'J', 'S'],['K', 'C', 'J', 'C', 8, 'H', 2, 'S', 9, 'H'],[9, 'C', 'J', 'H', 8, 'S', 8, 'C', 9, 'S'],[8, 'S', 2, 'H', 'Q', 'H', 4, 'D', 'Q', 'C'],[9, 'D', 'K', 'C', 'A', 'S', 'T', 'H', 3, 'C'],[8, 'S', 6, 'H', 'T', 'H', 7, 'C', 2, 'H'],[6, 'S', 3, 'C', 3, 'H', 'A', 'S', 7, 'S'],['Q', 'H', 5, 'S', 'J', 'S', 4, 'H', 5, 'H'],['T', 'S', 8, 'H', 'A', 'H', 'A', 'C', 'J', 'C'],[9, 'D', 8, 'H', 2, 'S', 4, 'S', 'T', 'C'],['J', 'C', 3, 'C', 7, 'H', 3, 'H', 5, 'C'],[3, 'D', 'A', 'D', 3, 'C', 3, 'S', 4, 'C'],['Q', 'C', 'A', 'S', 5, 'D', 'T', 'H', 8, 'C'],[6, 'S', 9, 'D', 4, 'C', 'J', 'S', 'K', 'H'],['A', 'H', 'T', 'S', 'J', 'D', 8, 'H', 'A', 'D'],[4, 'C', 6, 'S', 9, 'D', 7, 'S', 'A', 'C'],[4, 'D', 3, 'D', 3, 'S', 'T', 'C', 'J', 'D'],['A', 'D', 7, 'H', 6, 'H', 4, 'H', 'J', 'H'],['K', 'C', 'T', 'D', 'T', 'S', 7, 'D', 6, 'S'],[8, 'H', 'J', 'H', 'T', 'C', 3, 'S', 8, 'D'],[8, 'C', 9, 'S', 2, 'C', 5, 'C', 4, 'D'],[2, 'C', 9, 'D', 'K', 'C', 'Q', 'H', 'T', 'H'],['Q', 'S', 'J', 'C', 9, 'C', 4, 'H', 'T', 'S'],['Q', 'S', 3, 'C', 'Q', 'D', 8, 'H', 'K', 'H'],[4, 'H', 8, 'D', 'T', 'D', 8, 'S', 'A', 'C'],[7, 'C', 3, 'C', 'T', 'H', 5, 'S', 8, 'H'],[8, 'C', 9, 'C', 'J', 'D', 'T', 'C', 'K', 'D'],['Q', 'C', 'T', 'C', 'J', 'D', 'T', 'S', 8, 'C'],[3, 'H', 6, 'H', 'K', 'D', 7, 'C', 'T', 'D'],['J', 'H', 'Q', 'S', 'K', 'S', 9, 'C', 6, 'D'],[6, 'S', 'A', 'S', 9, 'H', 'K', 'H', 6, 'H'],[2, 'H', 4, 'D', 'A', 'H', 2, 'D', 'J', 'H'],[6, 'H', 'T', 'D', 5, 'D', 4, 'H', 'J', 'D'],['K', 'D', 8, 'C', 9, 'S', 'J', 'H', 'Q', 'D'],['J', 'S', 2, 'C', 'Q', 'S', 5, 'C', 7, 'C'],[4, 'S', 'T', 'C', 7, 'H', 8, 'D', 2, 'S'],[6, 'H', 7, 'S', 9, 'C', 7, 'C', 'K', 'C'],[8, 'C', 5, 'D', 7, 'H', 4, 'S', 'T', 'D'],['Q', 'C', 8, 'S', 'J', 'S', 4, 'H', 'K', 'S'],['A', 'D', 8, 'S', 'J', 'H', 6, 'D', 'T', 'D'],['K', 'D', 7, 'C', 6, 'C', 2, 'D', 7, 'D'],['J', 'C', 6, 'H', 6, 'S', 'J', 'S', 4, 'H'],['Q', 'H', 9, 'H', 'A', 'H', 4, 'C', 3, 'C'],[6, 'H', 5, 'H', 'A', 'S', 7, 'C', 7, 'S'],[3, 'D', 'K', 'H', 'K', 'C', 5, 'D', 5, 'C'],['J', 'C', 3, 'D', 'T', 'D', 'A', 'S', 4, 'D'],[6, 'D', 6, 'S', 'Q', 'H', 'J', 'D', 'K', 'S'],[8, 'C', 7, 'S', 8, 'S', 'Q', 'H', 2, 'S'],['J', 'D', 5, 'C', 7, 'H', 'A', 'H', 'Q', 'D'],[8, 'S', 3, 'C', 6, 'H', 6, 'C', 2, 'C'],[8, 'D', 'T', 'D', 7, 'D', 4, 'C', 4, 'D'],[5, 'D', 'Q', 'H', 'K', 'H', 7, 'C', 2, 'S'],[7, 'H', 'J', 'S', 6, 'D', 'Q', 'C', 'Q', 'D'],['A', 'D', 6, 'C', 6, 'S', 7, 'D', 'T', 'H'],[6, 'H', 2, 'H', 8, 'H', 'K', 'H', 4, 'H'],['K', 'S', 'J', 'S', 'K', 'D', 5, 'D', 2, 'D'],['K', 'H', 7, 'D', 9, 'C', 8, 'C', 3, 'D'],[9, 'C', 6, 'D', 'Q', 'D', 3, 'C', 'K', 'S'],[3, 'S', 7, 'S', 'A', 'H', 'J', 'D', 2, 'D'],['A', 'H', 'Q', 'H', 'A', 'S', 'J', 'C', 8, 'S'],[8, 'H', 4, 'C', 'K', 'C', 'T', 'H', 7, 'D'],['J', 'C', 5, 'H', 'T', 'D', 7, 'C', 5, 'D'],['K', 'D', 4, 'C', 'A', 'D', 8, 'H', 'J', 'S'],['K', 'C', 2, 'H', 'A', 'C', 'A', 'H', 7, 'D'],['J', 'H', 'K', 'H', 5, 'D', 7, 'S', 6, 'D'],[9, 'S', 5, 'S', 9, 'C', 6, 'H', 8, 'S'],['T', 'D', 'J', 'D', 9, 'H', 6, 'C', 'A', 'C'],[7, 'D', 8, 'S', 6, 'D', 'T', 'S', 'K', 'D'],[7, 'H', 'A', 'C', 5, 'S', 7, 'C', 5, 'D'],['A', 'H', 'Q', 'C', 'J', 'C', 4, 'C', 'T', 'C'],[8, 'C', 2, 'H', 'T', 'S', 2, 'C', 7, 'D'],['K', 'D', 'K', 'C', 6, 'S', 3, 'D', 7, 'D'],[2, 'S', 8, 'S', 3, 'H', 5, 'S', 5, 'C'],[8, 'S', 5, 'D', 8, 'H', 4, 'C', 6, 'H'],['K', 'C', 3, 'H', 7, 'C', 5, 'S', 'K', 'D'],['J', 'H', 8, 'C', 3, 'D', 3, 'C', 6, 'C'],['K', 'C', 'T', 'D', 7, 'H', 7, 'C', 4, 'C'],['J', 'C', 'K', 'C', 6, 'H', 'T', 'S', 'Q', 'S'],['T', 'D', 'K', 'S', 8, 'H', 8, 'C', 9, 'S'],[6, 'C', 5, 'S', 9, 'C', 'Q', 'H', 7, 'D'],['A', 'H', 'K', 'S', 'K', 'C', 9, 'S', 2, 'C'],[4, 'D', 4, 'S', 8, 'H', 'T', 'D', 9, 'C'],[3, 'S', 7, 'D', 9, 'D', 'A', 'S', 'T', 'H'],[6, 'S', 7, 'D', 3, 'C', 6, 'H', 5, 'D'],['K', 'D', 2, 'C', 5, 'C', 9, 'D', 9, 'C'],[2, 'H', 'K', 'C', 3, 'D', 'A', 'D', 3, 'H'],['Q', 'D', 'Q', 'S', 8, 'D', 'J', 'C', 4, 'S'],[8, 'C', 3, 'H', 9, 'C', 7, 'C', 'A', 'D'],[5, 'D', 'J', 'C', 9, 'D', 'J', 'S', 'A', 'S'],[5, 'D', 9, 'H', 5, 'C', 7, 'H', 6, 'S'],[6, 'C', 'Q', 'C', 'J', 'C', 'Q', 'D', 9, 'S'],['J', 'C', 'Q', 'S', 'J', 'H', 2, 'C', 6, 'S'],[9, 'C', 'Q', 'C', 3, 'D', 4, 'S', 'T', 'C'],[4, 'H', 5, 'S', 8, 'D', 3, 'D', 4, 'D'],[2, 'S', 'K', 'C', 2, 'H', 'J', 'S', 2, 'C'],['T', 'D', 3, 'S', 'T', 'H', 'K', 'D', 4, 'D'],[7, 'H', 'J', 'H', 'J', 'S', 'K', 'S', 'A', 'C'],[7, 'S', 8, 'C', 9, 'S', 2, 'D', 8, 'S'],[7, 'D', 5, 'C', 'A', 'D', 9, 'D', 'A', 'S'],[8, 'C', 7, 'H', 2, 'S', 6, 'C', 'T', 'H'],[3, 'H', 4, 'C', 3, 'S', 8, 'H', 'A', 'C'],['K', 'D', 5, 'H', 'J', 'C', 8, 'H', 'J', 'D'],[2, 'D', 4, 'H', 'T', 'D', 'J', 'H', 5, 'C'],[3, 'D', 'A', 'S', 'Q', 'H', 'K', 'S', 7, 'H'],['J', 'D', 8, 'S', 5, 'S', 6, 'D', 5, 'H'],[9, 'S', 6, 'S', 'T', 'C', 'Q', 'S', 'J', 'C'],[5, 'C', 5, 'D', 9, 'C', 'T', 'H', 8, 'C'],[5, 'H', 3, 'S', 'J', 'H', 9, 'H', 2, 'S'],[2, 'C', 6, 'S', 7, 'S', 'A', 'S', 'K', 'S'],[8, 'C', 'Q', 'D', 'J', 'C', 'Q', 'S', 'T', 'C'],['Q', 'C', 4, 'H', 'A', 'C', 'K', 'H', 6, 'C'],['T', 'C', 5, 'H', 7, 'D', 'J', 'H', 4, 'H'],[2, 'H', 8, 'D', 'J', 'C', 'K', 'S', 4, 'D'],[5, 'S', 9, 'C', 'K', 'H', 'K', 'D', 9, 'H'],[5, 'C', 'T', 'S', 3, 'D', 7, 'D', 2, 'D'],[5, 'H', 'A', 'S', 'T', 'C', 4, 'D', 8, 'C'],[2, 'C', 'T', 'S', 9, 'D', 3, 'H', 8, 'D'],[6, 'H', 8, 'D', 2, 'D', 9, 'H', 'J', 'D'],[6, 'C', 4, 'S', 5, 'H', 5, 'S', 6, 'D'],['A', 'D', 9, 'C', 'J', 'C', 7, 'D', 6, 'H'],[9, 'S', 6, 'D', 'J', 'S', 9, 'H', 3, 'C'],['A', 'D', 'J', 'H', 'T', 'C', 'Q', 'S', 4, 'C'],[5, 'D', 9, 'S', 7, 'C', 9, 'C', 'A', 'H'],['K', 'D', 6, 'H', 2, 'H', 'T', 'H', 8, 'S'],['Q', 'D', 'K', 'S', 9, 'D', 9, 'H', 'A', 'S'],[4, 'H', 8, 'H', 8, 'D', 5, 'H', 6, 'C'],['A', 'H', 5, 'S', 'A', 'S', 'A', 'D', 8, 'S'],['Q', 'S', 5, 'D', 4, 'S', 2, 'H', 'T', 'D'],['K', 'S', 5, 'H', 'A', 'C', 3, 'H', 'J', 'C'],[9, 'C', 7, 'D', 'Q', 'D', 'K', 'D', 'A', 'C'],[6, 'D', 5, 'H', 'Q', 'H', 6, 'H', 5, 'S'],['K', 'C', 'A', 'H', 'Q', 'H', 2, 'H', 7, 'D'],['Q', 'S', 3, 'H', 'K', 'S', 7, 'S', 'J', 'D'],[6, 'C', 8, 'S', 3, 'H', 6, 'D', 'K', 'S'],['Q', 'D', 5, 'D', 5, 'C', 8, 'H', 'T', 'C'],[9, 'H', 4, 'D', 4, 'S', 6, 'S', 9, 'D'],['K', 'H', 'Q', 'C', 4, 'H', 6, 'C', 'J', 'D'],['T', 'D', 2, 'D', 'Q', 'H', 4, 'S', 6, 'H'],['J', 'H', 'K', 'D', 3, 'C', 'Q', 'D', 8, 'C'],[4, 'S', 6, 'H', 7, 'C', 'Q', 'D', 9, 'D'],['A', 'S', 'A', 'H', 6, 'S', 'A', 'D', 3, 'C'],[2, 'C', 'K', 'C', 'T', 'H', 6, 'H', 8, 'D'],['A', 'H', 5, 'C', 6, 'D', 8, 'S', 5, 'D'],['T', 'D', 'T', 'S', 7, 'C', 'A', 'D', 'J', 'C'],['Q', 'D', 9, 'H', 3, 'C', 'K', 'C', 7, 'H'],[5, 'D', 4, 'D', 5, 'S', 8, 'H', 4, 'H'],[7, 'D', 3, 'H', 'J', 'D', 'K', 'D', 2, 'D'],['J', 'H', 'T', 'D', 6, 'H', 'Q', 'S', 4, 'S'],['K', 'D', 5, 'C', 8, 'S', 7, 'D', 8, 'H'],['A', 'C', 3, 'D', 'A', 'S', 8, 'C', 'T', 'D'],[7, 'H', 'K', 'H', 5, 'D', 6, 'C', 'J', 'D'],[9, 'D', 'K', 'S', 7, 'C', 6, 'D', 'Q', 'H'],['T', 'C', 'J', 'D', 'K', 'D', 'A', 'S', 'K', 'C'],['J', 'H', 8, 'S', 5, 'S', 7, 'S', 7, 'D'],['A', 'S', 2, 'D', 3, 'D', 'A', 'D', 2, 'H'],[2, 'H', 5, 'D', 'A', 'S', 3, 'C', 'Q', 'D'],['K', 'C', 6, 'H', 9, 'H', 9, 'S', 2, 'C'],[9, 'D', 5, 'D', 'T', 'H', 4, 'C', 'J', 'H'],[3, 'H', 8, 'D', 'T', 'C', 8, 'H', 9, 'H'],[6, 'H', 'K', 'D', 2, 'C', 'T', 'D', 2, 'H'],[6, 'C', 9, 'D', 2, 'D', 'J', 'S', 8, 'C'],['K', 'D', 7, 'S', 3, 'C', 7, 'C', 'A', 'S'],['Q', 'H', 'T', 'S', 'A', 'D', 8, 'C', 2, 'S'],['Q', 'S', 8, 'H', 6, 'C', 'J', 'S', 4, 'C'],[9, 'S', 'Q', 'C', 'A', 'D', 'T', 'D', 'T', 'S'],[2, 'H', 7, 'C', 'T', 'S', 'T', 'C', 8, 'C'],[3, 'C', 9, 'H', 2, 'D', 6, 'D', 'J', 'C'],['T', 'C', 2, 'H', 8, 'D', 'J', 'H', 'K', 'S'],[6, 'D', 3, 'H', 'T', 'D', 'T', 'H', 8, 'H'],[9, 'D', 'T', 'D', 9, 'H', 'Q', 'C', 5, 'D'],[6, 'C', 8, 'H', 8, 'C', 'K', 'C', 'T', 'S'],[2, 'H', 8, 'C', 3, 'D', 'A', 'H', 4, 'D'],['T', 'H', 'T', 'C', 7, 'D', 8, 'H', 'K', 'C'],['T', 'S', 5, 'C', 2, 'D', 8, 'C', 6, 'S'],['K', 'H', 'A', 'H', 5, 'H', 6, 'H', 'K', 'C'],[5, 'S', 5, 'D', 'A', 'H', 'T', 'C', 4, 'C'],['J', 'D', 8, 'D', 6, 'H', 8, 'C', 6, 'C'],['K', 'C', 'Q', 'D', 3, 'D', 8, 'H', 2, 'D'],['J', 'C', 9, 'H', 4, 'H', 'A', 'D', 2, 'S'],['T', 'D', 6, 'S', 7, 'D', 'J', 'S', 'K', 'D'],[4, 'H', 'Q', 'S', 2, 'S', 3, 'S', 8, 'C'],[4, 'C', 9, 'H', 'J', 'H', 'T', 'S', 3, 'S'],[4, 'H', 'Q', 'C', 5, 'S', 9, 'S', 9, 'C'],[2, 'C', 'K', 'D', 9, 'H', 'J', 'S', 9, 'S'],[3, 'H', 'J', 'C', 'T', 'S', 5, 'D', 'A', 'C'],['A', 'S', 2, 'H', 5, 'D', 'A', 'D', 5, 'H'],['J', 'C', 7, 'S', 'T', 'D', 'J', 'S', 4, 'C'],[2, 'D', 4, 'S', 8, 'H', 3, 'D', 7, 'D'],[2, 'C', 'A', 'D', 'K', 'D', 9, 'C', 'T', 'S'],[7, 'H', 'Q', 'D', 'J', 'H', 5, 'H', 'J', 'S'],['A', 'C', 3, 'D', 'T', 'H', 4, 'C', 8, 'H'],[6, 'D', 'K', 'H', 'K', 'C', 'Q', 'D', 5, 'C'],['A', 'D', 7, 'C', 2, 'D', 4, 'H', 'A', 'C'],[3, 'D', 9, 'D', 'T', 'C', 8, 'S', 'Q', 'D'],[2, 'C', 'J', 'C', 4, 'H', 'J', 'D', 'A', 'H'],[6, 'C', 'T', 'D', 5, 'S', 'T', 'C', 8, 'S'],['A', 'H', 2, 'C', 5, 'D', 'A', 'S', 'A', 'C'],['T', 'H', 7, 'S', 3, 'D', 'A', 'S', 6, 'C'],[4, 'C', 7, 'H', 7, 'D', 4, 'H', 'A', 'H'],[5, 'C', 2, 'H', 'K', 'S', 6, 'H', 7, 'S'],[4, 'H', 5, 'H', 3, 'D', 3, 'C', 7, 'H'],[3, 'C', 9, 'S', 'A', 'C', 7, 'S', 'Q', 'H'],[2, 'H', 3, 'D', 6, 'S', 3, 'S', 3, 'H'],[2, 'D', 3, 'H', 'A', 'S', 2, 'C', 6, 'H'],['T', 'C', 'J', 'S', 6, 'S', 9, 'C', 6, 'C'],['Q', 'H', 'K', 'D', 'Q', 'D', 6, 'D', 'A', 'C'],[6, 'H', 'K', 'H', 2, 'C', 'T', 'S', 8, 'C'],[8, 'H', 7, 'D', 3, 'S', 9, 'H', 5, 'D'],[3, 'H', 4, 'S', 'Q', 'C', 9, 'S', 5, 'H'],[2, 'D', 9, 'D', 7, 'H', 6, 'H', 3, 'C'],[8, 'S', 5, 'H', 4, 'D', 3, 'S', 4, 'S'],['K', 'D', 9, 'S', 4, 'S', 'T', 'C', 7, 'S'],['Q', 'C', 3, 'S', 8, 'S', 2, 'H', 7, 'H'],['T', 'C', 3, 'D', 8, 'C', 3, 'H', 6, 'C'],[2, 'H', 6, 'H', 'K', 'S', 'K', 'D', 4, 'D'],['K', 'C', 3, 'D', 9, 'S', 3, 'H', 'J', 'S'],[4, 'S', 8, 'H', 2, 'D', 6, 'C', 8, 'S'],[6, 'H', 'Q', 'S', 6, 'C', 'T', 'C', 'Q', 'D'],[9, 'H', 7, 'D', 7, 'C', 5, 'H', 4, 'D'],['T', 'D', 9, 'D', 8, 'D', 6, 'S', 6, 'C'],['T', 'C', 5, 'D', 'T', 'S', 'J', 'S', 8, 'H'],[4, 'H', 'K', 'C', 'J', 'D', 9, 'H', 'T', 'C'],[2, 'C', 6, 'S', 5, 'H', 8, 'H', 'A', 'S'],['J', 'S', 9, 'C', 5, 'C', 6, 'S', 9, 'D'],['J', 'D', 8, 'H', 'K', 'C', 4, 'C', 6, 'D'],[4, 'D', 8, 'D', 8, 'S', 6, 'C', 7, 'C'],[6, 'H', 7, 'H', 8, 'H', 5, 'C', 'K', 'C'],['T', 'C', 3, 'D', 'J', 'C', 6, 'D', 'K', 'S'],[9, 'S', 6, 'H', 7, 'S', 9, 'C', 2, 'C'],[6, 'C', 3, 'S', 'K', 'D', 5, 'H', 'T', 'S'],[7, 'D', 9, 'H', 9, 'S', 6, 'H', 'K', 'H'],[3, 'D', 'Q', 'D', 4, 'C', 6, 'H', 'T', 'S'],['A', 'C', 3, 'S', 5, 'C', 2, 'H', 'K', 'D'],[4, 'C', 'A', 'S', 'J', 'S', 9, 'S', 7, 'C'],['T', 'S', 7, 'H', 9, 'H', 'J', 'C', 'K', 'S'],[4, 'H', 8, 'C', 'J', 'D', 3, 'H', 6, 'H'],['A', 'D', 9, 'S', 4, 'S', 5, 'S', 'K', 'S'],[4, 'C', 2, 'C', 7, 'D', 3, 'D', 'A', 'S'],[9, 'C', 2, 'S', 'Q', 'S', 'K', 'C', 6, 'C'],[8, 'S', 5, 'H', 3, 'D', 2, 'S', 'A', 'C'],[9, 'D', 6, 'S', 3, 'S', 4, 'D', 'T', 'D'],['Q', 'D', 'T', 'H', 7, 'S', 'T', 'S', 3, 'D'],['A', 'C', 7, 'H', 6, 'C', 5, 'D', 'Q', 'C'],['T', 'C', 'Q', 'D', 'A', 'D', 9, 'C', 'Q', 'S'],[5, 'C', 8, 'D', 'K', 'D', 3, 'D', 3, 'C'],[9, 'D', 8, 'H', 'A', 'S', 3, 'S', 7, 'C'],[8, 'S', 'J', 'D', 2, 'D', 8, 'D', 'K', 'C'],[4, 'C', 'T', 'H', 'A', 'C', 'Q', 'H', 'J', 'S'],[8, 'D', 7, 'D', 7, 'S', 9, 'C', 'K', 'H'],[9, 'D', 8, 'D', 4, 'C', 'J', 'H', 2, 'C'],[2, 'S', 'Q', 'D', 'K', 'D', 'T', 'S', 4, 'H'],[4, 'D', 6, 'D', 5, 'D', 2, 'D', 'J', 'H'],[3, 'S', 8, 'S', 3, 'H', 'T', 'C', 'K', 'H'],['A', 'D', 4, 'D', 2, 'C', 'Q', 'S', 8, 'C'],['K', 'D', 'J', 'H', 'J', 'D', 'A', 'H', 5, 'C'],[5, 'C', 6, 'C', 5, 'H', 2, 'H', 'J', 'H'],[4, 'H', 'K', 'S', 7, 'C', 'T', 'C', 3, 'H'],[3, 'C', 4, 'C', 'Q', 'C', 5, 'D', 'J', 'H'],[9, 'C', 'Q', 'D', 'K', 'H', 8, 'D', 'T', 'C'],[3, 'H', 9, 'C', 'J', 'S', 7, 'H', 'Q', 'H'],['A', 'S', 7, 'C', 9, 'H', 5, 'H', 'J', 'C'],[2, 'D', 5, 'S', 'Q', 'D', 4, 'S', 3, 'C'],['K', 'C', 6, 'S', 6, 'C', 5, 'C', 4, 'C'],[5, 'D', 'K', 'H', 2, 'D', 'T', 'S', 8, 'S'],[9, 'C', 'A', 'S', 9, 'S', 7, 'C', 4, 'C'],[7, 'C', 'A', 'H', 8, 'C', 8, 'D', 5, 'S'],['K', 'D', 'Q', 'H', 'Q', 'S', 'J', 'H', 2, 'C'],[8, 'C', 9, 'D', 'A', 'H', 2, 'H', 'A', 'C'],['Q', 'C', 5, 'S', 8, 'H', 7, 'H', 2, 'C'],['Q', 'D', 9, 'H', 5, 'S', 'Q', 'S', 'Q', 'C'],[9, 'C', 5, 'H', 'J', 'C', 'T', 'H', 4, 'H'],[6, 'C', 6, 'S', 3, 'H', 5, 'H', 3, 'S'],[6, 'H', 'K', 'S', 8, 'D', 'A', 'C', 7, 'S'],['A', 'C', 'Q', 'H', 7, 'H', 8, 'C', 4, 'S'],['K', 'C', 6, 'C', 3, 'D', 3, 'S', 'T', 'C'],[9, 'D', 3, 'D', 'J', 'S', 'T', 'H', 'A', 'C'],[5, 'H', 3, 'H', 8, 'S', 3, 'S', 'T', 'C'],['Q', 'D', 'K', 'H', 'J', 'S', 'K', 'S', 9, 'S'],['Q', 'C', 8, 'D', 'A', 'H', 3, 'C', 'A', 'C'],[5, 'H', 6, 'C', 'K', 'H', 3, 'S', 9, 'S'],['J', 'H', 2, 'D', 'Q', 'D', 'A', 'S', 8, 'C'],[6, 'C', 4, 'D', 7, 'S', 7, 'H', 5, 'S'],['J', 'C', 6, 'S', 9, 'H', 4, 'H', 'J', 'H'],['A', 'H', 5, 'S', 6, 'H', 9, 'S', 'A', 'D'],[3, 'S', 'T', 'H', 2, 'H', 9, 'D', 8, 'C'],[4, 'C', 8, 'D', 9, 'H', 7, 'C', 'Q', 'C'],['A', 'D', 4, 'S', 9, 'C', 'K', 'C', 5, 'S'],[9, 'D', 6, 'H', 4, 'D', 'T', 'C', 4, 'C'],['J', 'H', 2, 'S', 5, 'D', 3, 'S', 'A', 'S'],[2, 'H', 6, 'C', 7, 'C', 'K', 'H', 5, 'C'],['A', 'D', 'Q', 'S', 'T', 'H', 'J', 'D', 8, 'S'],[3, 'S', 4, 'S', 7, 'S', 'A', 'H', 'A', 'S'],['K', 'C', 'J', 'S', 2, 'S', 'A', 'D', 'T', 'H'],['J', 'S', 'K', 'C', 2, 'S', 7, 'D', 8, 'C'],[5, 'C', 9, 'C', 'T', 'S', 5, 'H', 9, 'D'],[7, 'S', 9, 'S', 4, 'D', 'T', 'D', 'J', 'H'],['J', 'S', 'K', 'H', 6, 'H', 5, 'D', 2, 'C'],['J', 'D', 'J', 'S', 'J', 'C', 'T', 'H', 2, 'D'],[3, 'D', 'Q', 'D', 8, 'C', 'A', 'C', 5, 'H'],[7, 'S', 'K', 'H', 5, 'S', 9, 'D', 5, 'D'],['T', 'D', 4, 'S', 6, 'H', 3, 'C', 2, 'D'],[4, 'S', 5, 'D', 'A', 'C', 8, 'D', 4, 'D'],[7, 'C', 'A', 'D', 'A', 'S', 'A', 'H', 9, 'C'],[6, 'S', 'T', 'H', 'T', 'S', 'K', 'S', 2, 'C'],['Q', 'C', 'A', 'H', 'A', 'S', 3, 'C', 4, 'S'],[2, 'H', 8, 'C', 3, 'S', 'J', 'C', 5, 'C'],[7, 'C', 3, 'H', 3, 'C', 'K', 'H', 'J', 'H'],[7, 'S', 3, 'H', 'J', 'C', 5, 'S', 6, 'H'],[4, 'C', 2, 'S', 4, 'D', 'K', 'C', 7, 'H'],[4, 'D', 7, 'C', 4, 'H', 9, 'S', 8, 'S'],[6, 'S', 'A', 'D', 'T', 'C', 6, 'C', 'J', 'C'],['K', 'H', 'Q', 'S', 3, 'S', 'T', 'C', 4, 'C'],[8, 'H', 8, 'S', 'A', 'C', 3, 'C', 'T', 'S'],['Q', 'D', 'Q', 'S', 'T', 'H', 3, 'C', 'T', 'S'],[7, 'H', 7, 'D', 'A', 'H', 'T', 'D', 'J', 'C'],['T', 'D', 'J', 'D', 'Q', 'C', 4, 'D', 9, 'S'],[7, 'S', 'T', 'S', 'A', 'D', 7, 'D', 'A', 'C'],['A', 'H', 7, 'H', 4, 'S', 6, 'D', 7, 'C'],[2, 'H', 9, 'D', 'K', 'S', 'J', 'C', 'T', 'D'],[7, 'C', 'A', 'H', 'J', 'D', 4, 'H', 6, 'D'],['Q', 'S', 'T', 'S', 2, 'H', 2, 'C', 5, 'C'],['T', 'C', 'K', 'C', 8, 'C', 9, 'S', 4, 'C'],['J', 'S', 3, 'C', 'J', 'C', 6, 'S', 'A', 'H'],['A', 'S', 7, 'D', 'Q', 'C', 3, 'D', 5, 'S'],['J', 'C', 'J', 'D', 9, 'D', 'T', 'D', 'K', 'H'],['T', 'H', 3, 'C', 2, 'S', 6, 'H', 'A', 'H'],['A', 'C', 5, 'H', 5, 'C', 7, 'S', 8, 'H'],['Q', 'C', 2, 'D', 'A', 'C', 'Q', 'D', 2, 'S'],[3, 'S', 'J', 'D', 'Q', 'S', 6, 'S', 8, 'H'],['K', 'C', 4, 'H', 3, 'C', 9, 'D', 'J', 'S'],[6, 'H', 3, 'S', 8, 'S', 'A', 'S', 8, 'C'],[7, 'H', 'K', 'C', 7, 'D', 'J', 'D', 2, 'H'],['J', 'C', 'Q', 'H', 5, 'S', 3, 'H', 'Q', 'S'],[9, 'H', 'T', 'D', 3, 'S', 8, 'H', 7, 'S'],['A', 'C', 5, 'C', 6, 'C', 'A', 'H', 7, 'C'],[8, 'D', 9, 'H', 'A', 'H', 'J', 'D', 'T', 'D'],['Q', 'S', 7, 'D', 3, 'S', 9, 'C', 8, 'S'],['A', 'H', 'Q', 'H', 3, 'C', 'J', 'D', 'K', 'C'],[4, 'S', 5, 'S', 5, 'D', 'T', 'D', 'K', 'S'],[9, 'H', 7, 'H', 6, 'S', 'J', 'H', 'T', 'H'],[4, 'C', 7, 'C', 'A', 'D', 5, 'C', 2, 'D'],[7, 'C', 'K', 'D', 5, 'S', 'T', 'C', 9, 'D'],[6, 'S', 6, 'C', 5, 'D', 2, 'S', 'T', 'H'],['K', 'C', 9, 'H', 8, 'D', 5, 'H', 7, 'H'],[4, 'H', 'Q', 'C', 3, 'D', 7, 'C', 'A', 'S'],[6, 'S', 8, 'S', 'Q', 'C', 'T', 'D', 4, 'S'],[5, 'C', 'T', 'H', 'Q', 'S', 'Q', 'D', 2, 'S'],[8, 'S', 5, 'H', 'T', 'H', 'Q', 'C', 9, 'H'],[6, 'S', 'K', 'C', 7, 'D', 7, 'C', 5, 'C'],[7, 'H', 'K', 'D', 'A', 'H', 4, 'D', 'K', 'H'],[5, 'C', 4, 'S', 2, 'D', 'K', 'C', 'Q', 'H'],[6, 'S', 2, 'C', 'T', 'D', 'J', 'C', 'A', 'S'],[4, 'D', 6, 'C', 8, 'C', 4, 'H', 5, 'S'],['J', 'C', 'T', 'C', 'J', 'D', 5, 'S', 6, 'S'],[8, 'D', 'A', 'S', 9, 'D', 'A', 'D', 3, 'S'],[6, 'D', 6, 'H', 5, 'D', 5, 'S', 'T', 'C'],[3, 'D', 7, 'D', 'Q', 'S', 9, 'D', 'Q', 'D'],[4, 'S', 6, 'C', 8, 'S', 3, 'S', 7, 'S'],['A', 'D', 'K', 'S', 2, 'D', 7, 'D', 7, 'C'],['K', 'C', 'Q', 'H', 'J', 'C', 'A', 'C', 'Q', 'D'],[5, 'D', 8, 'D', 'Q', 'S', 7, 'H', 7, 'D'],['J', 'S', 'A', 'H', 8, 'S', 5, 'H', 3, 'D'],['T', 'D', 3, 'H', 4, 'S', 6, 'C', 'J', 'H'],[4, 'S', 'Q', 'S', 7, 'D', 'A', 'S', 9, 'H'],['J', 'S', 'K', 'S', 6, 'D', 'T', 'C', 5, 'C'],[2, 'D', 5, 'C', 6, 'H', 'T', 'C', 4, 'D'],['Q', 'H', 3, 'D', 9, 'H', 8, 'S', 6, 'C'],[6, 'D', 7, 'H', 'T', 'C', 'T', 'H', 5, 'S'],['J', 'D', 5, 'C', 9, 'C', 'K', 'S', 'K', 'D'],[8, 'D', 'T', 'D', 'Q', 'H', 6, 'S', 4, 'S'],[6, 'C', 8, 'S', 'K', 'C', 5, 'C', 'T', 'C'],[5, 'S', 3, 'D', 'K', 'S', 'A', 'C', 4, 'S'],[7, 'D', 'Q', 'D', 4, 'C', 'T', 'H', 2, 'S'],['T', 'S', 8, 'H', 9, 'S', 6, 'S', 7, 'S'],['Q', 'H', 3, 'C', 'A', 'H', 7, 'H', 8, 'C'],[4, 'C', 8, 'C', 'T', 'S', 'J', 'S', 'Q', 'C'],[3, 'D', 7, 'D', 5, 'D', 7, 'S', 'J', 'H'],[8, 'S', 7, 'S', 9, 'D', 'Q', 'C', 'A', 'C'],[7, 'C', 6, 'D', 2, 'H', 'J', 'H', 'K', 'C'],['J', 'S', 'K', 'D', 3, 'C', 6, 'S', 4, 'S'],[7, 'C', 'A', 'H', 'Q', 'C', 'K', 'S', 5, 'H'],['K', 'S', 6, 'S', 4, 'H', 'J', 'D', 'Q', 'S'],['T', 'C', 8, 'H', 'K', 'C', 6, 'H', 'A', 'S'],['K', 'H', 7, 'C', 'T', 'C', 6, 'S', 'T', 'D'],['J', 'C', 5, 'C', 7, 'D', 'A', 'H', 3, 'S'],[3, 'H', 4, 'C', 4, 'H', 'T', 'C', 'T', 'H'],[6, 'S', 7, 'H', 6, 'D', 9, 'C', 'Q', 'H'],[7, 'D', 5, 'H', 4, 'S', 8, 'C', 'J', 'S'],[4, 'D', 3, 'D', 8, 'S', 'Q', 'H', 'K', 'C'],[3, 'H', 6, 'S', 'A', 'D', 7, 'H', 3, 'S'],['Q', 'C', 8, 'S', 4, 'S', 7, 'S', 'J', 'S'],[3, 'S', 'J', 'D', 'K', 'H', 'T', 'H', 6, 'H'],['Q', 'S', 9, 'C', 6, 'C', 2, 'D', 'Q', 'D'],[4, 'S', 'Q', 'H', 4, 'D', 5, 'H', 'K', 'C'],[7, 'D', 6, 'D', 8, 'D', 'T', 'H', 5, 'S'],['T', 'D', 'A', 'D', 6, 'S', 7, 'H', 'K', 'D'],['K', 'H', 9, 'H', 5, 'S', 'K', 'C', 'J', 'C'],[3, 'H', 'Q', 'C', 'A', 'S', 'T', 'S', 4, 'S'],['Q', 'D', 'K', 'S', 9, 'C', 7, 'S', 'K', 'C'],['T', 'S', 6, 'S', 'Q', 'C', 6, 'C', 'T', 'H'],['T', 'C', 9, 'D', 5, 'C', 5, 'D', 'K', 'D'],['J', 'S', 3, 'S', 4, 'H', 'K', 'D', 4, 'C'],['Q', 'D', 6, 'D', 9, 'S', 'J', 'C', 9, 'D'],[8, 'S', 'J', 'S', 6, 'D', 4, 'H', 'J', 'H'],[6, 'H', 6, 'S', 6, 'C', 'K', 'S', 'K', 'H'],['A', 'C', 7, 'D', 5, 'D', 'T', 'C', 9, 'S'],['K', 'H', 6, 'S', 'Q', 'D', 6, 'H', 'A', 'S'],['A', 'S', 7, 'H', 6, 'D', 'Q', 'H', 8, 'D'],['T', 'H', 2, 'S', 'K', 'H', 5, 'C', 5, 'H'],[4, 'C', 7, 'C', 3, 'D', 'Q', 'C', 'T', 'C'],[4, 'S', 'K', 'H', 8, 'C', 2, 'D', 'J', 'S'],[6, 'H', 5, 'D', 7, 'S', 5, 'H', 9, 'C'],[9, 'H', 'J', 'H', 8, 'S', 'T', 'H', 7, 'H'],['A', 'S', 'J', 'S', 2, 'S', 'Q', 'D', 'K', 'H'],[8, 'H', 4, 'S', 'A', 'C', 8, 'D', 8, 'S'],[3, 'H', 4, 'C', 'T', 'D', 'K', 'D', 8, 'C'],['J', 'C', 5, 'C', 'Q', 'S', 2, 'D', 'J', 'D'],['T', 'S', 7, 'D', 5, 'D', 6, 'C', 2, 'C'],['Q', 'S', 2, 'H', 3, 'C', 'A', 'H', 'K', 'S'],[4, 'S', 7, 'C', 9, 'C', 7, 'D', 'J', 'H'],[6, 'C', 5, 'C', 8, 'H', 9, 'D', 'Q', 'D'],[2, 'S', 'T', 'D', 7, 'S', 6, 'D', 9, 'C'],[9, 'S', 'Q', 'S', 'K', 'H', 'Q', 'H', 5, 'C'],['J', 'C', 6, 'S', 9, 'C', 'Q', 'H', 'J', 'H'],[8, 'D', 7, 'S', 'J', 'S', 'K', 'H', 2, 'H'],[8, 'D', 5, 'H', 'T', 'H', 'K', 'C', 4, 'D'],[4, 'S', 3, 'S', 6, 'S', 3, 'D', 'Q', 'S'],[2, 'D', 'J', 'D', 4, 'C', 'T', 'D', 7, 'C'],[6, 'D', 'T', 'H', 7, 'S', 'J', 'C', 'A', 'H'],['Q', 'S', 7, 'S', 4, 'C', 'T', 'H', 9, 'D'],['T', 'S', 'A', 'D', 4, 'D', 3, 'H', 6, 'H'],[2, 'D', 3, 'H', 7, 'D', 'J', 'D', 3, 'D'],['A', 'S', 2, 'S', 9, 'C', 'Q', 'C', 8, 'S'],[4, 'H', 9, 'H', 9, 'C', 2, 'C', 7, 'S'],['J', 'H', 'K', 'D', 5, 'C', 5, 'D', 6, 'H'],['T', 'C', 9, 'H', 8, 'H', 'J', 'C', 3, 'C'],[9, 'S', 8, 'D', 'K', 'S', 'A', 'D', 'K', 'C'],['T', 'S', 5, 'H', 'J', 'D', 'Q', 'S', 'Q', 'H'],['Q', 'C', 8, 'D', 5, 'D', 'K', 'H', 'A', 'H'],[5, 'D', 'A', 'S', 8, 'S', 6, 'S', 4, 'C'],['A', 'H', 'Q', 'C', 'Q', 'D', 'T', 'H', 7, 'H'],[3, 'H', 4, 'H', 7, 'D', 6, 'S', 4, 'S'],[9, 'H', 'A', 'S', 8, 'H', 'J', 'S', 9, 'D'],['J', 'D', 8, 'C', 2, 'C', 9, 'D', 7, 'D'],[5, 'H', 5, 'S', 9, 'S', 'J', 'C', 'K', 'D'],['K', 'D', 9, 'C', 4, 'S', 'Q', 'D', 'A', 'H'],[7, 'C', 'A', 'D', 9, 'D', 'A', 'C', 'T', 'D'],[6, 'S', 4, 'H', 4, 'S', 9, 'C', 8, 'D'],['K', 'S', 'T', 'C', 9, 'D', 'J', 'H', 7, 'C'],[5, 'S', 'J', 'C', 5, 'H', 4, 'S', 'Q', 'H'],['A', 'C', 2, 'C', 'J', 'S', 2, 'S', 9, 'S'],[8, 'C', 5, 'H', 'A', 'S', 'Q', 'D', 'A', 'D'],[5, 'C', 7, 'D', 8, 'S', 'Q', 'C', 'T', 'D'],['J', 'C', 4, 'C', 8, 'D', 5, 'C', 'K', 'H'],['Q', 'S', 4, 'D', 6, 'H', 2, 'H', 2, 'C'],['T', 'H', 4, 'S', 2, 'D', 'K', 'C', 3, 'H'],['Q', 'D', 'A', 'C', 7, 'H', 'A', 'D', 9, 'D'],['K', 'H', 'Q', 'D', 'A', 'S', 8, 'H', 'T', 'H'],['K', 'C', 8, 'D', 7, 'S', 'Q', 'H', 8, 'C'],['J', 'C', 6, 'C', 7, 'D', 8, 'C', 'K', 'H'],['A', 'D', 'Q', 'S', 2, 'H', 6, 'S', 2, 'D'],['J', 'C', 'K', 'H', 2, 'D', 7, 'D', 'J', 'S'],['Q', 'C', 5, 'H', 4, 'C', 5, 'D', 'A', 'D'],['T', 'S', 3, 'S', 'A', 'D', 4, 'S', 'T', 'D'],[2, 'D', 'T', 'H', 6, 'S', 9, 'H', 'J', 'H'],[9, 'H', 2, 'D', 'Q', 'S', 2, 'C', 4, 'S'],[3, 'D', 'K', 'H', 'A', 'S', 'A', 'C', 9, 'D'],['K', 'H', 6, 'S', 8, 'H', 4, 'S', 'K', 'D'],[7, 'D', 9, 'D', 'T', 'S', 'Q', 'D', 'Q', 'C'],['J', 'H', 5, 'H', 'A', 'H', 'K', 'S', 'A', 'S'],['A', 'D', 'J', 'C', 'Q', 'C', 5, 'S', 'K', 'H'],[5, 'D', 7, 'D', 6, 'D', 'K', 'S', 'K', 'D'],[3, 'D', 7, 'C', 4, 'D', 'J', 'D', 3, 'S'],['A', 'C', 'J', 'S', 8, 'D', 5, 'H', 9, 'C'],[3, 'H', 4, 'H', 4, 'D', 'T', 'S', 2, 'C'],[6, 'H', 'K', 'S', 'K', 'H', 9, 'D', 7, 'C'],[2, 'S', 6, 'S', 8, 'S', 2, 'H', 3, 'D'],[6, 'H', 'A', 'C', 'J', 'S', 7, 'S', 3, 'S'],['T', 'D', 8, 'H', 3, 'H', 4, 'H', 'T', 'H'],[9, 'H', 'T', 'C', 'Q', 'C', 'K', 'C', 5, 'C'],['K', 'S', 6, 'H', 4, 'H', 'A', 'C', 8, 'S'],['T', 'C', 7, 'D', 'Q', 'H', 4, 'S', 'J', 'C'],['T', 'S', 6, 'D', 6, 'C', 'A', 'C', 'K', 'H'],['Q', 'H', 7, 'D', 7, 'C', 'J', 'H', 'Q', 'S'],['Q', 'D', 'T', 'H', 3, 'H', 5, 'D', 'K', 'S'],[3, 'D', 5, 'S', 8, 'D', 'J', 'S', 4, 'C'],[2, 'C', 'K', 'S', 7, 'H', 9, 'C', 4, 'H'],[5, 'H', 8, 'S', 4, 'H', 'T', 'D', 2, 'C'],[3, 'S', 'Q', 'D', 'Q', 'C', 3, 'H', 'K', 'C'],['Q', 'C', 'J', 'S', 'K', 'D', 9, 'C', 'A', 'D'],[5, 'S', 9, 'D', 7, 'D', 7, 'H', 'T', 'S'],[8, 'C', 'J', 'C', 'K', 'H', 7, 'C', 7, 'S'],[6, 'C', 'T', 'S', 2, 'C', 'Q', 'D', 'T', 'H'],[5, 'S', 9, 'D', 'T', 'H', 3, 'C', 7, 'S'],['Q', 'H', 8, 'S', 9, 'C', 2, 'H', 5, 'H'],[5, 'D', 9, 'H', 6, 'H', 2, 'S', 'J', 'S'],['K', 'H', 3, 'H', 7, 'C', 2, 'H', 5, 'S'],['J', 'D', 5, 'D', 5, 'S', 2, 'C', 'T', 'C'],[2, 'S', 6, 'S', 6, 'C', 3, 'C', 8, 'S'],[4, 'D', 'K', 'H', 8, 'H', 4, 'H', 2, 'D'],['K', 'S', 3, 'H', 5, 'C', 2, 'S', 9, 'H'],[3, 'S', 2, 'D', 'T', 'D', 7, 'H', 8, 'S'],[6, 'H', 'J', 'D', 'K', 'C', 9, 'C', 8, 'D'],[6, 'S', 'Q', 'D', 'J', 'H', 7, 'C', 9, 'H'],[5, 'H', 8, 'S', 8, 'H', 'T', 'H', 'T', 'D'],['Q', 'S', 7, 'S', 'T', 'D', 7, 'D', 'T', 'S'],['J', 'C', 'K', 'D', 7, 'C', 3, 'C', 2, 'C'],[3, 'C', 'J', 'D', 8, 'S', 4, 'H', 2, 'D'],[2, 'S', 'T', 'D', 'A', 'S', 4, 'D', 'A', 'C'],['A', 'H', 'K', 'S', 6, 'C', 4, 'C', 4, 'S'],[7, 'D', 8, 'C', 9, 'H', 6, 'H', 'A', 'S'],[5, 'S', 3, 'C', 9, 'S', 2, 'C', 'Q', 'S'],['K', 'D', 4, 'D', 4, 'S', 'A', 'C', 5, 'D'],[2, 'D', 'T', 'S', 2, 'C', 'J', 'S', 'K', 'H'],['Q', 'H', 5, 'D', 8, 'C', 'A', 'S', 'K', 'C'],['K', 'D', 3, 'H', 6, 'C', 'T', 'H', 8, 'S'],[7, 'S', 'K', 'H', 6, 'H', 9, 'S', 'A', 'C'],[6, 'H', 7, 'S', 6, 'C', 'Q', 'S', 'A', 'H'],[2, 'S', 2, 'H', 4, 'H', 5, 'D', 5, 'H'],[5, 'H', 'J', 'C', 'Q', 'D', 2, 'C', 2, 'S'],['J', 'D', 'A', 'S', 'Q', 'C', 6, 'S', 7, 'D'],[6, 'C', 'T', 'C', 'A', 'S', 'K', 'D', 8, 'H'],[9, 'D', 2, 'C', 7, 'D', 'J', 'H', 9, 'S'],[2, 'H', 4, 'C', 6, 'C', 'A', 'H', 8, 'S'],['T', 'D', 3, 'H', 'T', 'H', 7, 'C', 'T', 'S'],['K', 'D', 4, 'S', 'T', 'S', 6, 'C', 'Q', 'H'],[8, 'D', 9, 'D', 9, 'C', 'A', 'H', 7, 'D'],[6, 'D', 'J', 'S', 5, 'C', 'Q', 'D', 'Q', 'C'],[9, 'C', 5, 'D', 8, 'C', 2, 'H', 'K', 'D'],[3, 'C', 'Q', 'H', 'J', 'H', 'A', 'D', 6, 'S'],['A', 'H', 'K', 'C', 8, 'S', 6, 'D', 6, 'H'],[3, 'D', 7, 'C', 4, 'C', 7, 'S', 5, 'S'],[3, 'S', 6, 'S', 5, 'H', 'J', 'C', 3, 'C'],['Q', 'H', 7, 'C', 5, 'H', 3, 'C', 3, 'S'],[8, 'C', 'T', 'S', 4, 'C', 'K', 'D', 9, 'C'],['Q', 'D', 3, 'S', 7, 'S', 5, 'H', 7, 'H'],['Q', 'H', 'J', 'C', 7, 'C', 8, 'C', 'K', 'D'],[3, 'C', 'K', 'D', 'K', 'H', 2, 'S', 4, 'C'],['T', 'S', 'A', 'C', 6, 'S', 2, 'C', 7, 'C'],[2, 'C', 'K', 'H', 3, 'C', 4, 'C', 6, 'H'],[4, 'D', 5, 'H', 5, 'S', 7, 'S', 'Q', 'D'],[4, 'D', 7, 'C', 8, 'S', 'Q', 'D', 'T', 'S'],[9, 'D', 'K', 'S', 6, 'H', 'K', 'D', 3, 'C'],['Q', 'S', 4, 'D', 'T', 'S', 7, 'S', 4, 'C'],[3, 'H', 'Q', 'D', 8, 'D', 9, 'S', 'T', 'C'],['T', 'S', 'Q', 'H', 'A', 'C', 6, 'S', 3, 'C'],[9, 'H', 9, 'D', 'Q', 'S', 8, 'S', 6, 'H'],[3, 'S', 7, 'S', 5, 'D', 4, 'S', 'J', 'S'],[2, 'D', 6, 'C', 'Q', 'H', 6, 'S', 'T', 'H'],[4, 'C', 4, 'H', 'A', 'S', 'J', 'S', 5, 'D'],[3, 'D', 'T', 'S', 9, 'C', 'A', 'C', 8, 'S'],[6, 'S', 9, 'C', 7, 'C', 3, 'S', 5, 'C'],['Q', 'S', 'A', 'D', 'A', 'S', 6, 'H', 3, 'C'],[9, 'S', 8, 'C', 7, 'H', 3, 'H', 6, 'S'],[7, 'C', 'A', 'S', 9, 'H', 'J', 'D', 'K', 'H'],[3, 'D', 3, 'H', 7, 'S', 4, 'D', 6, 'C'],[7, 'C', 'A', 'C', 2, 'H', 9, 'C', 'T', 'H'],[4, 'H', 5, 'S', 3, 'H', 'A', 'C', 'T', 'C'],['T', 'H', 9, 'C', 9, 'H', 9, 'S', 8, 'D'],[8, 'D', 9, 'H', 5, 'H', 4, 'D', 6, 'C'],[2, 'H', 'Q', 'D', 6, 'S', 5, 'D', 3, 'S'],[4, 'C', 5, 'C', 'J', 'D', 'Q', 'S', 4, 'D'],[3, 'H', 'T', 'H', 'A', 'C', 'Q', 'H', 8, 'C'],['Q', 'C', 5, 'S', 3, 'C', 7, 'H', 'A', 'D'],[4, 'C', 'K', 'S', 4, 'H', 'J', 'D', 6, 'D'],['Q', 'S', 'A', 'H', 3, 'H', 'K', 'S', 9, 'H'],[2, 'S', 'J', 'S', 'J', 'H', 5, 'H', 2, 'H'],[2, 'H', 5, 'S', 'T', 'H', 6, 'S', 'T', 'S'],[3, 'S', 'K', 'S', 3, 'C', 5, 'H', 'J', 'S'],[2, 'D', 9, 'S', 7, 'H', 3, 'D', 'K', 'C'],['J', 'H', 6, 'D', 7, 'D', 'J', 'S', 'T', 'D'],['A', 'C', 'J', 'S', 8, 'H', 2, 'C', 8, 'C'],['J', 'H', 'J', 'C', 2, 'D', 'T', 'H', 7, 'S'],[5, 'D', 9, 'S', 8, 'H', 2, 'H', 3, 'D'],['T', 'C', 'A', 'H', 'J', 'C', 'K', 'D', 9, 'C'],[9, 'D', 'Q', 'D', 'J', 'C', 2, 'H', 6, 'D'],['K', 'H', 'T', 'S', 9, 'S', 'Q', 'H', 'T', 'H'],[2, 'C', 8, 'D', 4, 'S', 'J', 'D', 5, 'H'],[3, 'H', 'T', 'H', 'T', 'C', 9, 'C', 'K', 'C'],['A', 'S', 3, 'D', 9, 'H', 7, 'D', 4, 'D'],['T', 'H', 'K', 'H', 2, 'H', 7, 'S', 3, 'H'],[4, 'H', 7, 'S', 'K', 'S', 2, 'S', 'J', 'S'],['T', 'S', 8, 'S', 2, 'H', 'Q', 'D', 8, 'D'],[5, 'S', 6, 'H', 'J', 'H', 'K', 'S', 8, 'H'],[2, 'S', 'Q', 'C', 'A', 'C', 6, 'S', 3, 'S'],['J', 'C', 'A', 'S', 'A', 'D', 'Q', 'S', 8, 'H'],[6, 'C', 'K', 'H', 4, 'C', 4, 'D', 'Q', 'D'],[2, 'S', 3, 'D', 'T', 'S', 'T', 'D', 9, 'S'],['K', 'S', 6, 'S', 'Q', 'S', 5, 'C', 8, 'D'],[3, 'C', 6, 'D', 4, 'S', 'Q', 'C', 'K', 'C'],['J', 'H', 'Q', 'D', 'T', 'H', 'K', 'H', 'A', 'D'],[9, 'H', 'A', 'H', 4, 'D', 'K', 'S', 2, 'S'],[8, 'D', 'J', 'H', 'J', 'C', 7, 'C', 'Q', 'S'],[2, 'D', 6, 'C', 'T', 'H', 3, 'C', 8, 'H'],['Q', 'D', 'Q', 'H', 2, 'S', 3, 'S', 'K', 'S'],[6, 'H', 5, 'D', 9, 'S', 4, 'C', 'T', 'S'],['T', 'D', 'J', 'S', 'Q', 'D', 9, 'D', 'J', 'D'],[5, 'H', 8, 'H', 'K', 'H', 8, 'S', 'K', 'S'],[7, 'C', 'T', 'D', 'A', 'D', 4, 'S', 'K', 'D'],[2, 'C', 7, 'C', 'J', 'C', 5, 'S', 'A', 'S'],[6, 'C', 7, 'D', 8, 'S', 5, 'H', 9, 'C'],[6, 'S', 'Q', 'D', 9, 'S', 'T', 'S', 'K', 'H'],['Q', 'S', 5, 'S', 'Q', 'H', 3, 'C', 'K', 'C'],[7, 'D', 3, 'H', 3, 'C', 'K', 'D', 5, 'C'],['A', 'S', 'J', 'H', 7, 'H', 6, 'H', 'J', 'D'],[9, 'D', 5, 'C', 9, 'H', 'K', 'C', 8, 'H'],['K', 'S', 4, 'S', 'A', 'D', 4, 'D', 2, 'S'],[3, 'S', 'J', 'D', 'Q', 'D', 8, 'D', 2, 'S'],[7, 'C', 5, 'S', 6, 'S', 5, 'H', 'T', 'S'],[6, 'D', 9, 'S', 'K', 'C', 'T', 'D', 3, 'S'],[6, 'H', 'Q', 'D', 'J', 'D', 5, 'C', 8, 'D'],[5, 'H', 9, 'D', 'T', 'S', 'K', 'D', 8, 'D'],[6, 'H', 'T', 'D', 'Q', 'C', 4, 'C', 7, 'D'],[6, 'D', 4, 'S', 'J', 'D', 9, 'D', 'A', 'H'],[9, 'S', 'A', 'S', 'T', 'D', 9, 'H', 'Q', 'D'],[2, 'D', 5, 'S', 2, 'H', 9, 'C', 6, 'H'],[9, 'S', 'T', 'D', 'Q', 'C', 7, 'D', 'T', 'C'],[3, 'S', 2, 'H', 'K', 'S', 'T', 'S', 2, 'C'],[9, 'C', 8, 'S', 'J', 'S', 9, 'D', 7, 'D'],[3, 'C', 'K', 'C', 6, 'D', 5, 'D', 6, 'C'],[6, 'H', 8, 'S', 'A', 'S', 7, 'S', 'Q', 'S'],['J', 'H', 9, 'S', 2, 'H', 8, 'D', 4, 'C'],[8, 'H', 9, 'H', 'A', 'D', 'T', 'H', 'K', 'H'],['Q', 'C', 'A', 'S', 2, 'S', 'J', 'S', 5, 'C'],[6, 'H', 'K', 'D', 3, 'H', 7, 'H', 2, 'C'],['Q', 'D', 8, 'H', 2, 'S', 8, 'D', 3, 'S'],[6, 'D', 'A', 'H', 2, 'C', 'T', 'C', 5, 'C'],['J', 'D', 'J', 'S', 'T', 'S', 8, 'S', 3, 'H'],[5, 'D', 'T', 'D', 'K', 'C', 'J', 'C', 6, 'H'],[6, 'S', 'Q', 'S', 'T', 'C', 3, 'H', 5, 'D'],['A', 'H', 'J', 'C', 7, 'C', 7, 'D', 4, 'H'],[7, 'C', 5, 'D', 8, 'H', 9, 'C', 2, 'H'],[9, 'H', 'J', 'H', 'K', 'H', 5, 'S', 2, 'C'],[9, 'C', 7, 'H', 6, 'S', 'T', 'H', 3, 'S'],['Q', 'C', 'Q', 'D', 4, 'C', 'A', 'C', 'J', 'D'],[2, 'H', 5, 'D', 9, 'S', 7, 'D', 'K', 'C'],[3, 'S', 'Q', 'S', 2, 'D', 'A', 'S', 'K', 'H'],[2, 'S', 4, 'S', 2, 'H', 7, 'D', 5, 'C'],['T', 'D', 'T', 'H', 'Q', 'H', 9, 'S', 4, 'D'],[6, 'D', 3, 'S', 'T', 'S', 6, 'H', 4, 'H'],['K', 'S', 9, 'D', 8, 'H', 5, 'S', 2, 'D'],[9, 'H', 'K', 'S', 4, 'H', 3, 'S', 5, 'C'],[5, 'D', 'K', 'H', 6, 'H', 6, 'S', 'J', 'S'],['K', 'C', 'A', 'S', 8, 'C', 4, 'C', 'J', 'C'],['K', 'H', 'Q', 'C', 'T', 'H', 'Q', 'D', 'A', 'H'],[6, 'S', 'K', 'H', 9, 'S', 2, 'C', 5, 'H'],['T', 'C', 3, 'C', 7, 'H', 'J', 'C', 4, 'D'],['J', 'D', 4, 'S', 6, 'S', 5, 'S', 8, 'D'],[7, 'H', 7, 'S', 4, 'D', 4, 'C', 2, 'H'],[7, 'H', 9, 'H', 5, 'D', 'K', 'H', 9, 'C'],[7, 'C', 'T', 'S', 'T', 'C', 7, 'S', 5, 'H'],[4, 'C', 8, 'D', 'Q', 'C', 'T', 'S', 4, 'S'],[9, 'H', 3, 'D', 'A', 'D', 'J', 'S', 7, 'C'],[8, 'C', 'Q', 'S', 5, 'C', 5, 'D', 3, 'H'],['J', 'S', 'A', 'H', 'K', 'C', 4, 'S', 9, 'D'],['T', 'S', 'J', 'D', 8, 'S', 'Q', 'S', 'T', 'H'],['J', 'H', 'K', 'H', 2, 'D', 'Q', 'D', 'J', 'S'],['J', 'D', 'Q', 'C', 5, 'D', 6, 'S', 9, 'H'],[3, 'S', 2, 'C', 8, 'H', 9, 'S', 'T', 'S'],[2, 'S', 4, 'C', 'A', 'D', 7, 'H', 'J', 'C'],[5, 'C', 2, 'D', 6, 'D', 4, 'H', 3, 'D'],[7, 'S', 'J', 'S', 2, 'C', 4, 'H', 8, 'C'],['A', 'D', 'Q', 'D', 9, 'C', 3, 'S', 'T', 'D'],['J', 'D', 'T', 'S', 4, 'C', 6, 'H', 9, 'H'],[7, 'D', 'Q', 'D', 6, 'D', 3, 'C', 'A', 'S'],['A', 'S', 7, 'C', 4, 'C', 6, 'S', 5, 'D'],[5, 'S', 5, 'C', 'J', 'S', 'Q', 'C', 4, 'S'],['K', 'D', 6, 'S', 9, 'S', 7, 'C', 3, 'C'],[5, 'S', 7, 'D', 'J', 'H', 'Q', 'D', 'J', 'S'],[4, 'S', 7, 'S', 'J', 'H', 2, 'C', 8, 'S'],[5, 'D', 7, 'H', 3, 'D', 'Q', 'H', 'A', 'D'],['T', 'D', 6, 'H', 2, 'H', 8, 'D', 4, 'H'],[2, 'D', 7, 'C', 'A', 'D', 'K', 'H', 5, 'D'],['T', 'S', 3, 'S', 5, 'H', 2, 'C', 'Q', 'D'],['A', 'H', 2, 'S', 5, 'C', 'K', 'H', 'T', 'D'],['K', 'C', 4, 'D', 8, 'C', 5, 'D', 'A', 'S'],[6, 'C', 2, 'H', 2, 'S', 9, 'H', 7, 'C'],['K', 'D', 'J', 'S', 'Q', 'C', 'T', 'S', 'Q', 'S'],['K', 'H', 'J', 'H', 2, 'C', 5, 'D', 'A', 'D'],[3, 'S', 5, 'H', 'K', 'C', 6, 'C', 9, 'H'],[3, 'H', 2, 'H', 'A', 'D', 7, 'D', 7, 'S'],[7, 'S', 'J', 'S', 'J', 'H', 'K', 'D', 8, 'S'],[7, 'D', 2, 'S', 9, 'H', 7, 'C', 2, 'H'],[9, 'H', 2, 'D', 8, 'D', 'Q', 'C', 6, 'S'],['A', 'D', 'A', 'S', 8, 'H', 5, 'H', 6, 'C'],[2, 'S', 7, 'H', 6, 'C', 6, 'D', 7, 'D'],[8, 'C', 5, 'D', 9, 'D', 'J', 'C', 3, 'C'],[7, 'C', 9, 'C', 7, 'H', 'J', 'D', 2, 'H'],['K', 'D', 3, 'S', 'K', 'H', 'A', 'D', 4, 'S'],['Q', 'H', 'A', 'S', 9, 'H', 4, 'D', 'J', 'D'],['K', 'S', 'K', 'D', 'T', 'S', 'K', 'H', 5, 'H'],[4, 'C', 8, 'H', 5, 'S', 3, 'S', 3, 'D'],[7, 'D', 'T', 'D', 'A', 'D', 7, 'S', 'K', 'C'],['J', 'S', 8, 'S', 5, 'S', 'J', 'C', 8, 'H'],['T', 'H', 9, 'C', 4, 'D', 5, 'D', 'K', 'C'],[7, 'C', 5, 'S', 9, 'C', 'Q', 'D', 2, 'C'],['Q', 'H', 'J', 'S', 5, 'H', 8, 'D', 'K', 'H'],['T', 'D', 2, 'S', 'K', 'S', 3, 'D', 'A', 'D'],['K', 'C', 7, 'S', 'T', 'C', 3, 'C', 5, 'D'],[4, 'C', 2, 'S', 'A', 'D', 'Q', 'S', 6, 'C'],[9, 'S', 'Q', 'D', 'T', 'H', 'Q', 'H', 5, 'C'],[8, 'C', 'A', 'D', 'Q', 'S', 2, 'D', 2, 'S'],['K', 'C', 'J', 'D', 'K', 'S', 6, 'C', 'J', 'C'],[8, 'D', 4, 'D', 'J', 'S', 2, 'H', 5, 'D'],['Q', 'D', 7, 'S', 7, 'D', 'Q', 'H', 'T', 'S'],[6, 'S', 7, 'H', 3, 'S', 8, 'C', 8, 'S'],[9, 'D', 'Q', 'S', 8, 'H', 6, 'C', 9, 'S'],[4, 'S', 'T', 'C', 2, 'S', 5, 'C', 'Q', 'D'],[4, 'D', 'Q', 'S', 6, 'D', 'T', 'H', 6, 'S'],[3, 'S', 5, 'C', 9, 'D', 6, 'H', 8, 'D'],[4, 'C', 7, 'D', 'T', 'C', 7, 'C', 'T', 'D'],['A', 'H', 6, 'S', 'A', 'S', 7, 'H', 5, 'S'],['K', 'D', 3, 'H', 5, 'H', 'A', 'C', 4, 'C'],[8, 'D', 8, 'S', 'A', 'H', 'K', 'S', 'Q', 'S'],[2, 'C', 'A', 'D', 6, 'H', 7, 'D', 5, 'D'],[6, 'H', 9, 'H', 9, 'S', 2, 'H', 'Q', 'S'],[8, 'S', 9, 'C', 5, 'D', 2, 'D', 'K', 'D'],['T', 'S', 'Q', 'C', 5, 'S', 'J', 'H', 7, 'D'],[7, 'S', 'T', 'H', 9, 'S', 9, 'H', 'A', 'C'],[7, 'H', 3, 'H', 6, 'S', 'K', 'C', 4, 'D'],[6, 'D', 5, 'C', 4, 'S', 'Q', 'D', 'T', 'S'],['T', 'D', 2, 'S', 7, 'C', 'Q', 'D', 3, 'H'],['J', 'H', 9, 'D', 4, 'H', 7, 'S', 7, 'H'],['K', 'S', 3, 'D', 4, 'H', 5, 'H', 'T', 'C'],[2, 'S', 'A', 'S', 2, 'D', 6, 'D', 7, 'D'],[8, 'H', 3, 'C', 7, 'H', 'T', 'D', 3, 'H'],['A', 'D', 'K', 'C', 'T', 'H', 9, 'C', 'K', 'H'],['T', 'C', 4, 'C', 2, 'C', 9, 'S', 9, 'D'],[9, 'C', 5, 'C', 2, 'H', 'J', 'D', 3, 'C'],[3, 'H', 'A', 'C', 'T', 'S', 5, 'D', 'A', 'D'],[8, 'D', 6, 'H', 'Q', 'C', 6, 'S', 8, 'C'],[2, 'S', 'T', 'S', 3, 'S', 'J', 'D', 7, 'H'],[8, 'S', 'Q', 'H', 4, 'C', 5, 'S', 8, 'D'],['A', 'C', 4, 'S', 6, 'C', 3, 'C', 'K', 'H'],[3, 'D', 7, 'C', 2, 'D', 8, 'S', 2, 'H'],[4, 'H', 6, 'C', 8, 'S', 'T', 'H', 2, 'H'],[4, 'S', 8, 'H', 9, 'S', 3, 'H', 7, 'S'],[7, 'C', 4, 'C', 9, 'C', 2, 'C', 5, 'C'],['A', 'S', 5, 'D', 'K', 'D', 4, 'D', 'Q', 'H'],[9, 'H', 4, 'H', 'T', 'S', 'A', 'S', 7, 'D'],[8, 'D', 5, 'D', 9, 'S', 8, 'C', 2, 'H'],['Q', 'C', 'K', 'D', 'A', 'C', 'A', 'D', 2, 'H'],[7, 'S', 'A', 'S', 3, 'S', 2, 'D', 9, 'S'],[2, 'H', 'Q', 'C', 8, 'H', 'T', 'C', 6, 'D'],['Q', 'D', 'Q', 'S', 5, 'D', 'K', 'H', 3, 'C'],['T', 'H', 'J', 'D', 'Q', 'S', 4, 'C', 2, 'S'],[5, 'S', 'A', 'D', 7, 'H', 3, 'S', 'A', 'S'],[7, 'H', 'J', 'S', 3, 'D', 6, 'C', 3, 'S'],[6, 'D', 'A', 'S', 9, 'S', 'A', 'C', 'Q', 'S'],[9, 'C', 'T', 'S', 'A', 'S', 8, 'C', 'T', 'C'],[8, 'S', 6, 'H', 9, 'D', 8, 'D', 6, 'C'],[4, 'D', 'J', 'D', 9, 'C', 'K', 'C', 7, 'C'],[6, 'D', 'K', 'S', 3, 'S', 8, 'C', 'A', 'S'],[3, 'H', 6, 'S', 'T', 'C', 8, 'D', 'T', 'S'],[3, 'S', 'K', 'C', 9, 'S', 7, 'C', 'A', 'S'],[8, 'C', 'Q', 'C', 4, 'H', 4, 'S', 8, 'S'],[6, 'C', 3, 'S', 'T', 'C', 'A', 'H', 'A', 'C'],[4, 'D', 7, 'D', 5, 'C', 'A', 'S', 2, 'H'],[6, 'S', 'T', 'S', 'Q', 'C', 'A', 'D', 'T', 'C'],['Q', 'D', 'Q', 'C', 8, 'S', 4, 'S', 'T', 'H'],[3, 'D', 'A', 'H', 'T', 'S', 'J', 'H', 4, 'H'],[5, 'C', 2, 'D', 9, 'S', 2, 'C', 3, 'H'],[3, 'C', 9, 'D', 'Q', 'D', 'Q', 'H', 7, 'D'],['K', 'C', 9, 'H', 6, 'C', 'K', 'D', 7, 'S'],[3, 'C', 4, 'D', 'A', 'S', 'T', 'C', 2, 'D'],[3, 'D', 'J', 'S', 4, 'D', 9, 'D', 'K', 'S'],[7, 'D', 'T', 'H', 'Q', 'C', 3, 'H', 3, 'C'],[8, 'D', 5, 'S', 2, 'H', 9, 'D', 3, 'H'],[8, 'C', 4, 'C', 4, 'H', 3, 'C', 'T', 'H'],['J', 'C', 'T', 'H', 4, 'S', 6, 'S', 'J', 'D'],[2, 'D', 4, 'D', 6, 'C', 3, 'D', 4, 'C'],['T', 'S', 3, 'S', 2, 'D', 4, 'H', 'A', 'C'],[2, 'C', 6, 'S', 2, 'H', 'J', 'H', 6, 'H'],['T', 'D', 8, 'S', 'A', 'D', 'T', 'C', 'A', 'H'],['A', 'C', 'J', 'H', 9, 'S', 6, 'S', 7, 'S'],[6, 'C', 'K', 'C', 4, 'S', 'J', 'D', 8, 'D'],[9, 'H', 5, 'S', 7, 'H', 'Q', 'H', 'A', 'H'],['K', 'D', 8, 'D', 'T', 'S', 'J', 'H', 5, 'C'],[5, 'H', 3, 'H', 'A', 'D', 'A', 'S', 'J', 'S'],[2, 'D', 4, 'H', 3, 'D', 6, 'C', 8, 'C'],[7, 'S', 'A', 'D', 5, 'D', 5, 'C', 8, 'S'],['T', 'D', 5, 'D', 7, 'S', 9, 'C', 4, 'S'],[5, 'H', 6, 'C', 8, 'C', 4, 'C', 8, 'S'],['J', 'S', 'Q', 'H', 9, 'C', 'A', 'S', 5, 'C'],['Q', 'S', 'J', 'C', 3, 'D', 'Q', 'C', 7, 'C'],['J', 'C', 9, 'C', 'K', 'H', 'J', 'H', 'Q', 'S'],['Q', 'C', 2, 'C', 'T', 'S', 3, 'D', 'A', 'D'],[5, 'D', 'J', 'H', 'A', 'C', 5, 'C', 9, 'S'],['T', 'S', 4, 'C', 'J', 'D', 8, 'C', 'K', 'S'],['K', 'C', 'A', 'S', 2, 'D', 'K', 'H', 9, 'H'],[2, 'C', 5, 'S', 4, 'D', 3, 'D', 6, 'H'],['T', 'H', 'A', 'H', 2, 'D', 8, 'S', 'J', 'C'],[3, 'D', 8, 'C', 'Q', 'H', 7, 'S', 3, 'S'],[8, 'H', 'Q', 'D', 4, 'H', 'J', 'C', 'A', 'S'],['K', 'H', 'K', 'S', 3, 'C', 9, 'S', 6, 'D'],[9, 'S', 'Q', 'H', 7, 'D', 9, 'C', 4, 'S'],['A', 'C', 7, 'H', 'K', 'H', 4, 'D', 'K', 'D'],['A', 'H', 'A', 'D', 'T', 'H', 6, 'D', 9, 'C'],[9, 'S', 'K', 'D', 'K', 'S', 'Q', 'H', 4, 'H'],['Q', 'D', 6, 'H', 9, 'C', 7, 'C', 'Q', 'S'],[6, 'D', 6, 'S', 9, 'D', 5, 'S', 'J', 'H'],['A', 'H', 8, 'D', 5, 'H', 'Q', 'D', 2, 'H'],['J', 'C', 'K', 'S', 4, 'H', 'K', 'H', 5, 'S'],[5, 'C', 2, 'S', 'J', 'S', 8, 'D', 9, 'C'],[8, 'C', 3, 'D', 'A', 'S', 'K', 'C', 'A', 'H'],['J', 'D', 9, 'S', 2, 'H', 'Q', 'S', 8, 'H'],[5, 'S', 8, 'C', 'T', 'H', 5, 'C', 4, 'C'],['Q', 'C', 'Q', 'S', 8, 'C', 2, 'S', 2, 'C'],[3, 'S', 9, 'C', 4, 'C', 'K', 'S', 'K', 'H'],[2, 'D', 5, 'D', 8, 'S', 'A', 'H', 'A', 'D'],['T', 'D', 2, 'C', 'J', 'S', 'K', 'S', 8, 'C'],['T', 'C', 5, 'S', 5, 'H', 8, 'H', 'Q', 'C'],[9, 'H', 6, 'H', 'J', 'D', 4, 'H', 9, 'S'],[3, 'C', 'J', 'H', 4, 'H', 9, 'H', 'A', 'H'],[4, 'S', 2, 'H', 4, 'C', 8, 'D', 'A', 'C'],[8, 'S', 'T', 'H', 4, 'D', 7, 'D', 6, 'D'],['Q', 'D', 'Q', 'S', 7, 'S', 'T', 'C', 7, 'C'],['K', 'H', 6, 'D', 2, 'D', 'J', 'D', 5, 'H'],['J', 'S', 'Q', 'D', 'J', 'H', 4, 'H', 4, 'S'],[9, 'C', 7, 'S', 'J', 'H', 4, 'S', 3, 'S'],['T', 'S', 'Q', 'C', 8, 'C', 'T', 'C', 4, 'H'],['Q', 'H', 9, 'D', 4, 'D', 'J', 'H', 'Q', 'S'],[3, 'S', 2, 'C', 7, 'C', 6, 'C', 2, 'D'],[4, 'H', 9, 'S', 'J', 'D', 5, 'C', 5, 'H'],['A', 'H', 9, 'D', 'T', 'S', 2, 'D', 4, 'C'],['K', 'S', 'J', 'H', 'T', 'S', 5, 'D', 2, 'D'],['A', 'H', 'J', 'S', 7, 'H', 'A', 'S', 8, 'D'],['J', 'S', 'A', 'H', 8, 'C', 'A', 'D', 'K', 'S'],[5, 'S', 8, 'H', 2, 'C', 6, 'C', 'T', 'H'],[2, 'H', 5, 'D', 'A', 'D', 'A', 'C', 'K', 'S'],[3, 'D', 8, 'H', 'T', 'S', 6, 'H', 'Q', 'C'],[6, 'D', 4, 'H', 'T', 'S', 9, 'C', 5, 'H'],['J', 'S', 'J', 'H', 6, 'S', 'J', 'D', 4, 'C'],['J', 'H', 'Q', 'H', 4, 'H', 2, 'C', 6, 'D'],[3, 'C', 5, 'D', 4, 'C', 'Q', 'S', 'K', 'C'],[6, 'H', 4, 'H', 6, 'C', 7, 'H', 6, 'S'],[2, 'S', 8, 'S', 'K', 'H', 'Q', 'C', 8, 'C'],[3, 'H', 3, 'D', 5, 'D', 'K', 'S', 4, 'H'],['T', 'D', 'A', 'D', 3, 'S', 4, 'D', 'T', 'S'],[5, 'S', 7, 'C', 8, 'S', 7, 'D', 2, 'C'],['K', 'S', 7, 'S', 6, 'C', 8, 'C', 'J', 'S'],[5, 'D', 2, 'H', 3, 'S', 7, 'C', 5, 'C'],['Q', 'D', 5, 'H', 6, 'D', 9, 'C', 9, 'H'],['J', 'S', 2, 'S', 'K', 'D', 9, 'S', 8, 'D'],['T', 'D', 'T', 'S', 'A', 'C', 8, 'C', 9, 'D'],[5, 'H', 'Q', 'D', 2, 'S', 'A', 'C', 8, 'C'],[9, 'H', 'K', 'S', 7, 'C', 4, 'S', 3, 'C'],['K', 'H', 'A', 'S', 3, 'H', 8, 'S', 9, 'C'],['J', 'S', 'Q', 'S', 4, 'S', 'A', 'D', 4, 'D'],['A', 'S', 2, 'S', 'T', 'D', 'A', 'D', 4, 'D'],[9, 'H', 'J', 'C', 4, 'C', 5, 'H', 'Q', 'S'],[5, 'D', 7, 'C', 4, 'H', 'T', 'C', 2, 'D'],[6, 'C', 'J', 'S', 4, 'S', 'K', 'C', 3, 'S'],[4, 'C', 2, 'C', 5, 'D', 'A', 'C', 9, 'H'],[3, 'D', 'J', 'D', 8, 'S', 'Q', 'S', 'Q', 'H'],[2, 'C', 8, 'S', 6, 'H', 3, 'C', 'Q', 'H'],[6, 'D', 'T', 'C', 'K', 'D', 'A', 'C', 'A', 'H'],['Q', 'C', 6, 'C', 3, 'S', 'Q', 'S', 4, 'S'],['A', 'C', 8, 'D', 5, 'C', 'A', 'D', 'K', 'H'],[5, 'S', 4, 'C', 'A', 'C', 'K', 'H', 'A', 'S'],['Q', 'C', 2, 'C', 5, 'C', 8, 'D', 9, 'C'],[8, 'H', 'J', 'D', 3, 'C', 'K', 'H', 8, 'D'],[5, 'C', 9, 'C', 'Q', 'D', 'Q', 'H', 9, 'D'],[7, 'H', 'T', 'S', 2, 'C', 8, 'C', 4, 'S'],['T', 'D', 'J', 'C', 9, 'C', 5, 'H', 'Q', 'H'],['J', 'S', 4, 'S', 2, 'C', 7, 'C', 'T', 'H'],[6, 'C', 'A', 'S', 'K', 'S', 7, 'S', 'J', 'D'],['J', 'H', 7, 'C', 9, 'H', 7, 'H', 'T', 'C'],[5, 'H', 3, 'D', 6, 'D', 5, 'D', 4, 'D'],[2, 'C', 'Q', 'D', 'J', 'H', 2, 'H', 9, 'D'],[5, 'S', 3, 'D', 'T', 'D', 'A', 'D', 'K', 'S'],['J', 'D', 'Q', 'H', 3, 'S', 4, 'D', 'T', 'H'],[7, 'D', 6, 'S', 'Q', 'S', 'K', 'S', 4, 'H'],['T', 'C', 'K', 'S', 5, 'S', 8, 'D', 8, 'H'],['A', 'D', 2, 'S', 2, 'D', 4, 'C', 'J', 'H'],[5, 'S', 'J', 'H', 'T', 'C', 3, 'S', 2, 'D'],['Q', 'S', 9, 'D', 4, 'C', 'K', 'D', 9, 'S'],['A', 'C', 'K', 'H', 3, 'H', 'A', 'S', 9, 'D'],['K', 'C', 9, 'H', 'Q', 'D', 6, 'C', 6, 'S'],[9, 'H', 7, 'S', 3, 'D', 5, 'C', 7, 'D'],['K', 'C', 'T', 'D', 8, 'H', 4, 'H', 6, 'S'],[3, 'C', 7, 'H', 8, 'H', 'T', 'C', 'Q', 'D'],[4, 'D', 7, 'S', 6, 'S', 'Q', 'H', 6, 'C'],[6, 'D', 'A', 'D', 4, 'C', 'Q', 'D', 6, 'C'],[5, 'D', 7, 'D', 9, 'D', 'K', 'S', 'T', 'S'],['J', 'H', 2, 'H', 'J', 'D', 9, 'S', 7, 'S'],['T', 'S', 'K', 'H', 8, 'D', 5, 'D', 8, 'H'],[2, 'D', 9, 'S', 4, 'C', 7, 'D', 9, 'D'],[5, 'H', 'Q', 'D', 6, 'D', 'A', 'C', 6, 'S'],[7, 'S', 6, 'D', 'J', 'C', 'Q', 'D', 'J', 'H'],[4, 'C', 6, 'S', 'Q', 'S', 2, 'H', 7, 'D'],[8, 'C', 'T', 'D', 'J', 'H', 'K', 'D', 2, 'H'],[5, 'C', 'Q', 'S', 2, 'C', 'J', 'S', 7, 'S'],['T', 'C', 5, 'H', 4, 'H', 'J', 'H', 'Q', 'D'],[3, 'S', 5, 'S', 5, 'D', 8, 'S', 'K', 'H'],['K', 'S', 'K', 'H', 7, 'C', 2, 'C', 5, 'D'],['J', 'H', 6, 'S', 9, 'C', 6, 'D', 'J', 'C'],[5, 'H', 'A', 'H', 'J', 'D', 9, 'C', 'J', 'S'],['K', 'C', 2, 'H', 6, 'H', 4, 'D', 5, 'S'],['A', 'S', 3, 'C', 'T', 'H', 'Q', 'C', 6, 'H'],[9, 'C', 8, 'S', 8, 'C', 'T', 'D', 7, 'C'],['K', 'C', 2, 'C', 'Q', 'D', 9, 'C', 'K', 'H'],[4, 'D', 7, 'S', 3, 'C', 'T', 'S', 9, 'H'],[9, 'C', 'Q', 'C', 2, 'S', 'T', 'S', 8, 'C'],['T', 'D', 9, 'S', 'Q', 'D', 3, 'S', 3, 'C'],[4, 'D', 9, 'D', 'T', 'H', 'J', 'H', 'A', 'H'],[6, 'S', 2, 'S', 'J', 'D', 'Q', 'H', 'J', 'S'],['Q', 'D', 9, 'H', 6, 'C', 'K', 'D', 7, 'D'],[7, 'H', 5, 'D', 6, 'S', 8, 'H', 'A', 'H'],[8, 'H', 3, 'C', 4, 'S', 2, 'H', 5, 'H'],['Q', 'S', 'Q', 'H', 7, 'S', 4, 'H', 'A', 'C'],['Q', 'S', 3, 'C', 7, 'S', 9, 'S', 4, 'H'],[3, 'S', 'A', 'H', 'K', 'S', 9, 'D', 7, 'C'],['A', 'D', 5, 'S', 6, 'S', 2, 'H', 2, 'D'],[5, 'H', 'T', 'C', 4, 'S', 3, 'C', 8, 'C'],['Q', 'H', 'T', 'S', 6, 'S', 4, 'D', 'J', 'S'],['K', 'S', 'J', 'H', 'A', 'S', 8, 'S', 6, 'D'],[2, 'C', 8, 'S', 2, 'S', 'T', 'D', 5, 'H'],['A', 'S', 'T', 'C', 'T', 'S', 6, 'C', 'K', 'C'],['K', 'C', 'T', 'S', 8, 'H', 2, 'H', 3, 'H'],[7, 'C', 4, 'C', 5, 'S', 'T', 'H', 'T', 'D'],['K', 'D', 'A', 'D', 'K', 'H', 7, 'H', 7, 'S'],[5, 'D', 5, 'H', 5, 'S', 2, 'D', 9, 'C'],['A', 'D', 9, 'S', 3, 'D', 7, 'S', 8, 'C'],['Q', 'C', 7, 'C', 9, 'C', 'K', 'D', 'K', 'S'],[3, 'C', 'Q', 'C', 9, 'S', 8, 'C', 4, 'D'],[5, 'C', 'A', 'S', 'Q', 'D', 6, 'C', 2, 'C'],[2, 'H', 'K', 'C', 8, 'S', 'J', 'D', 7, 'S'],['A', 'C', 8, 'D', 5, 'C', 2, 'S', 4, 'D'],[9, 'D', 'Q', 'H', 3, 'D', 2, 'S', 'T', 'C'],[3, 'S', 'K', 'S', 3, 'C', 9, 'H', 'T', 'D'],['K', 'D', 6, 'S', 'A', 'C', 2, 'C', 7, 'H'],[5, 'H', 3, 'S', 6, 'C', 6, 'H', 8, 'C'],['Q', 'H', 'T', 'C', 8, 'S', 6, 'S', 'K', 'H'],['T', 'H', 4, 'H', 5, 'D', 'T', 'S', 4, 'D'],[8, 'C', 'J', 'S', 4, 'H', 6, 'H', 2, 'C'],[2, 'H', 7, 'D', 'A', 'C', 'Q', 'D', 3, 'D'],['Q', 'S', 'K', 'C', 6, 'S', 2, 'D', 5, 'S'],[4, 'H', 'T', 'D', 3, 'H', 'J', 'H', 4, 'C'],[7, 'S', 5, 'H', 7, 'H', 8, 'H', 'K', 'H'],[6, 'H', 'Q', 'S', 'T', 'H', 'K', 'D', 7, 'D'],[5, 'H', 'A', 'D', 'K', 'D', 7, 'C', 'K', 'H'],[5, 'S', 'T', 'D', 6, 'D', 3, 'C', 6, 'C'],[8, 'C', 9, 'C', 5, 'H', 'J', 'D', 7, 'C'],['K', 'C', 'K', 'H', 7, 'H', 2, 'H', 3, 'S'],[7, 'S', 4, 'H', 'A', 'D', 4, 'D', 8, 'S'],['Q', 'S', 'T', 'H', 3, 'D', 7, 'H', 5, 'S'],[8, 'D', 'T', 'C', 'K', 'S', 'K', 'D', 9, 'S'],[6, 'D', 'A', 'D', 'J', 'D', 5, 'C', 2, 'S'],[7, 'H', 8, 'H', 6, 'C', 'Q', 'D', 2, 'H'],[6, 'H', 9, 'D', 'T', 'C', 9, 'S', 7, 'C'],[8, 'D', 6, 'D', 4, 'C', 7, 'C', 6, 'C'],[3, 'C', 'T', 'H', 'K', 'H', 'J', 'S', 'J', 'H'],[5, 'S', 3, 'S', 8, 'S', 'J', 'S', 9, 'H'],['A', 'S', 'A', 'D', 8, 'H', 7, 'S', 'K', 'D'],['J', 'H', 7, 'C', 2, 'C', 'K', 'C', 5, 'H'],['A', 'S', 'A', 'D', 9, 'C', 9, 'S', 'J', 'S'],['A', 'D', 'A', 'C', 2, 'C', 6, 'S', 'Q', 'D'],[7, 'C', 3, 'H', 'T', 'H', 'K', 'S', 'K', 'D'],[9, 'D', 'J', 'D', 4, 'H', 8, 'H', 4, 'C'],['K', 'H', 7, 'S', 'T', 'S', 8, 'C', 'K', 'C'],[3, 'S', 5, 'S', 2, 'H', 7, 'S', 6, 'H'],[7, 'D', 'K', 'S', 5, 'C', 6, 'D', 'A', 'D'],[5, 'S', 8, 'C', 9, 'H', 'Q', 'S', 7, 'H'],[7, 'S', 2, 'H', 6, 'C', 7, 'D', 'T', 'D'],['Q', 'S', 5, 'S', 'T', 'D', 'A', 'C', 9, 'D'],['K', 'C', 3, 'D', 'T', 'C', 2, 'D', 4, 'D'],['T', 'D', 2, 'H', 7, 'D', 'J', 'D', 'Q', 'D'],[4, 'C', 7, 'H', 5, 'D', 'K', 'C', 3, 'D'],[4, 'C', 3, 'H', 8, 'S', 'K', 'D', 'Q', 'H'],[5, 'S', 'Q', 'C', 9, 'H', 'T', 'C', 5, 'H'],[9, 'C', 'Q', 'D', 'T', 'H', 5, 'H', 'T', 'S'],[5, 'C', 9, 'H', 'A', 'H', 'Q', 'H', 2, 'C'],[4, 'D', 6, 'S', 3, 'C', 'A', 'C', 6, 'C'],[3, 'D', 2, 'C', 2, 'H', 'T', 'D', 'T', 'H'],['A', 'C', 9, 'C', 5, 'D', 'Q', 'C', 4, 'D'],['A', 'D', 8, 'D', 6, 'D', 8, 'C', 'K', 'C'],['A', 'D', 3, 'C', 4, 'H', 'A', 'C', 8, 'D'],[8, 'H', 7, 'S', 9, 'S', 'T', 'D', 'J', 'C'],[4, 'H', 9, 'H', 'Q', 'H', 'J', 'S', 2, 'D'],['T', 'H', 'T', 'D', 'T', 'C', 'K', 'D', 'K', 'S'],[5, 'S', 6, 'S', 9, 'S', 8, 'D', 'T', 'H'],['A', 'S', 'K', 'H', 5, 'H', 5, 'C', 8, 'S'],['J', 'D', 2, 'S', 9, 'S', 6, 'S', 5, 'S'],[8, 'S', 5, 'D', 7, 'S', 7, 'H', 9, 'D'],[5, 'D', 8, 'C', 4, 'C', 9, 'D', 'A', 'D'],['T', 'S', 2, 'C', 7, 'D', 'K', 'D', 'T', 'C'],[8, 'S', 'Q', 'S', 4, 'D', 'K', 'C', 5, 'C'],[8, 'D', 4, 'S', 'K', 'H', 'J', 'D', 'K', 'D'],['A', 'S', 5, 'C', 'A', 'D', 'Q', 'H', 7, 'D'],[2, 'H', 9, 'S', 7, 'H', 7, 'C', 'T', 'C'],[2, 'S', 8, 'S', 'J', 'D', 'K', 'H', 7, 'S'],[6, 'C', 6, 'D', 'A', 'D', 5, 'D', 'Q', 'C'],[9, 'H', 6, 'H', 3, 'S', 8, 'C', 8, 'H'],['A', 'H', 'T', 'C', 4, 'H', 'J', 'S', 'T', 'D'],[2, 'C', 'T', 'S', 4, 'D', 7, 'H', 2, 'D'],['Q', 'C', 9, 'C', 5, 'D', 'T', 'H', 7, 'C'],[6, 'C', 8, 'H', 'Q', 'C', 5, 'D', 'T', 'S'],['J', 'H', 5, 'C', 5, 'H', 9, 'H', 4, 'S'],[2, 'D', 'Q', 'C', 7, 'H', 'A', 'S', 'J', 'S'],[8, 'S', 2, 'H', 4, 'C', 4, 'H', 8, 'D'],['J', 'S', 6, 'S', 'A', 'C', 'K', 'D', 3, 'D'],[3, 'C', 4, 'S', 7, 'H', 'T', 'H', 'K', 'C'],['Q', 'H', 'K', 'H', 6, 'S', 'Q', 'S', 5, 'S'],[4, 'H', 3, 'C', 'Q', 'D', 3, 'S', 3, 'H'],[7, 'H', 'A', 'S', 'K', 'H', 8, 'C', 4, 'H'],[9, 'C', 5, 'S', 3, 'D', 6, 'S', 'T', 'S'],[9, 'C', 7, 'C', 3, 'H', 5, 'S', 'Q', 'D'],[2, 'C', 3, 'D', 'A', 'D', 'A', 'C', 5, 'H'],['J', 'H', 'T', 'D', 2, 'D', 4, 'C', 'T', 'S'],[3, 'H', 'K', 'H', 'A', 'D', 3, 'S', 7, 'S'],['A', 'S', 4, 'C', 5, 'H', 4, 'D', 6, 'S'],['K', 'D', 'J', 'C', 3, 'C', 6, 'H', 2, 'D'],[3, 'H', 6, 'S', 8, 'C', 2, 'D', 'T', 'H'],[4, 'S', 'A', 'H', 'Q', 'H', 'A', 'D', 5, 'H'],[7, 'C', 2, 'S', 9, 'H', 7, 'H', 'K', 'C'],[5, 'C', 6, 'D', 5, 'S', 3, 'H', 'J', 'C'],[3, 'C', 'T', 'C', 9, 'C', 4, 'H', 'Q', 'D'],['T', 'D', 'J', 'H', 6, 'D', 9, 'H', 5, 'S'],[7, 'C', 6, 'S', 5, 'C', 5, 'D', 6, 'C'],[4, 'S', 7, 'H', 9, 'H', 6, 'H', 'A', 'H'],['A', 'D', 2, 'H', 7, 'D', 'K', 'C', 2, 'C'],[4, 'C', 2, 'S', 9, 'S', 7, 'H', 3, 'S'],['T', 'H', 4, 'C', 8, 'S', 6, 'S', 3, 'S'],['A', 'D', 'K', 'S', 'A', 'S', 'J', 'H', 'T', 'D'],[5, 'C', 'T', 'D', 4, 'S', 4, 'D', 'A', 'D'],[6, 'S', 5, 'D', 'T', 'C', 9, 'C', 7, 'D'],[8, 'H', 3, 'S', 4, 'D', 4, 'S', 5, 'S'],[6, 'H', 5, 'C', 'A', 'C', 3, 'H', 3, 'D'],[9, 'H', 3, 'C', 'A', 'C', 4, 'S', 'Q', 'S'],[8, 'S', 9, 'D', 'Q', 'H', 5, 'H', 4, 'D'],['J', 'C', 6, 'C', 5, 'H', 'T', 'S', 'A', 'C'],[9, 'C', 'J', 'D', 8, 'C', 7, 'C', 'Q', 'D'],[8, 'S', 8, 'H', 9, 'C', 'J', 'D', 2, 'D'],['Q', 'C', 'Q', 'H', 6, 'H', 3, 'C', 8, 'D'],['K', 'S', 'J', 'S', 2, 'H', 6, 'H', 5, 'H'],['Q', 'H', 'Q', 'S', 3, 'H', 7, 'C', 6, 'D'],['T', 'C', 3, 'H', 4, 'S', 7, 'H', 'Q', 'C'],[2, 'H', 3, 'S', 8, 'C', 'J', 'S', 'K', 'H'],['A', 'H', 8, 'H', 5, 'S', 4, 'C', 9, 'H'],['J', 'D', 3, 'H', 7, 'S', 'J', 'C', 'A', 'C'],[3, 'C', 2, 'D', 4, 'C', 5, 'S', 6, 'C'],[4, 'S', 'Q', 'S', 3, 'S', 'J', 'D', 3, 'D'],[5, 'H', 2, 'D', 'T', 'C', 'A', 'H', 'K', 'S'],[6, 'D', 7, 'H', 'A', 'D', 8, 'C', 6, 'H'],[6, 'C', 7, 'S', 3, 'C', 'J', 'D', 7, 'C'],[8, 'H', 'K', 'S', 'K', 'H', 'A', 'H', 6, 'D'],['A', 'H', 7, 'D', 3, 'H', 8, 'H', 8, 'S'],[7, 'H', 'Q', 'S', 5, 'H', 9, 'D', 2, 'D'],['J', 'D', 'A', 'C', 4, 'H', 7, 'S', 8, 'S'],[9, 'S', 'K', 'S', 'A', 'S', 9, 'D', 'Q', 'H'],[7, 'S', 2, 'C', 8, 'S', 5, 'S', 'J', 'H'],['Q', 'S', 'J', 'C', 'A', 'H', 'K', 'D', 4, 'C'],['A', 'H', 2, 'S', 9, 'H', 4, 'H', 8, 'D'],['T', 'S', 'T', 'D', 6, 'H', 'Q', 'H', 'J', 'D'],[4, 'H', 'J', 'C', 3, 'H', 'Q', 'S', 6, 'D'],[7, 'S', 9, 'C', 8, 'S', 9, 'D', 8, 'D'],[5, 'H', 'T', 'D', 4, 'S', 9, 'S', 4, 'C'],[8, 'C', 8, 'D', 7, 'H', 3, 'H', 3, 'D'],['Q', 'S', 'K', 'H', 3, 'S', 2, 'C', 2, 'S'],[3, 'C', 7, 'S', 'T', 'D', 4, 'S', 'Q', 'D'],[7, 'C', 'T', 'D', 4, 'D', 5, 'S', 'K', 'H'],['A', 'C', 'A', 'S', 7, 'H', 4, 'C', 6, 'C'],[2, 'S', 5, 'H', 6, 'D', 'J', 'D', 9, 'H'],['Q', 'S', 8, 'S', 2, 'C', 2, 'H', 'T', 'D'],[2, 'S', 'T', 'S', 6, 'H', 9, 'H', 7, 'S'],[4, 'H', 'J', 'C', 4, 'C', 5, 'D', 5, 'S'],[2, 'C', 5, 'H', 7, 'D', 4, 'H', 3, 'S'],['Q', 'H', 'J', 'C', 'J', 'S', 6, 'D', 8, 'H'],[4, 'C', 'Q', 'H', 7, 'C', 'Q', 'D', 3, 'S'],['A', 'D', 'T', 'H', 8, 'S', 5, 'S', 'T', 'S'],[9, 'H', 'T', 'C', 2, 'S', 'T', 'D', 'J', 'C'],[7, 'D', 3, 'S', 3, 'D', 'T', 'H', 'Q', 'H'],[7, 'D', 4, 'C', 8, 'S', 5, 'C', 'J', 'H'],[8, 'H', 6, 'S', 3, 'S', 'K', 'C', 3, 'H'],['J', 'C', 3, 'H', 'K', 'H', 'T', 'C', 'Q', 'H'],['T', 'H', 6, 'H', 2, 'C', 'A', 'C', 5, 'H'],['Q', 'S', 2, 'H', 9, 'D', 2, 'C', 'A', 'S'],[6, 'S', 6, 'C', 2, 'S', 8, 'C', 8, 'S'],[9, 'H', 7, 'D', 'Q', 'C', 'T', 'H', 4, 'H'],['K', 'D', 'Q', 'S', 'A', 'C', 7, 'S', 3, 'C'],[4, 'D', 'J', 'H', 6, 'S', 5, 'S', 8, 'H'],['K', 'S', 9, 'S', 'Q', 'C', 3, 'S', 'A', 'S'],['J', 'D', 2, 'D', 6, 'S', 7, 'S', 'T', 'C'],[9, 'H', 'K', 'C', 3, 'H', 7, 'D', 'K', 'D'],[2, 'H', 'K', 'H', 7, 'C', 4, 'D', 4, 'S'],[3, 'H', 'J', 'S', 'Q', 'D', 7, 'D', 'K', 'C'],[4, 'C', 'J', 'C', 'A', 'S', 9, 'D', 3, 'C'],['J', 'S', 6, 'C', 8, 'H', 'Q', 'D', 4, 'D'],['A', 'H', 'J', 'S', 3, 'S', 6, 'C', 4, 'C'],[3, 'D', 'J', 'H', 6, 'D', 9, 'C', 9, 'H'],[9, 'H', 2, 'D', 8, 'C', 7, 'H', 5, 'S'],['K', 'S', 6, 'H', 9, 'C', 2, 'S', 'T', 'C'],[6, 'C', 8, 'C', 'A', 'D', 7, 'H', 6, 'H'],[3, 'D', 'K', 'H', 'A', 'S', 5, 'D', 'T', 'H'],['K', 'S', 8, 'C', 3, 'S', 'T', 'S', 8, 'S'],[4, 'D', 5, 'S', 9, 'S', 6, 'C', 4, 'H'],[9, 'H', 4, 'S', 4, 'H', 5, 'C', 7, 'D'],['K', 'C', 2, 'D', 2, 'H', 9, 'D', 'J', 'H'],[5, 'C', 'J', 'S', 'T', 'C', 9, 'D', 9, 'H'],[5, 'H', 7, 'S', 'K', 'H', 'J', 'C', 6, 'S'],[7, 'C', 9, 'H', 8, 'H', 4, 'D', 'J', 'C'],['K', 'H', 'J', 'D', 2, 'H', 'T', 'D', 'T', 'C'],[8, 'H', 6, 'C', 2, 'H', 2, 'C', 'K', 'H'],[6, 'H', 9, 'D', 'Q', 'S', 'Q', 'H', 5, 'H'],['A', 'C', 7, 'D', 2, 'S', 3, 'D', 'Q', 'D'],['J', 'C', 2, 'D', 8, 'D', 'J', 'D', 'J', 'H'],[2, 'H', 'J', 'C', 2, 'D', 7, 'H', 2, 'C'],[3, 'C', 8, 'D', 'K', 'D', 'T', 'D', 4, 'H'],[3, 'S', 4, 'H', 6, 'D', 8, 'D', 'T', 'S'],[3, 'H', 'T', 'D', 3, 'D', 6, 'H', 'T', 'H'],['J', 'H', 'J', 'C', 3, 'S', 'A', 'C', 'Q', 'H'],[9, 'H', 7, 'H', 8, 'S', 'Q', 'C', 2, 'C'],[7, 'H', 'T', 'D', 'Q', 'S', 4, 'S', 8, 'S'],[9, 'C', 2, 'S', 5, 'D', 4, 'D', 2, 'H'],[3, 'D', 'T', 'S', 3, 'H', 2, 'S', 'Q', 'C'],[8, 'H', 6, 'H', 'K', 'C', 'J', 'C', 'K', 'S'],[5, 'D', 'J', 'D', 7, 'D', 'T', 'C', 8, 'C'],[6, 'C', 9, 'S', 3, 'D', 8, 'D', 'A', 'C'],[8, 'H', 6, 'H', 'J', 'H', 6, 'C', 5, 'D'],[8, 'D', 8, 'S', 4, 'H', 'A', 'D', 2, 'C'],[9, 'D', 4, 'H', 2, 'D', 2, 'C', 3, 'S'],['T', 'S', 'A', 'S', 'T', 'C', 3, 'C', 5, 'D'],[4, 'D', 'T', 'H', 5, 'H', 'K', 'S', 'Q', 'S'],[6, 'C', 4, 'S', 2, 'H', 3, 'D', 'A', 'D'],[5, 'C', 'K', 'C', 6, 'H', 2, 'C', 5, 'S'],[3, 'C', 4, 'D', 2, 'D', 9, 'H', 9, 'S'],['J', 'D', 4, 'C', 3, 'H', 'T', 'H', 'Q', 'H'],[9, 'H', 5, 'S', 'A', 'H', 8, 'S', 'A', 'C'],[7, 'D', 9, 'S', 6, 'S', 2, 'H', 'T', 'D'],[9, 'C', 4, 'H', 8, 'H', 'Q', 'S', 4, 'C'],[3, 'C', 6, 'H', 5, 'D', 4, 'H', 8, 'C'],[9, 'C', 'K', 'C', 6, 'S', 'Q', 'D', 'Q', 'S'],[3, 'S', 9, 'H', 'K', 'D', 'T', 'C', 2, 'D'],['J', 'S', 8, 'C', 6, 'S', 4, 'H', 4, 'S'],[2, 'S', 4, 'C', 8, 'S', 'Q', 'S', 6, 'H'],['K', 'H', 3, 'H', 'T', 'H', 8, 'C', 5, 'D'],[2, 'C', 'K', 'H', 5, 'S', 3, 'S', 7, 'S'],[7, 'H', 6, 'C', 9, 'D', 'Q', 'D', 8, 'D'],[8, 'H', 'K', 'S', 'A', 'C', 2, 'D', 'K', 'H'],['T', 'S', 6, 'C', 'J', 'S', 'K', 'C', 7, 'H'],[9, 'C', 'K', 'S', 5, 'C', 'T', 'D', 'Q', 'C'],['A', 'H', 6, 'C', 5, 'H', 9, 'S', 7, 'C'],[5, 'D', 4, 'D', 3, 'H', 4, 'H', 6, 'S'],[7, 'C', 7, 'S', 'A', 'H', 'Q', 'D', 'T', 'D'],[2, 'H', 7, 'D', 'Q', 'C', 6, 'S', 'T', 'C'],['T', 'S', 'A', 'H', 7, 'S', 9, 'D', 3, 'H'],['T', 'H', 5, 'H', 'Q', 'D', 9, 'S', 'K', 'S'],[7, 'S', 7, 'C', 6, 'H', 8, 'C', 'T', 'D'],['T', 'H', 2, 'D', 4, 'D', 'Q', 'C', 5, 'C'],[7, 'D', 'J', 'D', 'A', 'H', 9, 'C', 4, 'H'],[4, 'H', 3, 'H', 'A', 'H', 8, 'D', 6, 'H'],['Q', 'C', 'Q', 'H', 9, 'H', 2, 'H', 2, 'C'],[2, 'D', 'A', 'D', 4, 'C', 'T', 'S', 6, 'H'],[7, 'S', 'T', 'H', 4, 'H', 'Q', 'S', 'T', 'D'],[3, 'C', 'K', 'D', 2, 'H', 3, 'H', 'Q', 'S'],['J', 'D', 'T', 'C', 'Q', 'C', 5, 'D', 8, 'H'],['K', 'S', 'J', 'C', 'Q', 'D', 'T', 'H', 9, 'S'],['K', 'D', 8, 'D', 8, 'C', 2, 'D', 9, 'C'],[3, 'C', 'Q', 'D', 'K', 'D', 6, 'D', 4, 'D'],[8, 'D', 'A', 'H', 'A', 'D', 'Q', 'C', 8, 'S'],[8, 'H', 3, 'S', 9, 'D', 2, 'S', 3, 'H'],['K', 'S', 6, 'H', 4, 'C', 7, 'C', 'K', 'C'],['T', 'H', 9, 'S', 5, 'C', 3, 'D', 7, 'D'],[6, 'H', 'A', 'C', 7, 'S', 4, 'D', 2, 'C'],[5, 'C', 3, 'D', 'J', 'D', 4, 'D', 2, 'D'],[6, 'D', 5, 'H', 9, 'H', 4, 'C', 'K', 'H'],['A', 'S', 7, 'H', 'T', 'D', 6, 'C', 2, 'H'],[3, 'D', 'Q', 'D', 'K', 'S', 4, 'C', 4, 'S'],['J', 'C', 3, 'C', 'A', 'C', 7, 'C', 'J', 'D'],['J', 'S', 8, 'H', 9, 'S', 'Q', 'C', 5, 'D'],['J', 'D', 6, 'S', 5, 'S', 2, 'H', 'A', 'S'],[8, 'C', 7, 'D', 5, 'H', 'J', 'H', 3, 'D'],[8, 'D', 'T', 'C', 5, 'S', 9, 'S', 8, 'S'],[3, 'H', 'J', 'C', 5, 'H', 7, 'S', 'A', 'S'],[5, 'C', 'T', 'D', 3, 'D', 7, 'D', 4, 'H'],[8, 'D', 7, 'H', 4, 'D', 5, 'D', 'J', 'S'],['Q', 'S', 9, 'C', 'K', 'S', 'T', 'D', 2, 'S'],[8, 'S', 5, 'C', 2, 'H', 4, 'H', 'A', 'S'],['T', 'H', 7, 'S', 4, 'H', 7, 'D', 3, 'H'],['J', 'D', 'K', 'D', 5, 'D', 2, 'S', 'K', 'C'],['J', 'D', 7, 'H', 4, 'S', 8, 'H', 4, 'C'],['J', 'S', 6, 'H', 'Q', 'H', 5, 'S', 4, 'H'],[2, 'C', 'Q', 'S', 8, 'C', 5, 'S', 3, 'H'],['Q', 'C', 2, 'S', 6, 'C', 'Q', 'D', 'A', 'D'],[8, 'C', 3, 'D', 'J', 'D', 'T', 'C', 4, 'H'],[2, 'H', 'A', 'D', 5, 'S', 'A', 'C', 2, 'S'],[5, 'D', 2, 'C', 'J', 'S', 2, 'D', 'A', 'D'],[9, 'D', 3, 'D', 4, 'C', 4, 'S', 'J', 'H'],[8, 'D', 5, 'H', 5, 'D', 6, 'H', 7, 'S'],[4, 'D', 'K', 'S', 9, 'D', 'T', 'D', 'J', 'D'],[3, 'D', 6, 'D', 9, 'C', 2, 'S', 'A', 'S'],[7, 'D', 5, 'S', 5, 'C', 8, 'H', 'J', 'D'],[7, 'C', 8, 'S', 3, 'S', 6, 'S', 5, 'H'],['J', 'D', 'T', 'C', 'A', 'D', 7, 'H', 7, 'S'],[2, 'S', 9, 'D', 'T', 'S', 4, 'D', 'A', 'C'],[8, 'D', 6, 'C', 'Q', 'D', 'J', 'D', 3, 'H'],[9, 'S', 'K', 'H', 2, 'C', 3, 'C', 'A', 'C'],[3, 'D', 5, 'H', 6, 'H', 8, 'D', 5, 'D'],['K', 'S', 3, 'D', 2, 'D', 6, 'S', 'A', 'S'],[4, 'C', 2, 'S', 7, 'C', 7, 'H', 'K', 'H'],['A', 'C', 2, 'H', 3, 'S', 'J', 'C', 5, 'C'],['Q', 'H', 4, 'D', 2, 'D', 5, 'H', 7, 'S'],['T', 'S', 'A', 'S', 'J', 'D', 8, 'C', 6, 'H'],['J', 'C', 8, 'S', 5, 'S', 2, 'C', 5, 'D'],[7, 'S', 'Q', 'H', 7, 'H', 6, 'C', 'Q', 'C'],[8, 'H', 2, 'D', 7, 'C', 'J', 'D', 2, 'S'],[2, 'C', 'Q', 'D', 2, 'S', 2, 'H', 'J', 'C'],[9, 'C', 5, 'D', 2, 'D', 'J', 'D', 'J', 'H'],[7, 'C', 5, 'C', 9, 'C', 8, 'S', 7, 'D'],[6, 'D', 8, 'D', 6, 'C', 9, 'S', 'J', 'H'],[2, 'C', 'A', 'D', 6, 'S', 5, 'H', 3, 'S'],['K', 'S', 7, 'S', 9, 'D', 'K', 'H', 4, 'C'],[7, 'H', 6, 'C', 2, 'C', 5, 'C', 'T', 'H'],[9, 'D', 8, 'D', 3, 'S', 'Q', 'C', 'A', 'H'],[5, 'S', 'K', 'C', 6, 'H', 'T', 'C', 5, 'H'],[8, 'S', 'T', 'H', 6, 'D', 3, 'C', 'A', 'H'],[9, 'C', 'K', 'D', 4, 'H', 'A', 'D', 'T', 'D'],[9, 'S', 4, 'S', 7, 'D', 6, 'H', 5, 'D'],[7, 'H', 5, 'C', 5, 'H', 6, 'D', 'A', 'S'],[4, 'C', 'K', 'D', 'K', 'H', 4, 'H', 9, 'D'],[3, 'C', 2, 'S', 5, 'C', 6, 'C', 'J', 'D'],['Q', 'S', 2, 'H', 9, 'D', 7, 'D', 3, 'H'],['A', 'C', 2, 'S', 6, 'S', 7, 'S', 'J', 'S'],['Q', 'D', 5, 'C', 'Q', 'S', 6, 'H', 'A', 'D'],[5, 'H', 'T', 'H', 'Q', 'C', 7, 'H', 'T', 'C'],[3, 'S', 7, 'C', 6, 'D', 'K', 'C', 3, 'D'],[4, 'H', 3, 'D', 'Q', 'C', 9, 'S', 8, 'H'],[2, 'C', 3, 'S', 'J', 'C', 'K', 'S', 5, 'C'],[4, 'S', 6, 'S', 2, 'C', 6, 'H', 8, 'S'],[3, 'S', 3, 'D', 9, 'H', 3, 'H', 'J', 'S'],[4, 'S', 8, 'C', 4, 'D', 2, 'D', 8, 'H'],[9, 'H', 7, 'D', 9, 'D', 'A', 'H', 'T', 'S'],[9, 'S', 2, 'C', 9, 'H', 4, 'C', 8, 'D'],['A', 'S', 7, 'D', 3, 'D', 6, 'D', 5, 'S'],[6, 'S', 4, 'C', 7, 'H', 8, 'C', 3, 'H'],[5, 'H', 'J', 'C', 'A', 'H', 9, 'D', 9, 'C'],[2, 'S', 7, 'C', 5, 'S', 'J', 'D', 8, 'C'],[3, 'S', 3, 'D', 4, 'D', 7, 'D', 6, 'S'],[3, 'C', 'K', 'C', 4, 'S', 5, 'D', 7, 'D'],[3, 'D', 'J', 'D', 7, 'H', 3, 'H', 4, 'H'],[9, 'C', 9, 'H', 4, 'H', 4, 'D', 'T', 'H'],[6, 'D', 'Q', 'D', 8, 'S', 9, 'S', 7, 'S'],[2, 'H', 'A', 'C', 8, 'S', 4, 'S', 'A', 'D'],[8, 'C', 2, 'C', 'A', 'H', 7, 'D', 'T', 'C'],['T', 'S', 9, 'H', 3, 'C', 'A', 'D', 'K', 'S'],['T', 'C', 3, 'D', 8, 'C', 8, 'H', 'J', 'D'],['Q', 'C', 8, 'D', 2, 'C', 3, 'C', 7, 'D'],[7, 'C', 'J', 'D', 9, 'H', 9, 'C', 6, 'C'],['A', 'H', 6, 'S', 'J', 'S', 'J', 'H', 5, 'D'],['A', 'S', 'Q', 'C', 2, 'C', 'J', 'D', 'T', 'D'],[9, 'H', 'K', 'D', 2, 'H', 5, 'D', 2, 'D'],[3, 'S', 7, 'D', 'T', 'C', 'A', 'H', 'T', 'S'],['T', 'D', 8, 'H', 'A', 'S', 5, 'D', 'A', 'H'],['Q', 'C', 'A', 'C', 6, 'S', 'T', 'C', 5, 'H'],['K', 'S', 4, 'S', 7, 'H', 4, 'D', 8, 'D'],[9, 'C', 'T', 'C', 2, 'H', 6, 'H', 3, 'H'],[3, 'H', 'K', 'D', 4, 'S', 'Q', 'D', 'Q', 'H'],[3, 'D', 8, 'H', 8, 'C', 'T', 'D', 7, 'S'],[8, 'S', 'J', 'D', 'T', 'C', 'A', 'H', 'J', 'S'],['Q', 'S', 2, 'D', 'K', 'H', 'K', 'S', 4, 'D'],[3, 'C', 'A', 'D', 'J', 'C', 'K', 'D', 'J', 'S'],['K', 'H', 4, 'S', 'T', 'H', 9, 'H', 2, 'C'],['Q', 'C', 5, 'S', 'J', 'S', 9, 'S', 'K', 'S'],['A', 'S', 7, 'C', 'Q', 'D', 2, 'S', 'J', 'D'],['K', 'C', 5, 'S', 'Q', 'S', 3, 'S', 2, 'D'],['A', 'C', 5, 'D', 9, 'H', 8, 'H', 'K', 'S'],[6, 'H', 9, 'C', 'T', 'C', 'A', 'D', 2, 'C'],[6, 'D', 5, 'S', 'J', 'D', 6, 'C', 7, 'C'],['Q', 'S', 'K', 'H', 'T', 'D', 'Q', 'D', 2, 'C'],[3, 'H', 8, 'S', 2, 'S', 'Q', 'C', 'A', 'H'],[9, 'D', 9, 'H', 'J', 'H', 'T', 'C', 'Q', 'H'],[3, 'C', 2, 'S', 'J', 'S', 5, 'C', 7, 'H'],[6, 'C', 3, 'S', 3, 'D', 2, 'S', 4, 'S'],['Q', 'D', 2, 'D', 'T', 'H', 5, 'D', 2, 'C'],[2, 'D', 6, 'H', 6, 'D', 2, 'S', 'J', 'C'],['Q', 'H', 'A', 'S', 7, 'H', 4, 'H', 'K', 'H'],[5, 'H', 6, 'S', 'K', 'S', 'A', 'D', 'T', 'C'],['T', 'S', 7, 'C', 'A', 'C', 4, 'S', 4, 'H'],['A', 'D', 3, 'C', 4, 'H', 'Q', 'S', 8, 'C'],[9, 'D', 'K', 'S', 2, 'H', 2, 'D', 4, 'D'],[4, 'S', 9, 'D', 6, 'C', 6, 'D', 9, 'C'],['A', 'C', 8, 'D', 3, 'H', 7, 'H', 'K', 'D'],['J', 'C', 'A', 'H', 6, 'C', 'T', 'S', 'J', 'D'],[6, 'D', 'A', 'D', 3, 'S', 5, 'D', 'Q', 'D'],['J', 'C', 'J', 'H', 'J', 'D', 3, 'S', 7, 'S'],[8, 'S', 'J', 'S', 'Q', 'C', 3, 'H', 4, 'S'],['J', 'D', 'T', 'H', 5, 'C', 2, 'C', 'A', 'D'],['J', 'S', 7, 'H', 9, 'S', 2, 'H', 7, 'S'],[8, 'D', 3, 'S', 'J', 'H', 4, 'D', 'Q', 'C'],['A', 'S', 'J', 'D', 2, 'C', 'K', 'C', 6, 'H'],[2, 'C', 'A', 'C', 5, 'H', 'K', 'D', 5, 'S'],[7, 'H', 'Q', 'D', 'J', 'H', 'A', 'H', 2, 'D'],['J', 'C', 'Q', 'H', 8, 'D', 8, 'S', 'T', 'C'],[5, 'H', 5, 'C', 'A', 'H', 8, 'C', 6, 'C'],[3, 'H', 'J', 'S', 8, 'S', 'Q', 'D', 'J', 'H'],[3, 'C', 4, 'H', 6, 'D', 5, 'C', 3, 'S'],[6, 'D', 4, 'S', 4, 'C', 'A', 'H', 5, 'H'],[5, 'S', 3, 'H', 'J', 'D', 7, 'C', 8, 'D'],[8, 'H', 'A', 'H', 2, 'H', 3, 'H', 'J', 'S'],[3, 'C', 7, 'D', 'Q', 'C', 4, 'H', 'K', 'D'],[6, 'S', 2, 'H', 'K', 'D', 5, 'H', 8, 'H'],[2, 'D', 3, 'C', 8, 'S', 7, 'S', 'Q', 'D'],[2, 'S', 7, 'S', 'K', 'C', 'Q', 'C', 'A', 'H'],['T', 'C', 'Q', 'S', 6, 'D', 4, 'C', 8, 'D'],[5, 'S', 9, 'H', 2, 'C', 3, 'S', 'Q', 'D'],[7, 'S', 6, 'C', 2, 'H', 7, 'C', 9, 'D'],[3, 'C', 6, 'C', 5, 'C', 5, 'S', 'J', 'D'],['J', 'C', 'K', 'S', 3, 'S', 5, 'D', 'T', 'S'],[7, 'C', 'K', 'S', 6, 'S', 5, 'S', 2, 'S'],[2, 'D', 'T', 'C', 2, 'H', 5, 'H', 'Q', 'S'],['A', 'S', 7, 'H', 6, 'S', 'T', 'S', 5, 'H'],[9, 'S', 9, 'D', 3, 'C', 'K', 'D', 2, 'H'],[4, 'S', 'J', 'S', 'Q', 'S', 3, 'S', 4, 'H'],[7, 'C', 2, 'S', 'A', 'C', 6, 'S', 9, 'D'],[8, 'C', 'J', 'H', 2, 'H', 5, 'H', 7, 'C'],[5, 'D', 'Q', 'H', 'Q', 'S', 'K', 'H', 'Q', 'C'],[3, 'S', 'T', 'D', 3, 'H', 7, 'C', 'K', 'C'],[8, 'D', 5, 'H', 8, 'S', 'K', 'H', 8, 'C'],[4, 'H', 'K', 'H', 'J', 'D', 'T', 'S', 3, 'C'],[7, 'H', 'A', 'S', 'Q', 'C', 'J', 'S', 5, 'S'],['A', 'H', 9, 'D', 2, 'C', 8, 'D', 4, 'D'],[2, 'D', 6, 'H', 6, 'C', 'K', 'C', 6, 'S'],[2, 'S', 6, 'H', 9, 'D', 3, 'S', 7, 'H'],[4, 'D', 'K', 'H', 8, 'H', 'K', 'D', 3, 'D'],[9, 'C', 'T', 'C', 'A', 'C', 'J', 'H', 'K', 'H'],[4, 'D', 'J', 'D', 5, 'H', 'T', 'D', 3, 'S'],[7, 'S', 4, 'H', 9, 'D', 'A', 'S', 4, 'C'],[7, 'D', 'Q', 'S', 9, 'S', 2, 'S', 'K', 'H'],[3, 'S', 8, 'D', 8, 'S', 'K', 'S', 8, 'C'],['J', 'C', 5, 'C', 'K', 'H', 2, 'H', 5, 'D'],[8, 'S', 'Q', 'H', 2, 'C', 4, 'D', 'K', 'C'],['J', 'S', 'Q', 'C', 9, 'D', 'A', 'C', 6, 'H'],[8, 'S', 8, 'C', 7, 'C', 'J', 'S', 'J', 'D'],[6, 'S', 4, 'C', 9, 'C', 'A', 'C', 4, 'S'],['Q', 'H', 5, 'D', 2, 'C', 7, 'D', 'J', 'C'],[8, 'S', 2, 'D', 'J', 'S', 'J', 'H', 4, 'C'],['J', 'S', 4, 'C', 7, 'S', 'T', 'S', 'J', 'H'],['K', 'C', 'K', 'H', 5, 'H', 'Q', 'D', 4, 'S'],['Q', 'D', 8, 'C', 8, 'D', 2, 'D', 6, 'S'],['T', 'D', 9, 'D', 'A', 'C', 'Q', 'H', 5, 'S'],['Q', 'H', 'Q', 'C', 'J', 'S', 3, 'D', 3, 'C'],[5, 'C', 4, 'H', 'K', 'H', 8, 'S', 7, 'H'],[7, 'C', 2, 'C', 5, 'S', 'J', 'C', 8, 'S'],[3, 'H', 'Q', 'C', 5, 'D', 2, 'H', 'K', 'C'],[5, 'S', 8, 'D', 'K', 'D', 6, 'H', 4, 'H'],['Q', 'D', 'Q', 'H', 6, 'D', 'A', 'H', 3, 'D'],[7, 'S', 'K', 'S', 6, 'C', 2, 'S', 4, 'D'],['A', 'C', 'Q', 'S', 5, 'H', 'T', 'S', 'J', 'D'],[7, 'C', 2, 'D', 'T', 'C', 5, 'D', 'Q', 'S'],['A', 'C', 'J', 'S', 'Q', 'C', 6, 'C', 'K', 'C'],[2, 'C', 'K', 'S', 4, 'D', 3, 'H', 'T', 'S'],[8, 'S', 'A', 'D', 4, 'H', 7, 'S', 9, 'S'],['Q', 'D', 9, 'H', 'Q', 'H', 5, 'H', 4, 'H'],[4, 'D', 'K', 'H', 3, 'S', 'J', 'C', 'A', 'D'],[4, 'D', 'A', 'C', 'K', 'C', 8, 'D', 6, 'D'],[4, 'C', 2, 'D', 'K', 'H', 2, 'C', 'J', 'D'],[2, 'C', 9, 'H', 2, 'D', 'A', 'H', 3, 'H'],[6, 'D', 9, 'C', 7, 'D', 'T', 'C', 'K', 'S'],[8, 'C', 3, 'H', 'K', 'D', 7, 'C', 5, 'C'],[2, 'S', 4, 'S', 5, 'H', 'A', 'S', 'A', 'H'],['T', 'H', 'J', 'D', 4, 'H', 'K', 'D', 3, 'H'],['T', 'C', 5, 'C', 3, 'S', 'A', 'C', 'K', 'H'],[6, 'D', 7, 'H', 'A', 'H', 7, 'S', 'Q', 'C'],[6, 'H', 2, 'D', 'T', 'D', 'J', 'D', 'A', 'S'],['J', 'H', 5, 'D', 7, 'H', 'T', 'C', 9, 'S'],[7, 'D', 'J', 'C', 'A', 'S', 5, 'S', 'K', 'H'],[2, 'H', 8, 'C', 'A', 'D', 'T', 'H', 6, 'H'],['Q', 'D', 'K', 'D', 9, 'H', 6, 'S', 6, 'C'],['Q', 'H', 'K', 'C', 9, 'D', 4, 'D', 3, 'S'],['J', 'S', 'J', 'H', 4, 'H', 2, 'C', 9, 'H'],['T', 'C', 7, 'H', 'K', 'H', 4, 'H', 'J', 'C'],[7, 'D', 9, 'S', 3, 'H', 'Q', 'S', 7, 'S'],['A', 'D', 7, 'D', 'J', 'H', 6, 'C', 7, 'H'],[4, 'H', 3, 'S', 3, 'H', 4, 'D', 'Q', 'H'],['J', 'D', 2, 'H', 5, 'C', 'A', 'S', 6, 'C'],['Q', 'C', 4, 'D', 3, 'C', 'T', 'C', 'J', 'H'],['A', 'C', 'J', 'D', 3, 'H', 6, 'H', 4, 'C'],['J', 'C', 'A', 'D', 7, 'D', 7, 'H', 9, 'H'],[4, 'H', 'T', 'C', 'T', 'S', 2, 'C', 8, 'C'],[6, 'S', 'K', 'S', 2, 'H', 'J', 'D', 9, 'S'],[4, 'C', 3, 'H', 'Q', 'S', 'Q', 'C', 9, 'S'],[9, 'H', 6, 'D', 'K', 'C', 9, 'D', 9, 'C'],[5, 'C', 'A', 'D', 8, 'C', 2, 'C', 'Q', 'H'],['T', 'H', 'Q', 'D', 'J', 'C', 8, 'D', 8, 'H'],['Q', 'C', 2, 'C', 2, 'S', 'Q', 'D', 9, 'C'],[4, 'D', 3, 'S', 8, 'D', 'J', 'H', 'Q', 'S'],[9, 'D', 3, 'S', 2, 'C', 7, 'S', 7, 'C'],['J', 'C', 'T', 'D', 3, 'C', 'T', 'C', 9, 'H'],[3, 'C', 'T', 'S', 8, 'H', 5, 'C', 4, 'C'],[2, 'C', 6, 'S', 8, 'D', 7, 'C', 4, 'H'],['K', 'S', 7, 'H', 2, 'H', 'T', 'C', 4, 'H'],[2, 'C', 3, 'S', 'A', 'S', 'A', 'H', 'Q', 'S'],[8, 'C', 2, 'D', 2, 'H', 2, 'C', 4, 'S'],[4, 'C', 6, 'S', 7, 'D', 5, 'S', 3, 'S'],['T', 'H', 'Q', 'C', 5, 'D', 'T', 'D', 3, 'C'],['Q', 'S', 'K', 'D', 'K', 'C', 'K', 'S', 'A', 'S'],[4, 'D', 'A', 'H', 'K', 'D', 9, 'H', 'K', 'S'],[5, 'C', 4, 'C', 6, 'H', 'J', 'C', 7, 'S'],['K', 'C', 4, 'H', 5, 'C', 'Q', 'S', 'T', 'C'],[2, 'H', 'J', 'C', 9, 'S', 'A', 'H', 'Q', 'H'],[4, 'S', 9, 'H', 3, 'H', 5, 'H', 3, 'C'],['Q', 'D', 2, 'H', 'Q', 'C', 'J', 'H', 8, 'H'],[5, 'D', 'A', 'S', 7, 'H', 2, 'C', 3, 'D'],['J', 'H', 6, 'H', 4, 'C', 6, 'S', 7, 'D'],[9, 'C', 'J', 'D', 9, 'H', 'A', 'H', 'J', 'S'],[8, 'S', 'Q', 'H', 3, 'H', 'K', 'S', 8, 'H'],[3, 'S', 'A', 'C', 'Q', 'C', 'T', 'S', 4, 'D'],['A', 'D', 3, 'D', 'A', 'H', 8, 'S', 9, 'H'],[7, 'H', 3, 'H', 'Q', 'S', 9, 'C', 9, 'S'],[5, 'H', 'J', 'H', 'J', 'S', 'A', 'H', 'A', 'C'],[8, 'D', 3, 'C', 'J', 'D', 2, 'H', 'A', 'C'],[9, 'C', 7, 'H', 5, 'S', 4, 'D', 8, 'H'],[7, 'C', 'J', 'H', 9, 'H', 6, 'C', 'J', 'S'],[9, 'S', 7, 'H', 8, 'C', 9, 'D', 4, 'H'],[2, 'D', 'A', 'S', 9, 'S', 6, 'H', 4, 'D'],['J', 'S', 'J', 'H', 9, 'H', 'A', 'D', 'Q', 'D'],[6, 'H', 7, 'S', 'J', 'H', 'K', 'H', 'A', 'H'],[7, 'H', 'T', 'D', 5, 'S', 6, 'S', 2, 'C'],[8, 'H', 'J', 'H', 6, 'S', 5, 'H', 5, 'S'],[9, 'D', 'T', 'C', 4, 'C', 'Q', 'C', 9, 'S'],[7, 'D', 2, 'C', 'K', 'D', 3, 'H', 5, 'H'],['A', 'S', 'Q', 'D', 7, 'H', 'J', 'S', 4, 'D'],['T', 'S', 'Q', 'H', 6, 'C', 8, 'H', 'T', 'H'],[5, 'H', 3, 'C', 3, 'H', 9, 'C', 9, 'D'],['A', 'D', 'K', 'H', 'J', 'S', 5, 'D', 3, 'H'],['A', 'S', 'A', 'C', 9, 'S', 5, 'C', 'K', 'C'],[2, 'C', 'K', 'H', 8, 'C', 'J', 'C', 'Q', 'S'],[6, 'D', 'A', 'H', 2, 'D', 'K', 'C', 'T', 'C'],[9, 'D', 3, 'H', 2, 'S', 7, 'C', 4, 'D'],[6, 'D', 'K', 'H', 'K', 'S', 8, 'D', 7, 'D'],[9, 'H', 2, 'S', 'T', 'C', 'J', 'H', 'A', 'C'],['Q', 'C', 3, 'H', 5, 'S', 3, 'S', 8, 'H'],[3, 'S', 'A', 'S', 'K', 'D', 8, 'H', 4, 'C'],[3, 'H', 7, 'C', 'J', 'H', 'Q', 'H', 'T', 'S'],[7, 'S', 6, 'D', 7, 'H', 9, 'D', 'J', 'H'],[4, 'C', 3, 'D', 3, 'S', 6, 'C', 'A', 'S'],[4, 'S', 2, 'H', 2, 'C', 4, 'C', 8, 'S'],[5, 'H', 'K', 'C', 8, 'C', 'Q', 'C', 'Q', 'D'],[3, 'H', 3, 'S', 6, 'C', 'Q', 'S', 'Q', 'C'],[2, 'D', 6, 'S', 5, 'D', 2, 'C', 9, 'D'],[2, 'H', 8, 'D', 'J', 'H', 2, 'S', 3, 'H'],[2, 'D', 6, 'C', 5, 'C', 7, 'S', 'A', 'D'],[9, 'H', 'J', 'S', 5, 'D', 'Q', 'H', 8, 'S'],['T', 'S', 2, 'H', 7, 'S', 6, 'S', 'A', 'D'],[6, 'D', 'Q', 'C', 9, 'S', 7, 'H', 5, 'H'],[5, 'C', 7, 'D', 'K', 'C', 'J', 'D', 4, 'H'],['Q', 'C', 5, 'S', 9, 'H', 9, 'C', 4, 'D'],[6, 'S', 'K', 'S', 2, 'S', 4, 'C', 7, 'C'],[9, 'H', 7, 'C', 4, 'H', 8, 'D', 3, 'S'],[6, 'H', 5, 'C', 8, 'H', 'J', 'S', 7, 'S'],[2, 'D', 6, 'H', 'J', 'S', 'T', 'D', 4, 'H'],[4, 'D', 'J', 'C', 'T', 'H', 5, 'H', 'K', 'C'],['A', 'C', 7, 'C', 8, 'D', 'T', 'H', 3, 'H'],[9, 'S', 2, 'D', 4, 'C', 'K', 'C', 4, 'D'],['K', 'D', 'Q', 'S', 9, 'C', 7, 'S', 3, 'D'],['K', 'S', 'A', 'D', 'T', 'S', 4, 'C', 4, 'H'],['Q', 'H', 9, 'C', 8, 'H', 2, 'S', 7, 'D'],['K', 'S', 7, 'H', 5, 'D', 'K', 'D', 4, 'C'],[9, 'C', 2, 'S', 2, 'H', 'J', 'C', 6, 'S'],[6, 'C', 'T', 'C', 'Q', 'C', 'J', 'H', 5, 'C'],[7, 'S', 'A', 'C', 8, 'H', 'K', 'C', 8, 'S'],[6, 'H', 'Q', 'S', 'J', 'C', 3, 'D', 6, 'S'],['J', 'S', 2, 'D', 'J', 'H', 8, 'C', 4, 'S'],[6, 'H', 8, 'H', 6, 'D', 5, 'D', 'A', 'D'],[6, 'H', 7, 'D', 2, 'S', 4, 'H', 9, 'H'],[7, 'C', 'A', 'S', 'A', 'C', 8, 'H', 5, 'S'],[3, 'C', 'J', 'S', 4, 'S', 6, 'D', 5, 'H'],[2, 'S', 'Q', 'H', 6, 'S', 9, 'C', 2, 'C'],[3, 'D', 5, 'S', 6, 'S', 9, 'S', 4, 'C'],['Q', 'S', 8, 'D', 'Q', 'D', 8, 'S', 'T', 'C'],[9, 'C', 3, 'D', 'A', 'H', 9, 'H', 5, 'S'],[2, 'C', 7, 'D', 'A', 'D', 'J', 'C', 3, 'S'],[7, 'H', 'T', 'C', 'A', 'S', 3, 'C', 6, 'S'],[6, 'D', 7, 'S', 'K', 'H', 'K', 'C', 9, 'H'],[3, 'S', 'T', 'C', 8, 'H', 6, 'S', 5, 'H'],['J', 'H', 8, 'C', 7, 'D', 'A', 'C', 2, 'S'],['Q', 'D', 9, 'D', 9, 'C', 3, 'S', 'J', 'C'],[8, 'C', 'K', 'S', 8, 'H', 5, 'D', 4, 'D'],['J', 'S', 'A', 'H', 'J', 'D', 6, 'D', 9, 'D'],[8, 'C', 9, 'H', 9, 'S', 8, 'H', 3, 'H'],[2, 'D', 6, 'S', 4, 'C', 4, 'D', 8, 'S'],['A', 'D', 4, 'S', 'T', 'C', 'A', 'H', 9, 'H'],['T', 'S', 'A', 'C', 'Q', 'C', 'T', 'H', 'K', 'C'],[6, 'D', 4, 'H', 7, 'S', 8, 'C', 2, 'H'],[3, 'C', 'Q', 'D', 'J', 'S', 9, 'D', 5, 'S'],['J', 'C', 'A', 'H', 2, 'H', 'T', 'S', 9, 'H'],[3, 'H', 4, 'D', 'Q', 'H', 5, 'D', 9, 'C'],[5, 'H', 7, 'D', 4, 'S', 'J', 'C', 3, 'S'],[8, 'S', 'T', 'H', 3, 'H', 7, 'C', 2, 'H'],['J', 'D', 'J', 'S', 'T', 'S', 'A', 'C', 8, 'D'],[9, 'C', 2, 'H', 'T', 'D', 'K', 'C', 'J', 'D'],[2, 'S', 8, 'C', 5, 'S', 'A', 'D', 2, 'C'],[3, 'D', 'K', 'D', 7, 'C', 5, 'H', 4, 'D'],['Q', 'H', 'Q', 'D', 'T', 'C', 6, 'H', 7, 'D'],[7, 'H', 2, 'C', 'K', 'C', 5, 'S', 'K', 'D'],[6, 'H', 'A', 'H', 'Q', 'C', 7, 'S', 'Q', 'H'],[6, 'H', 5, 'C', 'A', 'C', 5, 'H', 2, 'C'],[9, 'C', 2, 'D', 7, 'C', 'T', 'D', 2, 'S'],[4, 'D', 9, 'D', 'A', 'H', 3, 'D', 7, 'C'],['J', 'D', 4, 'H', 8, 'C', 4, 'C', 'K', 'S'],['T', 'H', 3, 'C', 'J', 'S', 'Q', 'H', 8, 'H'],[4, 'C', 'A', 'S', 3, 'D', 'Q', 'S', 'Q', 'C'],[4, 'D', 7, 'S', 5, 'H', 'J', 'H', 6, 'D'],[7, 'D', 6, 'H', 'J', 'S', 'K', 'H', 3, 'C'],['Q', 'D', 8, 'S', 7, 'D', 2, 'H', 2, 'C'],[7, 'C', 'J', 'C', 2, 'S', 5, 'H', 8, 'C'],['Q', 'H', 8, 'S', 9, 'D', 'T', 'C', 2, 'H'],['A', 'D', 7, 'C', 8, 'D', 'Q', 'D', 6, 'S'],[3, 'S', 7, 'C', 'A', 'D', 9, 'H', 2, 'H'],[9, 'S', 'J', 'D', 'T', 'S', 4, 'C', 2, 'D'],[3, 'S', 'A', 'S', 4, 'H', 'Q', 'C', 2, 'C'],[8, 'H', 8, 'S', 7, 'S', 'T', 'D', 'T', 'C'],['J', 'H', 'T', 'H', 'T', 'D', 3, 'S', 4, 'D'],[4, 'H', 5, 'S', 5, 'D', 'Q', 'S', 2, 'C'],[8, 'C', 'Q', 'D', 'Q', 'H', 'T', 'C', 6, 'D'],[4, 'S', 9, 'S', 9, 'D', 4, 'H', 'Q', 'C'],[8, 'C', 'J', 'S', 9, 'D', 6, 'H', 'J', 'D'],[3, 'H', 'A', 'D', 6, 'S', 'T', 'D', 'Q', 'C'],['K', 'C', 8, 'S', 3, 'D', 7, 'C', 'T', 'D'],[7, 'D', 8, 'D', 9, 'H', 4, 'S', 3, 'S'],[6, 'C', 4, 'S', 3, 'D', 9, 'D', 'K', 'D'],['T', 'C', 'K', 'C', 'K', 'S', 'A', 'C', 5, 'S'],[7, 'C', 6, 'S', 'Q', 'H', 3, 'D', 'J', 'S'],['K', 'D', 6, 'H', 6, 'D', 2, 'D', 8, 'C'],['J', 'D', 2, 'S', 5, 'S', 4, 'H', 8, 'S'],['A', 'C', 2, 'D', 6, 'S', 'T', 'S', 5, 'C'],[5, 'H', 8, 'C', 5, 'S', 3, 'C', 4, 'S'],[3, 'D', 7, 'C', 8, 'D', 'A', 'S', 3, 'H'],['A', 'S', 'T', 'S', 7, 'C', 3, 'H', 'A', 'D'],[7, 'D', 'J', 'C', 'Q', 'S', 6, 'C', 6, 'H'],[3, 'S', 9, 'S', 4, 'C', 'A', 'C', 'Q', 'H'],[5, 'H', 5, 'D', 9, 'H', 'T', 'S', 4, 'H'],[6, 'C', 5, 'C', 7, 'H', 7, 'S', 'T', 'D'],['A', 'D', 'J', 'D', 5, 'S', 2, 'H', 2, 'S'],[7, 'D', 6, 'C', 'K', 'C', 3, 'S', 'J', 'D'],[8, 'D', 8, 'S', 'T', 'S', 'Q', 'S', 'K', 'H'],[8, 'S', 'Q', 'S', 8, 'D', 6, 'C', 'T', 'H'],['A', 'C', 'A', 'H', 2, 'C', 8, 'H', 9, 'S'],[7, 'H', 'T', 'D', 'K', 'H', 'Q', 'H', 8, 'S'],[3, 'D', 4, 'D', 'A', 'H', 'J', 'D', 'A', 'S'],['T', 'S', 3, 'D', 2, 'H', 'J', 'C', 2, 'S'],['J', 'H', 'K', 'H', 6, 'C', 'Q', 'C', 'J', 'S'],['K', 'C', 'T', 'H', 2, 'D', 6, 'H', 7, 'S'],[2, 'S', 'T', 'C', 8, 'C', 9, 'D', 'Q', 'S'],[3, 'C', 9, 'D', 6, 'S', 'K', 'H', 8, 'H'],[6, 'D', 5, 'D', 'T', 'H', 2, 'C', 2, 'H'],[6, 'H', 'T', 'C', 7, 'D', 'A', 'D', 4, 'D'],[8, 'S', 'T', 'S', 9, 'H', 'T', 'D', 7, 'S'],['J', 'S', 6, 'D', 'J', 'D', 'J', 'C', 2, 'H'],['A', 'C', 6, 'C', 3, 'D', 'K', 'H', 8, 'D'],['K', 'H', 'J', 'D', 9, 'S', 5, 'D', 4, 'H'],[4, 'C', 3, 'H', 7, 'S', 'Q', 'S', 5, 'C'],[4, 'H', 'J', 'D', 5, 'D', 3, 'S', 3, 'C'],[4, 'D', 'K', 'H', 'Q', 'H', 'Q', 'S', 7, 'S'],['J', 'D', 'T', 'S', 8, 'S', 'Q', 'D', 'A', 'H'],[4, 'C', 6, 'H', 3, 'S', 5, 'S', 2, 'C'],['Q', 'S', 3, 'D', 'J', 'D', 'A', 'S', 8, 'D'],['T', 'H', 7, 'C', 6, 'S', 'Q', 'C', 'K', 'S'],[7, 'S', 2, 'H', 8, 'C', 'Q', 'C', 7, 'H'],['A', 'C', 6, 'D', 2, 'D', 'T', 'H', 'K', 'H'],[5, 'S', 6, 'C', 7, 'H', 'K', 'H', 7, 'D'],['A', 'H', 8, 'C', 5, 'C', 7, 'S', 3, 'D'],[3, 'C', 'K', 'D', 'A', 'D', 7, 'D', 6, 'C'],[4, 'D', 'K', 'S', 2, 'D', 8, 'C', 4, 'S'],[7, 'C', 8, 'D', 5, 'S', 2, 'D', 2, 'S'],['A', 'H', 'A', 'D', 2, 'C', 9, 'D', 'T', 'D'],[3, 'C', 'A', 'D', 4, 'S', 'K', 'S', 'J', 'H'],[7, 'C', 5, 'C', 8, 'C', 9, 'C', 'T', 'H'],['A', 'S', 'T', 'D', 4, 'D', 7, 'C', 'J', 'D'],[8, 'C', 'Q', 'H', 3, 'C', 5, 'H', 9, 'S'],[3, 'H', 9, 'C', 8, 'S', 9, 'S', 6, 'S'],['Q', 'D', 'K', 'S', 'A', 'H', 5, 'H', 'J', 'H'],['Q', 'C', 9, 'C', 5, 'S', 4, 'H', 2, 'H'],['T', 'D', 7, 'D', 'A', 'S', 8, 'C', 9, 'D'],[8, 'C', 2, 'C', 9, 'D', 'K', 'D', 'T', 'C'],[7, 'S', 3, 'D', 'K', 'H', 'Q', 'C', 3, 'C'],[4, 'D', 'A', 'S', 4, 'C', 'Q', 'S', 5, 'S'],[9, 'D', 6, 'S', 'J', 'D', 'Q', 'H', 'K', 'S'],[6, 'D', 'A', 'H', 6, 'C', 4, 'C', 5, 'H'],['T', 'S', 9, 'H', 7, 'D', 3, 'D', 5, 'S'],['Q', 'S', 'J', 'D', 7, 'C', 8, 'D', 9, 'C'],['A', 'C', 3, 'S', 6, 'S', 6, 'C', 'K', 'H'],[8, 'H', 'J', 'H', 5, 'D', 9, 'S', 6, 'D'],['A', 'S', 6, 'S', 3, 'S', 'Q', 'C', 7, 'H'],['Q', 'D', 'A', 'D', 5, 'C', 'J', 'H', 2, 'H'],['A', 'H', 4, 'H', 'A', 'S', 'K', 'C', 2, 'C'],['J', 'H', 9, 'C', 2, 'C', 6, 'H', 2, 'D'],['J', 'S', 5, 'D', 9, 'H', 'K', 'C', 6, 'D'],[7, 'D', 9, 'D', 'K', 'D', 'T', 'H', 3, 'H'],['A', 'S', 6, 'S', 'Q', 'C', 6, 'H', 'A', 'D'],['J', 'D', 4, 'H', 7, 'D', 'K', 'C', 3, 'H'],['J', 'S', 3, 'C', 'T', 'H', 3, 'D', 'Q', 'S'],[4, 'C', 3, 'H', 8, 'C', 'Q', 'D', 5, 'H'],[6, 'H', 'A', 'S', 8, 'H', 'A', 'D', 'J', 'D'],['T', 'H', 8, 'S', 'K', 'D', 5, 'D', 'Q', 'C'],[7, 'D', 'J', 'S', 5, 'S', 5, 'H', 'T', 'S'],[7, 'D', 'K', 'C', 9, 'D', 'Q', 'S', 3, 'H'],[3, 'C', 6, 'D', 'T', 'S', 7, 'S', 'A', 'H'],[7, 'C', 4, 'H', 7, 'H', 'A', 'H', 'Q', 'C'],['A', 'C', 4, 'D', 5, 'D', 6, 'D', 'T', 'H'],[3, 'C', 4, 'H', 2, 'S', 'K', 'D', 8, 'H'],[5, 'H', 'J', 'H', 'T', 'C', 6, 'C', 'J', 'D'],[4, 'S', 8, 'C', 3, 'D', 4, 'H', 'J', 'S'],['T', 'D', 7, 'S', 'J', 'H', 'Q', 'S', 'K', 'D'],[7, 'C', 'Q', 'C', 'K', 'D', 4, 'D', 7, 'H'],[6, 'S', 'A', 'D', 'T', 'D', 'T', 'C', 'K', 'H'],[5, 'H', 9, 'H', 'K', 'C', 3, 'H', 4, 'D'],[3, 'D', 'A', 'D', 6, 'S', 'Q', 'D', 6, 'H'],['T', 'H', 7, 'C', 6, 'H', 'T', 'S', 'Q', 'H'],[5, 'S', 2, 'C', 'K', 'C', 'T', 'D', 6, 'S'],[7, 'C', 4, 'D', 5, 'S', 'J', 'D', 'J', 'H'],[7, 'D', 'A', 'C', 'K', 'D', 'K', 'H', 4, 'H'],[7, 'D', 6, 'C', 8, 'D', 8, 'H', 5, 'C'],['J', 'H', 8, 'S', 'Q', 'D', 'T', 'H', 'J', 'D'],[8, 'D', 7, 'D', 6, 'C', 7, 'C', 9, 'D'],['K', 'D', 'A', 'S', 5, 'C', 'Q', 'H', 'J', 'H'],[9, 'S', 2, 'C', 8, 'C', 3, 'C', 4, 'C'],['K', 'S', 'J', 'H', 2, 'D', 8, 'D', 4, 'H'],[7, 'S', 6, 'C', 'J', 'H', 'K', 'H', 8, 'H'],[3, 'H', 9, 'D', 2, 'D', 'A', 'H', 6, 'D'],[4, 'D', 'T', 'C', 9, 'C', 8, 'D', 7, 'H'],['T', 'D', 'K', 'S', 'T', 'H', 'K', 'D', 3, 'C'],['J', 'D', 9, 'H', 8, 'D', 'Q', 'D', 'A', 'S'],['K', 'D', 9, 'D', 2, 'C', 2, 'S', 9, 'C'],[8, 'D', 3, 'H', 5, 'C', 7, 'H', 'K', 'S'],[5, 'H', 'Q', 'H', 2, 'D', 8, 'C', 9, 'H'],[2, 'D', 'T', 'H', 6, 'D', 'Q', 'D', 6, 'C'],['K', 'C', 3, 'H', 3, 'S', 'A', 'D', 4, 'C'],[4, 'H', 3, 'H', 'J', 'S', 9, 'D', 3, 'C'],['T', 'C', 5, 'H', 'Q', 'H', 'Q', 'C', 'J', 'C'],[3, 'D', 5, 'C', 6, 'H', 3, 'S', 3, 'C'],['J', 'C', 5, 'S', 7, 'S', 2, 'S', 'Q', 'H'],['A', 'C', 5, 'C', 8, 'C', 4, 'D', 5, 'D'],[4, 'H', 2, 'S', 'Q', 'D', 3, 'C', 3, 'H'],[2, 'C', 'T', 'D', 'A', 'H', 9, 'C', 'K', 'D'],['J', 'S', 6, 'S', 'Q', 'D', 4, 'C', 'Q', 'C'],['Q', 'S', 8, 'C', 3, 'S', 4, 'H', 'T', 'C'],['J', 'S', 3, 'H', 7, 'C', 'J', 'C', 'A', 'D'],[5, 'H', 4, 'D', 9, 'C', 'K', 'S', 'J', 'C'],['T', 'D', 9, 'S', 'T', 'S', 8, 'S', 9, 'H'],['Q', 'D', 'T', 'S', 7, 'D', 'A', 'S', 'A', 'C'],[2, 'C', 'T', 'D', 6, 'H', 8, 'H', 'A', 'H'],[6, 'S', 'A', 'D', 8, 'C', 4, 'S', 9, 'H'],[8, 'D', 9, 'D', 'K', 'H', 8, 'S', 3, 'C'],['Q', 'S', 4, 'D', 2, 'D', 7, 'S', 'K', 'H'],['J', 'S', 'J', 'C', 'A', 'D', 4, 'C', 3, 'C'],['Q', 'S', 9, 'S', 7, 'H', 'K', 'C', 'T', 'D'],['T', 'H', 5, 'H', 'J', 'S', 'A', 'C', 'J', 'H'],[6, 'D', 'A', 'C', 2, 'S', 'Q', 'S', 7, 'C'],['A', 'S', 'K', 'S', 6, 'S', 'K', 'H', 5, 'S'],[6, 'D', 8, 'H', 'K', 'H', 3, 'C', 'Q', 'S'],[2, 'H', 5, 'C', 9, 'C', 9, 'D', 6, 'C'],['J', 'S', 2, 'C', 4, 'C', 6, 'H', 7, 'D'],['J', 'C', 'A', 'C', 'Q', 'D', 'T', 'D', 3, 'H'],[4, 'H', 'Q', 'C', 8, 'H', 'J', 'D', 4, 'C'],['K', 'D', 'K', 'S', 5, 'C', 'K', 'C', 7, 'S'],[6, 'D', 2, 'D', 3, 'H', 2, 'S', 'Q', 'D'],[5, 'S', 7, 'H', 'A', 'S', 'T', 'H', 6, 'S'],['A', 'S', 6, 'D', 8, 'D', 2, 'C', 8, 'S'],['T', 'D', 8, 'H', 'Q', 'D', 'J', 'C', 'A', 'H'],[9, 'C', 9, 'H', 2, 'D', 'T', 'D', 'Q', 'H'],[2, 'H', 5, 'C', 'T', 'C', 3, 'D', 8, 'H'],['K', 'C', 8, 'S', 3, 'D', 'K', 'H', 2, 'S'],['T', 'S', 'T', 'C', 6, 'S', 4, 'D', 'J', 'H'],[9, 'H', 9, 'D', 'Q', 'S', 'A', 'C', 'K', 'C'],[6, 'H', 5, 'D', 4, 'D', 8, 'D', 'A', 'H'],[9, 'S', 5, 'C', 'Q', 'S', 4, 'H', 7, 'C'],[7, 'D', 2, 'H', 8, 'S', 'A', 'D', 'J', 'S'],[3, 'D', 'A', 'C', 9, 'S', 'A', 'S', 2, 'C'],[2, 'D', 2, 'H', 3, 'H', 'J', 'C', 'K', 'H'],[7, 'H', 'Q', 'H', 'K', 'H', 'J', 'D', 'T', 'C'],['K', 'S', 5, 'S', 8, 'H', 4, 'C', 8, 'D'],[2, 'H', 7, 'H', 3, 'S', 2, 'S', 5, 'H'],['Q', 'S', 3, 'C', 'A', 'S', 9, 'H', 'K', 'D'],['A', 'D', 3, 'D', 'J', 'D', 6, 'H', 5, 'S'],[9, 'C', 6, 'D', 'A', 'C', 9, 'S', 3, 'S'],[3, 'D', 5, 'D', 9, 'C', 2, 'D', 'A', 'C'],[4, 'S', 2, 'S', 'A', 'D', 6, 'C', 6, 'S'],['Q', 'C', 4, 'C', 2, 'D', 3, 'H', 6, 'S'],['K', 'C', 'Q', 'H', 'Q', 'D', 2, 'H', 'J', 'H'],['Q', 'C', 3, 'C', 8, 'S', 4, 'D', 9, 'S'],[2, 'H', 5, 'C', 8, 'H', 'Q', 'S', 'Q', 'D'],[6, 'D', 'K', 'D', 6, 'S', 7, 'H', 3, 'S'],['K', 'H', 2, 'H', 5, 'C', 'J', 'C', 6, 'C'],[3, 'S', 9, 'S', 'T', 'C', 6, 'S', 8, 'H'],[2, 'D', 'A', 'D', 7, 'S', 8, 'S', 'T', 'S'],[3, 'C', 6, 'H', 9, 'C', 3, 'H', 5, 'C'],['J', 'C', 8, 'H', 'Q', 'H', 'T', 'D', 'Q', 'D'],[3, 'C', 'J', 'S', 'Q', 'D', 5, 'D', 'T', 'D'],[2, 'C', 'K', 'H', 9, 'H', 'T', 'H', 'A', 'S'],[9, 'S', 'T', 'C', 'J', 'D', 3, 'D', 5, 'C'],[5, 'H', 'A', 'D', 'Q', 'H', 9, 'H', 'K', 'C'],['T', 'C', 7, 'H', 4, 'H', 8, 'H', 3, 'H'],['T', 'D', 6, 'S', 'A', 'C', 7, 'C', 2, 'S'],['Q', 'S', 9, 'D', 5, 'D', 3, 'C', 'J', 'C'],['K', 'S', 4, 'D', 6, 'C', 'J', 'H', 2, 'S'],[9, 'S', 6, 'S', 3, 'C', 7, 'H', 'T', 'S'],[4, 'C', 'K', 'D', 6, 'D', 3, 'D', 9, 'C'],[2, 'D', 9, 'H', 'A', 'H', 'A', 'C', 7, 'H'],[2, 'S', 'J', 'H', 3, 'S', 7, 'C', 'Q', 'C'],['Q', 'D', 9, 'H', 3, 'C', 2, 'H', 'A', 'C'],['A', 'S', 8, 'S', 'K', 'D', 8, 'C', 'K', 'H'],[2, 'D', 7, 'S', 'T', 'D', 'T', 'H', 6, 'D'],['J', 'D', 8, 'D', 4, 'D', 2, 'H', 5, 'S'],[8, 'S', 'Q', 'H', 'K', 'D', 'J', 'D', 'Q', 'S'],['J', 'H', 4, 'D', 'K', 'C', 5, 'H', 3, 'S'],[3, 'C', 'K', 'H', 'Q', 'C', 6, 'D', 8, 'H'],[3, 'S', 'A', 'H', 7, 'D', 'T', 'D', 2, 'D'],[5, 'S', 9, 'H', 'Q', 'H', 4, 'S', 6, 'S'],[6, 'C', 6, 'D', 'T', 'S', 'T', 'H', 7, 'S'],[6, 'C', 4, 'C', 6, 'D', 'Q', 'S', 'J', 'S'],[9, 'C', 'T', 'S', 3, 'H', 8, 'D', 8, 'S'],['J', 'S', 5, 'C', 7, 'S', 'A', 'S', 2, 'C'],['A', 'H', 2, 'H', 'A', 'D', 5, 'S', 'T', 'C'],['K', 'D', 6, 'C', 9, 'C', 9, 'D', 'T', 'S'],[2, 'S', 'J', 'C', 4, 'H', 2, 'C', 'Q', 'D'],['Q', 'S', 9, 'H', 'T', 'C', 3, 'H', 'K', 'C'],['K', 'S', 4, 'H', 3, 'C', 'A', 'D', 'T', 'H'],['K', 'H', 9, 'C', 2, 'H', 'K', 'D', 9, 'D'],['T', 'C', 7, 'S', 'K', 'C', 'J', 'H', 2, 'D'],[7, 'C', 3, 'S', 'K', 'C', 'A', 'S', 8, 'C'],[5, 'D', 9, 'C', 9, 'S', 'Q', 'H', 3, 'H'],[2, 'D', 8, 'C', 'T', 'D', 4, 'C', 2, 'H'],['Q', 'C', 5, 'D', 'T', 'C', 2, 'C', 7, 'D'],['K', 'S', 4, 'D', 6, 'C', 'Q', 'H', 'T', 'D'],['K', 'H', 5, 'D', 7, 'C', 'A', 'D', 8, 'D'],[2, 'S', 9, 'S', 8, 'S', 4, 'C', 8, 'C'],[3, 'D', 6, 'H', 'Q', 'D', 7, 'C', 7, 'H'],[6, 'C', 8, 'S', 'Q', 'H', 5, 'H', 'T', 'S'],[5, 'C', 3, 'C', 4, 'S', 2, 'S', 2, 'H'],[8, 'S', 6, 'S', 2, 'H', 'J', 'C', 3, 'S'],[3, 'H', 9, 'D', 8, 'C', 2, 'S', 7, 'H'],['Q', 'C', 2, 'C', 8, 'H', 9, 'C', 'A', 'C'],['J', 'D', 4, 'C', 4, 'H', 6, 'S', 3, 'S'],[3, 'H', 3, 'S', 7, 'D', 4, 'C', 9, 'S'],[5, 'H', 8, 'H', 'J', 'C', 3, 'D', 'T', 'C'],['Q', 'H', 2, 'S', 2, 'D', 9, 'S', 'K', 'D'],['Q', 'D', 9, 'H', 'A', 'D', 6, 'D', 9, 'C'],[8, 'D', 2, 'D', 'K', 'S', 9, 'S', 'J', 'C'],[4, 'C', 'J', 'D', 'K', 'C', 4, 'S', 'T', 'H'],['K', 'H', 'T', 'S', 6, 'D', 4, 'D', 5, 'C'],['K', 'D', 5, 'H', 'A', 'S', 9, 'H', 'A', 'D'],['Q', 'D', 'J', 'S', 7, 'C', 6, 'D', 5, 'D'],[5, 'C', 'T', 'H', 5, 'H', 'Q', 'H', 'Q', 'S'],[9, 'D', 'Q', 'H', 'K', 'H', 5, 'H', 'J', 'H'],[4, 'C', 4, 'D', 'T', 'C', 'T', 'H', 6, 'C'],['K', 'H', 'A', 'S', 'T', 'S', 9, 'D', 'K', 'D'],[9, 'C', 7, 'S', 4, 'D', 8, 'H', 5, 'S'],['K', 'H', 'A', 'S', 2, 'S', 7, 'D', 9, 'D'],[4, 'C', 'T', 'S', 'T', 'H', 'A', 'H', 7, 'C'],['K', 'S', 4, 'D', 'A', 'C', 8, 'S', 9, 'S'],[8, 'D', 'T', 'H', 'Q', 'H', 9, 'D', 5, 'C'],[5, 'D', 5, 'C', 8, 'C', 'Q', 'S', 'T', 'C'],[4, 'C', 3, 'D', 3, 'S', 2, 'C', 8, 'D'],[9, 'D', 'K', 'S', 2, 'D', 3, 'C', 'K', 'C'],[4, 'S', 8, 'C', 'K', 'H', 6, 'C', 'J', 'C'],[8, 'H', 'A', 'H', 6, 'H', 7, 'D', 7, 'S'],['Q', 'D', 3, 'C', 4, 'C', 6, 'C', 'K', 'C'],[3, 'H', 2, 'C', 'Q', 'H', 8, 'H', 'A', 'S'],[7, 'D', 4, 'C', 8, 'C', 4, 'H', 'K', 'C'],['Q', 'D', 5, 'S', 4, 'H', 2, 'C', 'T', 'D'],['A', 'H', 'J', 'H', 'Q', 'H', 4, 'C', 8, 'S'],[3, 'H', 'Q', 'S', 5, 'S', 'J', 'S', 8, 'H'],[2, 'S', 9, 'H', 9, 'C', 3, 'S', 2, 'C'],[6, 'H', 'T', 'S', 7, 'S', 'J', 'C', 'Q', 'D'],['A', 'C', 'T', 'D', 'K', 'C', 5, 'S', 3, 'H'],['Q', 'H', 'A', 'S', 'Q', 'S', 7, 'D', 'J', 'C'],['K', 'C', 2, 'C', 4, 'C', 5, 'C', 5, 'S'],['Q', 'H', 3, 'D', 'A', 'S', 'J', 'S', 4, 'H'],[8, 'D', 7, 'H', 'J', 'C', 2, 'S', 9, 'C'],[5, 'D', 4, 'D', 2, 'S', 4, 'S', 9, 'D'],[9, 'C', 2, 'D', 'Q', 'S', 8, 'H', 7, 'H'],[6, 'D', 7, 'H', 3, 'H', 'J', 'S', 'T', 'S'],['A', 'C', 2, 'D', 'J', 'H', 7, 'C', 8, 'S'],['J', 'H', 5, 'H', 'K', 'C', 3, 'C', 'T', 'C'],[5, 'S', 9, 'H', 4, 'C', 8, 'H', 9, 'D'],[8, 'S', 'K', 'C', 5, 'H', 9, 'H', 'A', 'D'],['K', 'S', 9, 'D', 'K', 'H', 8, 'D', 'A', 'H'],['J', 'C', 2, 'H', 9, 'H', 'K', 'S', 6, 'S'],[3, 'H', 'Q', 'C', 5, 'H', 'A', 'H', 9, 'C'],[5, 'C', 'K', 'H', 5, 'S', 'A', 'D', 6, 'C'],['J', 'C', 9, 'H', 'Q', 'C', 9, 'C', 'T', 'D'],[5, 'S', 5, 'D', 'J', 'C', 'Q', 'H', 2, 'D'],['K', 'S', 8, 'H', 'Q', 'S', 2, 'H', 'T', 'S'],['J', 'H', 5, 'H', 5, 'S', 'A', 'H', 7, 'H'],[3, 'C', 8, 'S', 'A', 'S', 'T', 'D', 'K', 'H'],[6, 'H', 3, 'D', 'J', 'D', 2, 'C', 4, 'C'],['K', 'C', 7, 'S', 'A', 'H', 6, 'C', 'J', 'H'],[4, 'C', 'K', 'S', 9, 'D', 'A', 'D', 7, 'S'],['K', 'C', 7, 'D', 8, 'H', 3, 'S', 9, 'C'],[7, 'H', 5, 'C', 5, 'H', 3, 'C', 8, 'H'],['Q', 'C', 3, 'D', 'K', 'H', 6, 'D', 'J', 'C'],[2, 'D', 4, 'H', 5, 'D', 7, 'D', 'Q', 'C'],['A', 'D', 'A', 'H', 9, 'H', 'Q', 'H', 8, 'H'],['K', 'D', 8, 'C', 'J', 'S', 9, 'D', 3, 'S'],[3, 'C', 2, 'H', 5, 'D', 6, 'D', 2, 'S'],[8, 'S', 6, 'S', 'T', 'S', 3, 'C', 6, 'H'],[8, 'D', 5, 'S', 3, 'H', 'T', 'D', 6, 'C'],['K', 'S', 3, 'D', 'J', 'H', 9, 'C', 7, 'C'],[9, 'S', 'Q', 'S', 5, 'S', 4, 'H', 6, 'H'],[7, 'S', 6, 'S', 'T', 'H', 4, 'S', 'K', 'C'],['K', 'D', 3, 'S', 'J', 'C', 'J', 'H', 'K', 'S'],[7, 'C', 3, 'C', 2, 'S', 6, 'D', 'Q', 'H'],[2, 'C', 7, 'S', 5, 'H', 8, 'H', 'A', 'H'],['K', 'C', 8, 'D', 'Q', 'D', 6, 'D', 'K', 'H'],[5, 'C', 7, 'H', 9, 'D', 3, 'D', 9, 'C'],[6, 'H', 2, 'D', 8, 'S', 'J', 'S', 9, 'S'],[2, 'S', 6, 'D', 'K', 'C', 7, 'C', 'T', 'C'],['K', 'D', 9, 'C', 'J', 'H', 7, 'H', 'K', 'C'],[8, 'S', 2, 'S', 7, 'S', 3, 'D', 6, 'H'],[4, 'H', 9, 'H', 2, 'D', 4, 'C', 8, 'H'],[7, 'H', 5, 'S', 8, 'S', 2, 'H', 8, 'D'],['A', 'D', 7, 'C', 3, 'C', 7, 'S', 5, 'S'],[4, 'D', 9, 'H', 3, 'D', 'J', 'C', 'K', 'H'],[5, 'D', 'A', 'S', 7, 'D', 6, 'D', 9, 'C'],['J', 'C', 4, 'C', 'Q', 'H', 'Q', 'S', 'K', 'H'],['K', 'D', 'J', 'D', 7, 'D', 3, 'D', 'Q', 'S'],['Q', 'C', 8, 'S', 6, 'D', 'J', 'S', 'Q', 'D'],[6, 'S', 8, 'C', 5, 'S', 'Q', 'H', 'T', 'H'],[9, 'H', 'A', 'S', 'A', 'C', 2, 'C', 'J', 'D'],['Q', 'C', 'K', 'S', 'Q', 'H', 7, 'S', 3, 'C'],[4, 'C', 5, 'C', 'K', 'C', 5, 'D', 'A', 'H'],[6, 'C', 4, 'H', 9, 'D', 'A', 'H', 2, 'C'],[3, 'H', 'K', 'D', 3, 'D', 'T', 'S', 5, 'C'],['T', 'D', 8, 'S', 'Q', 'S', 'A', 'S', 'J', 'S'],[3, 'H', 'K', 'D', 'A', 'C', 4, 'H', 'K', 'S'],[7, 'D', 5, 'D', 'T', 'S', 9, 'H', 4, 'H'],[4, 'C', 9, 'C', 2, 'H', 8, 'C', 'Q', 'C'],[2, 'C', 7, 'D', 9, 'H', 4, 'D', 'K', 'S'],[4, 'C', 'Q', 'H', 'A', 'D', 'K', 'D', 'J', 'S'],['Q', 'D', 'A', 'D', 'A', 'H', 'K', 'H', 9, 'D'],['J', 'S', 9, 'H', 'J', 'C', 'K', 'D', 'J', 'D'],[8, 'S', 3, 'C', 4, 'S', 'T', 'S', 7, 'S'],[4, 'D', 5, 'C', 2, 'S', 6, 'H', 7, 'C'],['J', 'S', 7, 'S', 5, 'C', 'K', 'D', 6, 'D'],['Q', 'H', 8, 'S', 'T', 'D', 2, 'H', 6, 'S'],['Q', 'H', 6, 'C', 'T', 'C', 6, 'H', 'T', 'D'],[4, 'C', 9, 'D', 2, 'H', 'Q', 'C', 8, 'H'],[3, 'D', 'T', 'S', 4, 'D', 2, 'H', 6, 'H'],[6, 'S', 2, 'C', 7, 'H', 8, 'S', 6, 'C'],[9, 'H', 9, 'D', 'J', 'D', 'J', 'H', 3, 'S'],['A', 'H', 2, 'C', 6, 'S', 3, 'H', 8, 'S'],[2, 'C', 'Q', 'S', 8, 'C', 5, 'S', 3, 'H'],[2, 'S', 7, 'D', 3, 'C', 'A', 'D', 4, 'S'],[5, 'C', 'Q', 'C', 'Q', 'H', 'A', 'S', 'T', 'S'],[4, 'S', 6, 'S', 4, 'C', 5, 'H', 'J', 'S'],['J', 'H', 5, 'C', 'T', 'D', 4, 'C', 6, 'H'],['J', 'S', 'K', 'D', 'K', 'H', 'Q', 'S', 4, 'H'],['T', 'C', 'K', 'H', 'J', 'C', 4, 'D', 9, 'H'],[9, 'D', 8, 'D', 'K', 'C', 3, 'C', 8, 'H'],[2, 'H', 'T', 'C', 8, 'S', 'A', 'D', 9, 'S'],[4, 'H', 'T', 'S', 7, 'H', 2, 'C', 5, 'C'],[4, 'H', 2, 'S', 6, 'C', 5, 'S', 'K', 'S'],['A', 'H', 9, 'C', 7, 'C', 8, 'H', 'K', 'D'],['T', 'S', 'Q', 'H', 'T', 'D', 'Q', 'S', 3, 'C'],['J', 'H', 'A', 'H', 2, 'C', 8, 'D', 7, 'D'],[5, 'D', 'K', 'C', 3, 'H', 5, 'S', 'A', 'C'],[4, 'S', 7, 'H', 'Q', 'S', 4, 'C', 2, 'H'],[3, 'D', 7, 'D', 'Q', 'C', 'K', 'H', 'J', 'H'],[6, 'D', 6, 'C', 'T', 'D', 'T', 'H', 'K', 'D'],[5, 'S', 8, 'D', 'T', 'H', 6, 'C', 9, 'D'],[7, 'D', 'K', 'H', 8, 'C', 9, 'S', 6, 'D'],['J', 'D', 'Q', 'S', 7, 'S', 'Q', 'C', 2, 'S'],['Q', 'H', 'J', 'C', 4, 'S', 'K', 'S', 8, 'D'],[7, 'S', 5, 'S', 9, 'S', 'J', 'D', 'K', 'D'],[9, 'C', 'J', 'C', 'A', 'D', 2, 'D', 7, 'C'],[4, 'S', 5, 'H', 'A', 'H', 'J', 'H', 9, 'C'],[5, 'D', 'T', 'D', 7, 'C', 2, 'D', 6, 'S'],['K', 'C', 6, 'C', 7, 'H', 6, 'S', 9, 'C'],['Q', 'D', 5, 'S', 4, 'H', 'K', 'S', 'T', 'D'],[6, 'S', 8, 'D', 'K', 'S', 2, 'D', 'T', 'H'],['T', 'D', 9, 'H', 'J', 'D', 'T', 'S', 3, 'S'],['K', 'H', 'J', 'S', 4, 'H', 5, 'D', 9, 'D'],['T', 'C', 'T', 'D', 'Q', 'C', 'J', 'D', 'T', 'S'],['Q', 'S', 'Q', 'D', 'A', 'C', 'A', 'D', 4, 'C'],[6, 'S', 2, 'D', 'A', 'S', 3, 'H', 'K', 'C'],[4, 'C', 7, 'C', 3, 'C', 'T', 'D', 'Q', 'S'],[9, 'C', 'K', 'C', 'A', 'S', 8, 'D', 'A', 'D'],['K', 'C', 7, 'H', 'Q', 'C', 6, 'D', 8, 'H'],[6, 'S', 5, 'S', 'A', 'H', 7, 'S', 8, 'C'],[3, 'S', 'A', 'D', 9, 'H', 'J', 'C', 6, 'D'],['J', 'D', 'A', 'S', 'K', 'H', 6, 'S', 'J', 'H'],['A', 'D', 3, 'D', 'T', 'S', 'K', 'S', 7, 'H'],['J', 'H', 2, 'D', 'J', 'S', 'Q', 'D', 'A', 'C'],[9, 'C', 'J', 'D', 7, 'C', 6, 'D', 'T', 'C'],[6, 'H', 6, 'C', 'J', 'C', 3, 'D', 3, 'S'],['Q', 'C', 'K', 'C', 3, 'S', 'J', 'C', 'K', 'D'],[2, 'C', 8, 'D', 'A', 'H', 'Q', 'S', 'T', 'S'],['A', 'S', 'K', 'D', 3, 'D', 'J', 'D', 8, 'H'],[7, 'C', 8, 'C', 5, 'C', 'Q', 'D', 6, 'C']]
    stevilo_zmag = 0
    for i in range(1000):
        stevilo_zmag += katera_roka_zmaga(seznam_rok[2*i + 1], seznam_rok[2*i])
    return stevilo_zmag

def naloga55(n):
    '''How many Lychrel numbers are there below n?'''
    lychrel_stevec = 0
    for a in range(1, n + 1):
        a = a + int(str(a)[::-1])
        stevec = 1
        while not je_palindrom(a) and stevec < 50:
            a = a + int(str(a)[::-1])
            stevec += 1
        if stevec == 50 and not je_palindrom(a):
            lychrel_stevec += 1
    return lychrel_stevec

def naloga51():
    '''Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.'''
    #6-mestne in 2x ali 3x menjava ni.. ---- zadnje stevke ne gledam
    najmanjse_tako = 0
    for stevilo in range(56000, 10000000):
        for i in range(1, len(str(stevilo)) - 2):
            for j in range(i + 1, len(str(stevilo)) - 1):
                for k in range(j + 1, len(str(stevilo))):
                        c = stevilo
                        ni_stevec = 0
                        kazalec = True
                        for vrednost in range(10):
                            stevilo = (stevilo // 10**(i + 1)) * 10**(i + 1) + stevilo % 10**i + vrednost * 10**i
                            stevilo = (stevilo // 10**(j + 1)) * 10**(j + 1) + stevilo % 10**j + vrednost * 10**j
                            stevilo = (stevilo // 10**(k + 1)) * 10**(k + 1) + stevilo % 10**k + vrednost * 10**k
                            if not je_prastevilo(stevilo):
                                ni_stevec += 1
                            if ni_stevec > 2:
                                kazalec = False
                                break 
                        if kazalec and je_prastevilo(c):
                            return c

def naloga56():
    '''Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?'''
    najvecja_vsota = 0
    for a in range(1, 101):
        for b in range(1, 101):
            potenca = a ** b
            vsota = vsota_stevk(potenca)
            najvecja_vsota = max(najvecja_vsota, vsota)
    return najvecja_vsota

def naloga58():
    '''If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?'''
    n = 49
    kotne = 13
    prastevila = 8
    krog = 3
    while prastevila / kotne > 0.1:
        krog += 1
        kotne += 4
        for _ in range(4):
            n += krog * 2
            if je_prastevilo(n):
                prastevila += 1
    return n ** 0.5

def naloga63():
    '''How many n-digit positive integers exist which are also an nth power?'''
    koliko = 0
    for a in range(1,10):
        n = 1
        while len(str(a ** n)) == n:
            koliko += 1
            n +=1
    return koliko



def naloga61():
    '''Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.'''
    # 8-kotna stirimestna od 19 do 58, v mnozici vsa 4-mestna
    mnozica = [
        [],
        [],
        [],
        [k_kotno(3,i) for i in range(45, 141)],
        [k_kotno(4,i) for i in range(32, 100)],
        [k_kotno(5,i) for i in range(26, 82)],
        [k_kotno(6,i) for i in range(23, 71)],
        [k_kotno(7,i) for i in range(21, 64)]
    ]
    moznosti = [3, 4, 5, 6, 7]
    for i in range(19, 59):
        for tipi in list(itertools.permutations(moznosti)):
            konec = False
            tipi = [m for m in tipi]
            stevilo = k_kotno(8, i)
            zeljena = [stevilo]

            while tipi != [] and not konec:
                for k in tipi:
                    for ostanek in range(10, 100):
                        skok = False
                        zacetek = stevilo % 100
                        preverjam = zacetek * 100 + ostanek
                        if preverjam in mnozica[k]:
                            stevilo = preverjam
                            zeljena.append(stevilo)
                            tipi.remove(k)
                            skok = True
                            break
                        if skok:
                            break
                    if ostanek == 99 :
                            konec = True
                            
            if len(zeljena) == 6 and (zeljena[5] % 100) == (zeljena[0] // 100):
                return sum(zeljena)

def naloga57(n):
    '''In the first n expansions (of sqrt(2)), how many fractions contain a numerator with more digits than denominator?'''
    resitev = 0
    st, im = (3,2)
    for _ in range(n - 1):
        st, im = 2 * im + st, st + im
        if len(str(st)) > len(str(im)):
            resitev += 1
    return resitev


def naloga67():
    '''Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a triangle with one-hundred rows.'''
    resitve= {}
    trikotnik = []
    with open('p067_triangle.txt', 'r') as dat:
        for line in dat.readlines():
            line = [int(a) for a in line.split()]
            trikotnik.append(line)
        
    def trikotna_vsota(n, i):
        if n == 99:
            resitve[(n, i)] = trikotnik[n][i]
        elif (n, i) not in resitve:
            resitve[(n,i)] = max(trikotna_vsota(n + 1, i), trikotna_vsota(n + 1, i +1)) + trikotnik[n][i]
        return resitve[(n,i)]
    return trikotna_vsota(0, 0)

def naloga76(n):
    '''How many different ways can n be written as a sum of at least two positive integers?'''
    moznosti = [0] * (n + 1)

    moznosti[0] = 1

    for i in range(1, n):
        for j in range(i, n + 1):
            moznosti[j] += moznosti[j - i]
    return moznosti[n]


def naloga77(n):
    '''What is the first value which can be written as the sum of primes in over n different ways?'''
    seznam_prastevil = [2]
    k = 3
    i = 5
    while True:
        i += 1
        while seznam_prastevil[-1] < i:
            kazalec = True
            for a in seznam_prastevil:
                if k % a == 0:
                    kazalec = False
                    break
            if kazalec:
                seznam_prastevil.append(k)
            k += 1
        #naloga31(n, seznam) vrne stevilo moznih zapisov stevila n z vrednostmi iz seznama
        if naloga31(i, seznam_prastevil) > n:
            return(i)

            
def naloga71(n):
    '''By listing the set of reduced proper fractions for d ≤ n in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.'''
    ulomki = []
    for im in range(2, n + 1):
        for st in range(int(im * 3/7),int(im * 3/7) + 1):
            if gcd(st, im) == 1:
                ulomki.append([st / im, (st, im)])
    ulomki.sort()
    polozaj = ulomki.index([3/7, (3,7)])
    return ulomki[polozaj - 1][1][0]


def naloga73(n):
    '''How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ n?'''
    ulomki = []
    for im in range(2, n + 1):
        for st in range(int(im * 1/3),int(im * 1/2) + 1):
            if gcd(st, im) == 1:
                ulomki.append([st / im, (st, im)])
    ulomki.sort()
    polozaj1 = ulomki.index([1/2, (1,2)])
    polozaj2 = ulomki.index([1/3, (1,3)])

    return polozaj1 - polozaj2 - 1



def naloga97():
    '''However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.
    Find the last ten digits of this prime number.'''
    n = 7830457
    stevilo = 28433
    for _ in range(n):
        stevilo *= 2
        stevilo = stevilo % 10 ** 10
    return stevilo + 1
    

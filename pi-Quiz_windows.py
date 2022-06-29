import sys
import msvcrt

f_pi = open(r'pi-Quiz\pi-zahl.txt', 'r')
pi = f_pi.read()

print('Willkommen bei pi-Game. Versuche, so viele Kommastellen der pi-Zahl wie möglich zu erraten.\n')

def getPi():
    count = 0
    while True:
        nutzereingabe = msvcrt.getwch()
        pi_zahl = pi[int(count)]
        if nutzereingabe in pi_zahl:
            count += 1
            continue
        else:
            print('\n\nDu hast verloren! Die nächste Ziffer ist: ' + pi[count] + '. Du konntest bisher ' + str(count) + ' Ziffer(n) der pi-Zahl erraten\nNeuer Versuch!\n')
            getPi()

getPi()
HARFLER = u'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
HARFDONUSUM = [(u'i', u'İ'), (u'ğ', u'Ğ'), (u'ü', u'Ü'), (u'ş', u'Ş'), (u'ö', u'Ö'), (u'ç', u'Ç'), (u'ı', u'I')]


def buyult(s):
    for x, y in HARFDONUSUM:
        s = s.replace(x, y)
    return s.upper()


def kucult(s):
    for x, y in HARFDONUSUM:
        s = s.replace(y, x)
    return s.lower()


def iletiDonustur(anahtar, ileti, kip):    
    donusturulmus = []

    anahtarIndex = 0
    anahtar = buyult(anahtar)

    for harf in ileti:
        num = HARFLER.find(buyult(harf))
        if num != -1:
            if kip == 'sifrele':
                num += HARFLER.find(anahtar[anahtarIndex])
            elif kip == 'desifrele':
                num -= HARFLER.find(anahtar[anahtarIndex])

            num %= len(HARFLER)

            if harf.isupper():
                donusturulmus.append(HARFLER[num])
            elif harf.islower():
                donusturulmus.append(kucult(HARFLER[num]))

            anahtarIndex += 1
            if anahtarIndex == len(anahtar):
                anahtarIndex = 0
        else:
            donusturulmus.append(harf)

    return ''.join(donusturulmus)

print ("\n","SONUÇ:","\n")
print (iletiDonustur(u'anahtar kelimenizi yazın', u'şifrelenecek metni yazın', 'sifrele'))


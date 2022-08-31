vuosi=int(input('Anna vuosi: '))
if vuosi/100==int(vuosi/100) and vuosi/400==int(vuosi/400):
    print('Vuosi on karkausvuosi.')
elif vuosi/4==int(vuosi/4):
    print('Vuosi on karkausvuosi.')
else:
    print('Vuosi ei ole karkausvuosi')
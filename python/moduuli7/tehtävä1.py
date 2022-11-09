vuodenAjat=('kesä', 'syksy', 'talvi', 'kevät')
kuukausi=int(input('Anna kuukausi numerona: '))
if kuukausi in (1, 2, 12):
    print(vuodenAjat[2])
elif kuukausi in (3, 4, 5):
    print(vuodenAjat[3])
elif kuukausi in (6, 7, 8):
    print(vuodenAjat[0])
elif kuukausi in (9, 10, 11):
    print(vuodenAjat[1])
else: print('Numero ei vastaa mitään kuukautta')
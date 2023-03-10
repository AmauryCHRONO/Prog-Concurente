import sys
if len(sys.argv)>2:
    for mot in sys.argv[1:]:
        miroir=""
        for lettre in mot:
            miroir=lettre+miroir
        print(miroir)
    
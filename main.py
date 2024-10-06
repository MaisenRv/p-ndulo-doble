from src.sketch import *
# import ctypes

def main():
    run(frame_rate=40, renderer='skia')
    # rg = ctypes.CDLL('./src/runge-kutta/rk.dll')

    # print(f'desde DLL {rg.contar()}')
    # con = 0
    # for i in range(0,1000000000):
    #     con += 1
    # print(f'Termino {con}')
    

if __name__ == '__main__':
    main()
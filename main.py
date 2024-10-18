from src.sketch import *
import ctypes

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
rg = ctypes.CDLL('./src/runge-kutta/rk.dll')
# rg.f1.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
# rg.f1.restype = ctypes.c_double
# rg.f2.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
# rg.f2.restype = ctypes.c_double

rg.runge_kutta.argtypes = [ctypes.c_float, ctypes.POINTER(ctypes.c_float)]
rg.runge_kutta.restype = None


def main():
    run(frame_rate=80, renderer='skia')

    # te1= np.pi/2
    # te2 = np.pi
    # S0=(0,0,te1,te2)
    # tiempo = np.array([0,5])
    # sol = solve_ivp(f1,tiempo,S0,max_step=1)
    # sol1 = solve_ivp(f2,tiempo,S0,max_step=0.001)
    # plt.plot(sol.t, sol.y[1],label='v1')
    # plt.plot(sol.t, sol.y[0],label='a1')
    # plt.plot(sol.t, sol.y[3],label='v2')
    # plt.plot(sol.t, sol.y[2],label='a2')
    # plt.legend()
                # plt.plot(sol1.t, sol1.y[0],'--')
                # plt.plot(sol1.t, sol1.y[1],'--')
                # print(sol1.y[1])
    # plt.show()

    # h = 0.1
    # con_iniciales = np.array([0.0, 0.0, np.pi / 2, np.pi], dtype=np.float32)
    # for _ in range(10000):  # Cambia 100 por el número de pasos que necesites
    #     rg.runge_kutta(h, con_iniciales.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))
    #     print(f"v1: {con_iniciales[0]}, v2: {con_iniciales[1]}, angulo1: {con_iniciales[2]}, angulo2: {con_iniciales[3]}")



    pass

m1=0.067
m2=0.008
l1=0.13
l2=0.1

# def f1(t,S):
    # global m1,m2,l1,l2,rg,con
    # y,z,te1,te2=S
    # A=np.cos(te1-te2)
    # B=np.sin(te1-te2)
    # C = y-z
    # D= m1+ m2
    # g=9.8


    # n1 = -m2*l1*y*A*B*(C+z)
    # n2 = m2*l2*z*B*(C-y)
    # n3 = -g*(m2*np.sin(te2)*A + np.sin(te1)*D)
    # de = l1*(D-m2*A*A)
   


    # f1_res = np.float64(rg.f1(np.float64(te1), np.float64(te2), np.float64(m1), np.float64(m2), np.float64(y), np.float64(z), np.float64(l1), np.float64(l2)))
    # f1_res = ( n1 + n2 - n3)/(de)
    # f2_res = np.float64(rg.f2(np.float64(te1), np.float64(te2), np.float64(m1), np.float64(m2), np.float64(y), np.float64(z), np.float64(l1), np.float64(l2)))
    # f2_res = (l1*y*B*(C+z) - g*(A*np.sin(te1)+np.sin(te2)) - ((m2*l2*z*A*B)/(D))*(C-y) )/(l2-((m2*l2*A*A)/(D)))
    # print(f'{t}  {y}')
    # return [f1_res, y, f2_res,z ]
    # return [y,z, f1_res,f2_res]


if __name__ == '__main__':
    main()
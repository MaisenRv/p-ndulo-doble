#include <stdio.h>
#include <math.h>

// #define M_1 0.067  // Masa 1
#define M_1 3  // Masa 1
// #define M_2 0.067 // Masa 2
#define M_2 2 // Masa 2
// #define M_2 0.008 // Masa 2
#define L_1 5// Longitud 1
#define L_2 5 // Longitud 2
#define G -9.81   // Gravedad
const double PI = 3.14159265358979323846;



float func1(float v1_inicial){
    return v1_inicial;
}
float func2(float v2_inicial){
    return v2_inicial;
}

float func3(float v1_inicial, float v2_inicial, float angulo1, float angulo2){
    float A = -cos(angulo1+angulo2);
    float B = sin(angulo1-angulo2);
    float C = v1_inicial - v2_inicial;
    float D = M_1 + M_2;

    return (-M_2 * L_1 * v1_inicial * A * B * (C+v2_inicial) + 
            M_2 * L_2 * v2_inicial * B * (C-v1_inicial)  +  
            G * ( M_2 * sin(angulo2) * A + sin(angulo1) * D )) / 
            (L_1 * (D - M_2 * A * A)); 
}
float func4(float v1_inicial, float v2_inicial, float angulo1, float angulo2){
    float A = -cos(angulo1+angulo2);
    float B = sin(angulo1-angulo2);
    float C = v1_inicial-v2_inicial;
    float D = M_1 + M_2;
    return (L_1 * v1_inicial * B * (C + v2_inicial) + 
            G * (A * sin(angulo1) + sin(angulo2)) - 
            ((M_2 * L_2 * v2_inicial * A * B) / D) * (C - v1_inicial)) / 
            (L_2 - ((M_2 * L_2 * A * A) / D));
}

// void runge_kutta(float h, float* con_iniciales){
//     const int tamano = 4;
//     float k1[tamano], k2[tamano], k3[tamano], k4[tamano];

//     // Cálculo de k1
//     k1[2] = h * func1(con_iniciales[0]);  // Velocidad 1
//     k1[3] = h * func2(con_iniciales[1]);  // Velocidad 2
//     k1[0] = h * func3(con_iniciales[0], con_iniciales[1], con_iniciales[2], con_iniciales[3]);  // Aceleración 1
//     k1[1] = h * func4(con_iniciales[0], con_iniciales[1], con_iniciales[2], con_iniciales[3]);  // Aceleración 2

//     // Cálculo de k2
//     k2[2] = h * func1(con_iniciales[0] + 0.5 * k1[0]);  // Velocidad 1
//     k2[3] = h * func2(con_iniciales[1] + 0.5 * k1[1]);  // Velocidad 2
//     k2[0] = h * func3(con_iniciales[0] + 0.5 * k1[0], con_iniciales[1] + 0.5 * k1[1], con_iniciales[2] + 0.5 * k1[2], con_iniciales[3] + 0.5 * k1[3]);  // Aceleración 1
//     k2[1] = h * func4(con_iniciales[0] + 0.5 * k1[0], con_iniciales[1] + 0.5 * k1[1], con_iniciales[2] + 0.5 * k1[2], con_iniciales[3] + 0.5 * k1[3]);  // Aceleración 2

//     // Cálculo de k3
//     k3[2] = h * func1(con_iniciales[0] + 0.5 * k2[0]);  // Velocidad 1
//     k3[3] = h * func2(con_iniciales[1] + 0.5 * k2[1]);  // Velocidad 2
//     k3[0] = h * func3(con_iniciales[0] + 0.5 * k2[0], con_iniciales[1] + 0.5 * k2[1], con_iniciales[2] + 0.5 * k2[2], con_iniciales[3] + 0.5 * k2[3]);  // Aceleración 1
//     k3[1] = h * func4(con_iniciales[0] + 0.5 * k2[0], con_iniciales[1] + 0.5 * k2[1], con_iniciales[2] + 0.5 * k2[2], con_iniciales[3] + 0.5 * k2[3]);  // Aceleración 2

//     // Cálculo de k4
//     k4[2] = h * func1(con_iniciales[0] + k3[0]);  // Velocidad 1
//     k4[3] = h * func2(con_iniciales[1] + k3[1]);  // Velocidad 2
//     k4[0] = h * func3(con_iniciales[0] + k3[0], con_iniciales[1] + k3[1], con_iniciales[2] + k3[2], con_iniciales[3] + k3[3]);  // Aceleración 1
//     k4[1] = h * func4(con_iniciales[0] + k3[0], con_iniciales[1] + k3[1], con_iniciales[2] + k3[2], con_iniciales[3] + k3[3]);  // Aceleración 2

//     // Actualización de los valores de con_iniciales
//     for (int i = 0; i < 4; i++) {
//         con_iniciales[i] += (1.0 / 6.0) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]);
//     }
// }



void runge_kutta(float h, float* con_iniciales){
    const int tamano = 4;
    float k1[tamano],k2[tamano],k3[tamano],k4[tamano];


    k1[0] = h * func3(con_iniciales[0],con_iniciales[1],con_iniciales[2],con_iniciales[3]);
    k1[1] = h * func4(con_iniciales[0],con_iniciales[1],con_iniciales[2],con_iniciales[3]);
    k1[2] = h * func1(con_iniciales[0]);
    k1[3] = h * func2(con_iniciales[1]);
    
    k2[0] = h * func3(con_iniciales[0]+ 0.5 * k1[0],con_iniciales[1]+ 0.5 * k1[1],con_iniciales[2]+ 0.5 * k1[2],con_iniciales[3]+ 0.5 * k1[3]);
    k2[1] = h * func4(con_iniciales[0]+ 0.5 * k1[0],con_iniciales[1]+ 0.5 * k1[1],con_iniciales[2]+ 0.5 * k1[2],con_iniciales[3]+ 0.5 * k1[3]);
    k2[2] = h * func1(con_iniciales[0]+ 0.5 * k1[0]);
    k2[3] = h * func2(con_iniciales[1]+ 0.5 * k1[1]);

    k3[0] = h * func3(con_iniciales[0]+ 0.5 *k2[0],con_iniciales[1]+ 0.5 *k2[1],con_iniciales[2]+ 0.5 *k2[2],con_iniciales[3]+ 0.5 *k2[3]);
    k3[1] = h * func4(con_iniciales[0]+ 0.5 *k2[0],con_iniciales[1]+ 0.5 *k2[1],con_iniciales[2]+ 0.5 *k2[2],con_iniciales[3]+ 0.5 *k2[3]);
    k3[2] = h * func1(con_iniciales[0]+ 0.5 *k2[0]);
    k3[3] = h * func2(con_iniciales[1]+ 0.5 *k2[1]);

    k4[0] = h * func3(con_iniciales[0]+ k3[0],con_iniciales[1]+ k3[1],con_iniciales[2]+ k3[2],con_iniciales[3]+ k3[3]);
    k4[1] = h * func4(con_iniciales[0]+ k3[0],con_iniciales[1]+ k3[1],con_iniciales[2]+ k3[2],con_iniciales[3]+ k3[3]);
    k4[2] = h * func1(con_iniciales[0]+ k3[0]);
    k4[3] = h * func2(con_iniciales[1]+ k3[1]);

    for (int i = 0; i < 4; i++) {
        con_iniciales[i] += (1.0 / 6.0) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]);
    }
}


// void main(){
//     float res[4] = {0.0,0.0,PI/2,PI};
//     float h = 0.1;
//     for (int i = 0; i < 10000; i++){
//         runge_kutta(h,res);
//         printf("I= %i  v1: %.5f  v2:  %.5f  angulo1: %.5f  angulo2: %.5f\n",i,res[0],res[1],res[2],res[3]);
//     }
    
// }

// UTILIZADAS --------------------------------
// double f1(double te1, double te2, double m1, double m2, double y1, double y2, double l1, double l2){
//     double A=cos(te1-te2);
//     double B=sin(te1-te2);
//     double C = y1-y2;
//     double D= m1+ m2;

//     double n1 = -m2*l1*y1*A*B*(C+y2);
//     double n2 = m2*l2*y2*B*(C-y1);
//     double n3 = G*(m2*sin(te2)*A + sin(te1)*D);
//     double de = l1*(D-m2*A*A);

//     return ( n1 + n2 - n3)/(de);
// }

// double f2(double te1, double te2, double m1, double m2, double y1, double y2, double l1, double l2){
//     double A=cos(te1-te2);
//     double B=sin(te1-te2);
//     double C = y1-y2;
//     double D= m1+ m2;
    
//     double res = (l1*y1*B*(C+y2) + G*(A*sin(te1)+sin(te2)) - ((m2*l2*y2*A*B)/(D))*(C-y1) )/(l2-((m2*l2*A*A)/(D)));
//     return res;
// }
// --------------------------------

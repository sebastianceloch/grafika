clear;
clc;

M=[2.541, 2.112; 1.872, 1.556];

b=[4.653; 3.428];

E=[0.001, 0.001;-0.001, -0.001];

disp(M);

function y=wz2(C);
    y=C(1,1)*C(2,2)-C(2,1)*C(1,2);
endfunction;

wz2(M);

//function C=msum(A,B);
//    C(1,1)=A(1,1)+B(1,1);
//    C(1,2)=A(1,2)+B(1,2);
//    C(2,1)=A(2,1)+B(2,1);
//    C(2,2)=A(2,2)+B(2,2);
//endfunction;

function C=msum(A,B); /*sumowanie macierzy*/
    C=A+B;
endfunction;

function Wk=Cmk(A,w,k);  /*wyliczanie wyznacznika macierzy*/
    Wk=A;
    Wk(:,k)=w; 
endfunction;

ME=msum(M,E);
dME=wz2(ME);
if dME<>0  then
    //metoda Cramera
    x(1,1)=wz2(Cmk(ME,b,1))/dME;
    x(2,1)=wz2(Cmk(ME,b,2))/dME;
    disp("x=",x);
else
    //nie ma rozwiązań
    disp("nic");
    
end

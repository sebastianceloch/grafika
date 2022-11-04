clear;
clc;

M=[1,2
   1,1];

E=[0.0,0.0
   0.0,0.0];

b=[4.653
   3.428];

disp(M);
disp(E);
disp(b);

function y=wz2(C);
    y=C(1,1)*C(2,2)-C(1,2)*C(2,1);
endfunction;

function C=msum(A,B);
    C=A+B;
endfunction;

function Wk=Cmk(A,w,k);
    Wk=A;
    Wk(:,k)=w;
endfunction;

ME=msum(M,E);
dME=wz2(ME);
if dME<>0 then
    x(1,1)=wz2(Cmk(ME,b,1))/dME;
    x(2,1)=wz2(Cmk(ME,b,2))/dME;
    disp("x=",x);
else
    disp("wyznacznik glowny zerowy = brak rozwiazan ukladu");
end
wz2(ME);

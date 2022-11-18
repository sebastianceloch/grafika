//Celoch Sebastian Informatyka Ogólna gr1 162298 Kolokwium nr 1 wersja A
clear;
clc;
clf;
disp("Sebastian Celoch Informatyka rok 3, specjalność Informatyka Ogólna");
i=5;
for x=0:i;
    xw(x+1)=cos(x-1);
end;
yw=xw';
disp("yw= ",yw);

for j = 1:14,
  if modulo(j,2)==0 then
    zw(j)=exp(sin(j));
    disp("zi = ",zw(j));
  else
  end;
end;

function y=f(x,y);
    y=sin(x)^2+cos(y)^2;
endfunction;

disp("f(0.15,1.15)= ",f(0.15,1.15));

X=ones(3,3);
for i=1:9;
    for j=1:9;
        X([i,j])=1/(i+j);
    end;
end;
disp(X);

function y=det2(C);
    y=C(1,1)*C(2,2)-C(1,2)*C(2,1);
endfunction;

A=[1,2
    2,3];
    
dA=det2(A);
disp("wyznacznik macierzy A =",dA);

function y=g(x);
    if x>=0 then
        y=cos(x)+sin(x);
    else
        y=exp(x);
    end
endfunction;

l=-5;
p=5;
lp=100;
tw=linspace(l,p,lp);

for i=1:lp;
    x(i)=g(i);
end

plot(tw,x');


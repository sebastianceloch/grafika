clear;
clc;
a=-2;
b=0.5;
r=4;
nmax=50;
h=0.001
 
function y=f(x)
    y=(x^2-3)*sin(x);
endfunction;
 
function y=fp(x,h)
    y=(f(x+h)-f(x))/h;
endfunction;
 
function y=fpp(x,h)
    y=(fp(x+h)-fp(x))/h;
endfunction;
 
wi=1;
xr(wi)=a;
 
kw=0;
if f(a)*f(b)<0 then
    while (fp(a,h)*fp(b,h)>0 && fpp(a,h)*fpp(b,h)>0) then
        if wi < nmax then
            kw=1;
            break;
        end;
        wi = wi + 1;
        xr(wi)=(a+b)/2;
        if abs(xr(wi)-xr(wi-1))<10^(-r) then
            kw=2;
            break;
        end;
        if f(a)*f(xr(wi))<0 then
            b=xr(wi);
        else
            a=xr(wi);
        end;
    end;
    
    if kw==0 then;
        wi=wi+1;
        if fp(a,h)*fpp(a,h)<0 then;
            c=a;
            xr(wi)=b;
        else
            c=b;
            xr(wi)=a;
        end;
        kw=1;
        while wi<nmax then;
            wi=wi+1;
            xr(wi)=xr(wi-1)-f(xr(wi-1))*(c-xr(wi-1))/(f(c)-f(xr(wi-1)));
            if abs()<10^(-r) then;
                kw=2;
                break;
            end;
        end;
            

else;
    kw=3;
end;

select kw
case 1 then;
    disp("osiegnieto maksymalna dopuszczalna liczbe iteracji max="+string(nmax));
    disp("x("+string(wi)+")-"+string(x(wi)));
case 2 then;
    disp("osiagnieto dokladnosc rzedu"+string(r)+"miejsc po przecinku");
    disp("x("+string(wi)+")-"+string(x(wi)));
case 3 then;
    disp("xd?");
case 4 then;
end;
end;

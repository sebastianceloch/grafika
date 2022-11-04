clear; 
clc;
clf;

n=8;

for i = 0:n
    xw(i+1)=-6+2*i;
end;

function y=f(x);
    y=x*sin(x);
endfunction

for i = 0:n
    yw(i+1)=f(xw(i+1));
end;

X=ones(n+1,1);

for j = 2:(n+1)
    X(:,j)=X(:,j-1).*xw;
end
aw=X\yw;

function y =Wn(x,a,n);
y=a(1);
for i=1:n
y=y+a(i+1)*x^i;
end;
endfunction;


l=xw(1)-0.5;
p=xw(n+1)+0.5;
lp=300;
tw=linspace(l,p,lp)';
for i = 1:lp
    fw(i)=f(tw(i));
    Wnw(i)=Wn(tw(i),aw,n);
end;

plot(tw,fw);
plot(tw,Wnw,"r");
plot(xw,yw,"k.");

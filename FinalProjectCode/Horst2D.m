function [xx,y,foot]=Hsieh2D_JDA(ustar,Lo,sv,zo,zm)

k=0.4;
Lx=100*zm;
zu=zm*(log(zm/zo)-1+zo/zm);       
P=[0.59 1 1.33];                  
D=[0.28 0.97 2.44];
Mu=[100 500 2000];
stab=zu/Lo;
thresh=0.04;

if stab<-thresh
    ii=1;
elseif abs(stab)<thresh
    ii=2;
elseif stab>thresh
    ii=3;
end
D1=D(ii);
P1=P(ii);
Mu1=Mu(ii);

bin=floor(Lx/500);
x=[eps:bin:Lx];



c1=(-1/k/k)*(D1*zu^P1*abs(Lo)^(1-P1))./(x);
Fc=exp(c1);
Fp=-(c1./x).*Fc;
Xp=(1/2/k/k)*(D1*zu^P1*abs(Lo)^(1-P1));
F2H=(D1/0.105/k/k)*(zm^(-1)*abs(Lo)^(1-P1)*zu^(P1));
Xm=min([F2H*zm Lx]);

nn=floor((Xm+1)/bin)-1;
p11=0.86;a11=0.3;
sy=a11*zo*(sv/ustar).*(x./zo).^(p11);%------------------- CHECK
b=floor((a11*zo*(sv/ustar).*(Xm./zo).^p11)/1.5);
y=[-b:bin:b];

for i=1:nn
    foot(i,:)=Fp(i)*normpdf(y,0,sy(i));
end
xx=x(1:nn);

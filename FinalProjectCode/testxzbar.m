clear all

p=1.55; c=.6; a1=16; a2=16; b1=5; b2=5; k=0.41;% (Gryning et al 1983)
xo=0;  %ground level source
Lo=-10000;
zo=.05
zbar=[2:100];
phim=(1-a1*zbar/Lo).^(-1/4);
psi=(1./phim)-1;
x=(zbar/k^2).*(log(c*zbar/zo)-psi).*(1-p*a1*zbar/(4*Lo)).^0.5;
figure (1)
plot (x,zbar)

clear all

p=1.55; c=.6; a1=16; a2=16; b1=5; b2=5; k=0.41;% (Gryning et al 1983)

global  long_dist Lo zo;


xo=0;  %ground level source
xo=0;  %ground level source
Lo=10;
zo=.05
zbar=[2:100];
%phim=(1+b2*zbar/Lo);
%psi=-b2*zbar/Lo;
x=(zbar./k^2).*(log(c*zbar./zo)+2*b2*p*zbar./(3*Lo)).*(1+b1*p*zbar./(2*Lo))+(b1/4-b2/6)*p*zbar./Lo;


figure (2)
plot (x,zbar)




function [ F ] = A1stab(zbar)
%Mean plume height from Gryning for unstable conditions
p=1.55; c=.6; a1=16; a2=16; b1=5; b2=5; k=0.41;% (Gryning et al 1983)

global  long_dist Lo zo;


xo=0;  %ground level source
size(zbar)
size(Lo)
phim=(1+b2*zbar/Lo);
psi=-b2*zbar/Lo;
F=long_dist+xo-(zbar/k^2).*(log(c*zbar/zo)+2*b2*p*zbar/(3*Lo))*(1+b1*p*zbar/(2*Lo))+(b1/4-b2/6)*p*zbar/Lo;
end


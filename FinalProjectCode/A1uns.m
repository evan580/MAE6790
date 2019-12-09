function [ F ] = A1uns(zbar)
%Mean plume height from Gryning for unstable conditions
p=1.55; c=.6; a1=16; a2=16; b1=5; b2=5; k=0.41;% (Gryning et al 1983)

global  long_dist Lo zo;


xo=0;  %ground level source
phim=(1-a2*c*zbar/Lo).^(-1/4);
psi=(1./phim)-1;
F=long_dist+xo-(zbar/k^2).*(log(c*zbar/zo)-psi).*(1-p*a1*zbar/(4*Lo)).^0.5;
end


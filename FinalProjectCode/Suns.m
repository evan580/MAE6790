function [ s ] = Suns(zbar)
%Mean plume height from Gryning for unstable conditions
p=1.55; c=.6; a1=16; a2=16; b1=5; b2=5; k=0.41;% (Gryning et al 1983)

global Lo zo;

phim=(1-a2*c*zbar/Lo).^(-1/4);
psi=(1./phim)-1;

s=(1-a1*c*zbar/(2*Lo))/(1-a1*c*zbar/Lo)  + (1-a2*c*zbar/(Lo))^(-.25)/(log(c*zbar/zo)-psi);

end


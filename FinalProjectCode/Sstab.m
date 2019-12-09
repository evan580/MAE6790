function [ s ] = Sstab(zbar)
%Mean plume height from Gryning for unstable conditions
p=1.55; c=.6; a1=16; a2=16; b1=5; b2=5; k=0.41;% (Gryning et al 1983)

global  Lo zo;

phim=(1+b2*c*zbar/Lo);
psi=-b2*c*zbar/Lo;

s=(1+2*b1*c*zbar/Lo)/(1+b1*c*zbar/Lo) + phim/(log(c*zbar/zo)-psi);

end


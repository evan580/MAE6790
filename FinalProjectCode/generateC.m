% Generate a 100 x 100 matrix for concentrations
%x and y positions should be centers of each box
close all
clear all

Nx=100;Ny=100;  %number of grid cells is concentration mesh
Lx=5000; Ly=5000; %domain size
Dx=Lx/Nx;  Dy=Ly/Ny;    %Grid size;
C=zeros(Nx,Ny);         %Inititalize concentration matrix
X=Dx.*([1:Nx]-0.5);     %Vector of X coordinates at grid centers
Y=Dy.*([1:Ny]-0.5);     %Vector of X coordinates at grid centers
WindDir=90;              %Set wind direction as angle. 

%ustar=0.5;              %Friction velocity [m/s]
ustar=1.; 

                %Direction wind is coming from, clockwise from N
Lo=-1000;                   %Set Obukhov length parameter
zo=.05;                 %Set surface roughness lenght [m]
zm=2;                   %sensor height in [m]
stab=zm/Lo;             %Stability parameter
%Set parameters for vertical mixing 

%Run the geography set up script
sample_map              %By Ashleigh Swingler
Nw=length(wells)        %total number of wells

%Assign Well source strengths



p=1;          %probability of leaky well.
Sw=rand(1,Nw);    %uniform random distribution
Sw=floor(Sw-p);   
ii=find(Sw<0);     %ID location of leaky wells
Sw=Sw*0+100;         %Set nonleaky well source strength
Sw(ii)=2000000;       %Set leaky well source strength 

%loop over wells
for iw=1:Nw
    xw=well_positions(iw,1);  %well coordinates in global space
    yw=well_positions(iw,2);
    
    
%Loop over spatial grid cells
    for i=1:Nx
        
        for j=1:Ny
            [i j iw]
            x=X(i);      %coordinate position in global space
            y=Y(j);
%NEED to GENERALIZE next line for Wind Dir            
            long_dist=(xw-x);  %compute longitudinal distance from well to sensor along wind
            lat_dist=abs(yw-y);%compute lateral distance from well to sensor wrt wind direx
            if long_dist>0  %NEED TO SKIP ALL CALCS for Negative X distance...
                
                
            if (stab<=0)
                global long_dist zbar Lo zo
%                zbar = fsolve(@A1uns,1)  %Solve Gryning (A1) for mean plume height (WORKS)
                c=.6;k=0.41;
                zbar=((2/5).^(6/7))* (exp(1/7))*(k^(12/7))*((zo/c)^(1/7))* long_dist^(6/7);       
                s=Suns(zbar);            %Gryning A(2) for s  [SEEMS LOW!!!]
                U=Uuns(zbar,ustar);      %Gryning mean wind at center pf plume height
            else
%                zbar = fsolve(@A1stab,1)  %Solve Gryning (A1) for mean plume height (WORKS)
                c=.6; k=0.41;
                zbar=((2/5).^(6/7))* (exp(1/7))*(k^(12/7))*((zo/c)^(1/7))* long_dist^(6/7);       
                s=Sstab(zbar)             %Gryning A(2) for s
                U=Ustab(zbar,ustar);      %Gryning mean wind at center pf plume height
                
            end
            A=s*gamma(2/s)/(gamma(1/s))^2;   
            B=gamma(2/s)/gamma(1/s); 
            Dz=(A/zbar)*exp(-(B*zm/zbar)^s);%  Vertical dispersion (downwind)
            ay=.3;py=0.86;  %Actually weak functions of stability... for now set constant
            sigmay=ay*zo*1.9*(long_dist/zo)^py; %lateral dispersion after Eckman (1994)
            Dy=(1/(sqrt(2*pi)*sigmay))*exp(-0.5*(lat_dist/sigmay)^2);
            C_cont(i,j,iw)=Dy*Dz*Sw(iw)/U;  %concentration at x,y due to well # iw
            C(i,j)=C(i,j)+C_cont(i,j,iw);           %total concentration at x,y (summed over wells).
            
            end       %End of if for skipping calcs with negative x-distance
            
        end
    end
end
figure (2)
clf
pcolor (X,Y,C); colorbar
shading interp
xlabel (' X [m]')
ylabel (' Y [m]')
title ('CH4 Concentrations [ppb]')

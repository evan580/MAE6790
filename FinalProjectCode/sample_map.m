%   SAMPLE_MAP.M -- create a sample map for the EPA

close all;

%   Load and Crop Image 
    I = imread('satmap3.jpg', 'jpg'); 
    hold on
    I = imcrop(I , [85 10 950 950]); 
    %image(I)
    daspect([1 1 1]);
    
%   Load Well Positions 

    load('wells');
    well_positions = []; 
    for i = 1:length(wells); 
       well_positions(i,:) =  [wells(i).Position].*100/19; 
    end
    
    load('intersection_data'); 
    intersection_position = []; 
    for i = 1:length(intersection_data)
        intersection_position(i,:) = [intersection_data(i).Position].*100/19; 
    end
    
    load('adj'); 
    
    
    imagesc([0  length(I)*100/19], [0 length(I)*100/19], I);
    hold on 
    set(gca,'YDir','reverse')
    gplot(adj, intersection_position) 
    plot(well_positions(:,1), well_positions(:, 2), 'ro')
    axis tight
    xlabel('m'); ylabel('m')
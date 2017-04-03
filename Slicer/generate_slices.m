clc
close all
clear all
%% INPUT

stl_file='cone.stl';
slice_direction='y';
print_displacement=2e-6; %m
layer_displacement=4e-6; %m

%% Receive dimension from STL file

%Plot the original STL mesh:
figure
[stlcoords] = READ_stl(stl_file);
xco = squeeze( stlcoords(:,1,:) )';
yco = squeeze( stlcoords(:,2,:) )';
zco = squeeze( stlcoords(:,3,:) )';
[hpat] = patch(xco,yco,zco,'b');
axis equal


xco=max(reshape(xco,[],1)*1e-3); %m
yco=max(reshape(yco,[],1)*1e-3); %m
zco=max(reshape(zco,[],1)*1e-3); %m

switch slice_direction
     case 'x'
        xco=xco-mod(xco,layer_displacement);
        yco=yco-mod(yco,print_displacement);
        zco=zco-mod(zco,print_displacement);
     case 'y'
        xco=xco-mod(xco,print_displacement);
        yco=yco-mod(yco,layer_displacement);
        zco=zco-mod(zco,print_displacement);
     case 'z'
        xco=xco-mod(xco,print_displacement);
        yco=yco-mod(yco,print_displacement);
        zco=zco-mod(zco,layer_displacement);
end

%% Generate and save VOXEL-map from STL

switch slice_direction
     case 'x'
        %Voxelise the STL:
        xx=xco/layer_displacement;      
        yy=yco/print_displacement;
        zz=zco/print_displacement;
        layers=xx;
        [OUTPUTgrid] = VOXELISE(round(xx),round(yy),round(zz),stl_file,'xyz');  
        for i=1:xx
            figure
            imagesc(squeeze(OUTPUTgrid(i,:,:)))
            colormap(gray(2))
            axis equal tight
            imwrite(squeeze(OUTPUTgrid(i,:,:)),['output/array',num2str(i),'.png'])
        end
        
    case 'y'
        %Voxelise the STL:
        xx=xco/print_displacement;
        yy=yco/layer_displacement;
        zz=zco/print_displacement;
        layers=yy;
        [OUTPUTgrid] = VOXELISE(round(xx),round(yy),round(zz),stl_file,'xyz');  
        for i=1:yy
            figure
            imagesc(squeeze(OUTPUTgrid(:,i,:)))
            colormap(gray(2))
            axis equal tight
            imwrite(squeeze(OUTPUTgrid(:,i,:)),['output/array',num2str(i),'.png'])
        end
    case 'z'
        %Voxelise the STL:
        xx=xco/print_displacement;
        yy=yco/print_displacement;
        zz=zco/layer_displacement;
        layers=zz;
        [OUTPUTgrid] = VOXELISE(round(xx),round(yy),round(zz),stl_file,'xyz');  
        for i=1:zz
            figure
            imagesc(squeeze(OUTPUTgrid(:,:,i)))
            colormap(gray(2))
            axis equal tight
            imwrite(squeeze(OUTPUTgrid(:,:,i)),['output/array',num2str(i),'.png'])
        end
end
dimension_x = xx
dimension_y = yy
save('output/specs.mat','print_displacement','layer_displacement','layers','dimension_x','dimension_y')
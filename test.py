I = imread('C:/Users/MY-PC/OneDrive/Desktop/projects/datasets/cart/out/simoes_p.jpg');
Ihat = imread('C:/Users/MY-PC/OneDrive/Desktop/projects/datasets/cart/testA/simoes.jpg');

[rows columns ~] = size(I);
  
mseRImage = (double(I(:,:,1)) - double(Ihat(:,:,1))) .^ 2;
mseGImage = (double(I(:,:,2)) - double(Ihat(:,:,2))) .^ 2;
mseBImage = (double(I(:,:,3)) - double(Ihat(:,:,3))) .^ 2;

mseR = sum(sum(mseRImage)) / (rows * columns);
mseG = sum(sum(mseGImage)) / (rows * columns);
mseB = sum(sum(mseBImage)) / (rows * columns);

mse = (mseR + mseG + mseB)/3;
PSNR_Value = 10 * log10( 255^2 / mse);
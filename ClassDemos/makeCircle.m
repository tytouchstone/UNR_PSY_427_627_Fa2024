function circleOut = makeCircle(size)
% Usage: circleOut = makeCircle(size)
% 
% This is a docstring! Provide useful information here.
%
% Inputs
% size : size of array

t = linspace(-1, 1, size);
[x, y] = meshgrid(t, t);

[theta, rho] = cart2pol(x, y);

circleOut = rho < 1;

end
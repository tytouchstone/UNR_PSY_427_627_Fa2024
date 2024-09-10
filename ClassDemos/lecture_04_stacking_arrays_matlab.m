% More exercises to generate images and interesting plots

%% Stacking arrays
% Two arrays can be stacked vertically with simple syntax in matlab: 

a = [1, 2, 3, 4];
b = [5, 6, 7, 8];
c = [a;b]; % note the semicolon!
disp(c)

% Arrays can be stacked horizontally with a comma instead of a semicolon:
d = [a,b];
disp(d)

%% Stacking in 3rd or other dimension
% To stack arrays in DEPTH (3rd array dimension), use cat:
r1 = rand(4,4);
r2 = rand(4,4);
r3 = cat(3, r1, r2);

size(r3)

% Note that this won't work if the arrays are different sizes! 

%% For loops (basic flow control)

for i = 1:10
    % do something with i
    disp(i)
end

%% Making a gradient image
% Pre-allocate an image of the size you want
image = zeros(10,10);
for i = 1:10
    % Replace each row of the image with a different range of numbers
    % (1-10 in the first row, then ?? in the second...)
    image(i, :) = i:i+9;
end

%% Print out resulting array as numbers
disp(image)

%% Show resulting array as image
imagesc(image)

%% Continuation: how would you...
% (There are several ways to do this! try to think of multiple ways)

% Make a vertical gradient? (increasing values from top to bottom?)

% Make a horizontal gradient? (increasing values from left to right?)


%% Making circles
% start with meshgrid
t = linspace(-1, 1, 101);
[x, y] = meshgrid(t, t);
figure; 
imagesc(x);
figure();
imagesc(y);

% Convert to polar coordinate (angle and radius instead of x and y)
[theta, rho] = cart2pol(x, y);
figure;
imagesc(rho);

%% threshold to get a circle!
% This creates a LOGICAL image of all true and false values, which will 
% show up as a binary (zero and one) image. You can convert this to another
% numerical format if you want! 
imagesc(rho < .5);

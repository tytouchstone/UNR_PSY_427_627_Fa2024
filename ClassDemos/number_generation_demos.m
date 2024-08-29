% In this demo, we will walk through several ways to generate numbers.
% Geneating numbers is used all the time in many programming tasks; here,
% we highlight some examples uses in experiment generation. 

%% First, a simple increasing list of integers
% Useful for specifying positions spaced across a screen, regularly spaced
% time intervals, 
a = 1:10;

%% Fancy skipping 
% Matlab syntax allows incrementing spaced values 
b = 2:2:20;
disp(b)

% or linearly spaced 
c = linspace(0, 1, 10);
disp(c)

% try getting help on this function to understand the options

%% Generating a grid of locations
[x, y] = meshgrid(1:10,1:10);

disp(x)
disp(y)

% what happened to any previous x?

%% Other means to generate:
% Check the help for these functions
% random (uniform) numbers
d = rand(5,3, 'single');
e = rand(5,3, 'double');

ones
zeros
randn

%% Basic plotting
plot
scatter
hist
imagesc


%% Challenges!

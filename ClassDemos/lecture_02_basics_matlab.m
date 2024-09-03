%% Demos of basic variables and operations in Matlab

%% Variables
% We will start with scalars (simple numbers)
% Assigning variables is done with the equals sign:
% (note the semicolon! without a semicolon at the end of each line, matlab
% is very verbose)
x = 1;

% you can inspect the type of data you've assigned to a variable with the
% `class` function, like this:
disp(class(x))

% And 

%% Operations on scalars
% Stay tuned for live demo! Using +, =, *, /, ^
disp(x + 5)

% Some things can be done with functions or with 
% Try to think of another way to do this:
sqrt(9)

%% Strings
% Strings are sequences of characters. All programming lanuages have some
% way to represent text or characters; Matlab syntax puts them in single
% quotes (other languages including python can use single or double quotes)
myString = 'this is a string.';
disp(class(myString))

fprintf
sprintf

% indexing
% - arrays
% - logical



% Generate the string: 
I can't imagine how to do this

% Display two points of precision of pi (3.14149)
display pi as a string with 2 decimal points


%%
x = -1:.002:1;
x = pi * x * 3;
y = sin(x);
plot(x, y);

%%
my_range = linspace(-1, 1, 101);
[x, y] = meshgrid(my_range,my_range);
ss = sin(pi * x * 4);
imagesc(ss)
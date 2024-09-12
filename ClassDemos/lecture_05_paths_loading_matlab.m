% Matlab loading data

%% String file paths
% Combine elements of a string
string_1 = 'hello';
string_2 = 'world';
new_string = [string_1, string_2]
disp(new_string)

%% Combining strings into file paths
% curdir() gives you '.', the indicator for (right here)
base_dir1 = pwd;
disp(base_dir1)
% Join that with something else
my_file_1 = fullfile(base_dir1, 'test.txt')
disp(my_file_1)
% Check if that file is there
disp(exist(my_file_1))

%% Get all files in a directory
files_a = dir(); % Supports wild card (*) syntax
%files_b = {files_a.name} 

%% Read text from a file
fname = 'makeCircle.m'
fid = fopen(fname);
% get one lines of file
fgetl(fid)
% Get the rest...?
% Ask chatgpt!

%% save arrays
% Create a random array
a = rand(10,10)
% Save it
save('test_array_1.mat', 'a')
% Save multiple arrays
b = rand(20,10)
save('test_arrays_2.mat', 'a','b')

%% Load arrays
load('test_array_1.mat')

%% Load images
fdir = '/Users/mark/pomsync/mark/Teaching/PSY427_627/datasets/fLoc_stimuli'
% Load image
im = imread(fullfile(fdir, 'adult-1.jpg'));
% display image
imagesc(im)
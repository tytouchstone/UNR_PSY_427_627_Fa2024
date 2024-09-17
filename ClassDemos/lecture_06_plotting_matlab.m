% Lecture 6: Plotting 
%% Generate data to use below
n_points = 10;
line_data_x = linspace(0, 10, n_points);
line_data_y = rand(n_points,1);
image_data = randn(n_points,n_points);
scatter_data_x = randn(n_points,1);
scatter_data_y = scatter_data_x * 2 + randn(n_points,1) * 2;
bar_data = rand(2,3);

%% Line plot
% Generate a figure (default)
fig = figure();
% Plot line data
line_h = plot(line_data_x, line_data_y);
xlabel('X data');
ylabel('Y data');

% The result is UGLY! 

%% Make it pretty: 
% Control size of figure in inches, explicitly get axis at figure creation
fig = figure(2);
PaperSize = [6, 4];
set(fig,'PaperType','<custom>','PaperUnits','inches','PaperSize',PaperSize);
nice_red = [0.8, 0.05, 0.05];
fontname = 'arial';
label_size = 24;
tk_size = 20;
linewidth = 3;
ytk = 0:.2:1;
line_h = plot(line_data_x, line_data_y);
% Set linewidth
set(line_h, 'LineWidth', 2)
xlabel('X data', fontsize=label_size, fontname=fontname)
ylabel('Y data', fontsize=label_size, fontname=fontname)
xticks(0:2:n_points);
yticks(ytk);
% Set fontsize
set(gca,'fontsize', 16)


%% Save
print(fig,'matlab_demoplot','-dpng', '-r100')

%% Scatter plot
dot_h = scatter(scatter_data_x, scatter_data_y);


% TO DO: Make it pretty! 
% Set dot sizes, fonts, 

% Bonus: open up axes, such that only left and bottom axis are shown, not top and right 

%% Image plot
image_h = imagesc(image_data);

% TO DO: Make it pretty!
% Change the colormap to something biphasic - which shows positive and negative
% values in different colors. Get rid of axis ticks. 


%% bar plot
% Apologies, the matplotlib bar plot function is terrible.
bar(bar_data);

% TO DO : Label axes, label ticks (with something)

%% Bonus bonus: 

% Write a function to set all tick labels in a graph to a particular size and
% font, and set all axis labels (xlabel and ylabel) to a particular size and 
% font. 
% 
% Write a function to open the axes up (to get rid of right and top bounding box)
% 
% Write a function to set axis linewidths
% 

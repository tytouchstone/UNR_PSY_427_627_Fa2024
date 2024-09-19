% Skip sync tests for now (sync tests cause issues on Mac OS)
Screen('Preference', 'SkipSyncTests', 1);         

% Choosing the display with the highest display number is
% a best guess about where you want the stimulus displayed.
screens=Screen('Screens');
screenNumber=max(screens);

% Open window with default settings:
screenColor = [128,128,128];
screenSize = [400,400];
screenUpperLeft = [200,200];
screenRect = [screenUpperLeft, screenUpperLeft + screenSize];
w=Screen('OpenWindow', screenNumber, screenColor, screenRect);

Screen('DrawText', w, 'Hello', screenSize(1)/2, screenSize(2)/2, [255, 255, 255, 255]);
Screen('Flip', w);
WaitSecs(1);

Screen('DrawText', w, 'world', screenSize(1)/2, screenSize(2)/2, [255, 255, 255, 255]);
Screen('Flip', w)
WaitSecs(1);

Screen('DrawText', w, 'bye!', screenSize(1)/2, screenSize(2)/2, [255, 255, 255, 255]);
Screen('Flip', w)
WaitSecs(0.5);

% End of demo, close window:
sca;
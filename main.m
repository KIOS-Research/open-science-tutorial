function main(varargin)

    % Parse the input arguments
    inpname = varargin{1};
    inpname = ['../data/', inpname, '.inp'];

    addpath(genpath(pwd));
    disp('Paths Loaded.');
    disp(inpname)

    tmpinp = 'tmp.inp';
    copyfile(inpname, tmpinp);
    d = epanet(tmpinp);

    h = d.plot(); % Plot network
    saveas(h, '../results/test.png'); % Save plot
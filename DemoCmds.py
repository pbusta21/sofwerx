@mfunction("command")
def DemoCmds(serPort=None):
    # Testing out the demo commands in the create
    t = 0
    while t < 600:
        DemoCmdsCreate(serPort, 9)
        for t in mslice[0:60]:
            DemoCmdsCreate(serPort, 2)
            t = t + 1
        end
        for t in mslice[61:120]:
            DemoCmdsCreate(serPort, 4)
            t = t + 1
        end
        for t in mslice[121:480]:
            DemoCmdsCreate(serPort, 0)
            t = t + 1
        end
        for t in mslice[481:540]:
            DemoCmdsCreate(serPort, 3)
            t = t + 1
        end
        for t in mslice[541:600]:
            DemoCmdsCreate(serPort, 1)
            t = t + 1
        end
    end


    #  % Set constants for this program
    #     maxDuration= 1200;  % Max time to allow the program to run (s)
    #    
    #     maxFwdVel= 0.5;     % Max allowable forward velocity with no angular 
    #                         % velocity at the time (m/s)
    #      tStart= tic;        % Time limit marker
    #      while toc(tStart) < maxDuration
    #                         
    #     command= DemoCmdsCreate(serPort,4);                    
    #                         
    #     pause(0.1)
    #      end

end
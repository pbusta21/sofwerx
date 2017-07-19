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
    # Stop roomba moving
    v = 0
    w = 0
    SetFwdVelAngVelCreate(serPort, v, w)

end
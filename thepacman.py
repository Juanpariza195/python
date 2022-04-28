def eat_ghost(energyPill, touchingGhost):
    return (energyPill and touchingGhost)

def score(energyPill, touchingPoint):
    return (energyPill or touchingPoint)

def lose(energyPill, touchingGhost):
    return (energyPill == False) and (touchingGhost == True)

def win(eatenPoints, energyPill, touchingGhost):
    return (eatenPoints == True) and (lose(energyPill, touchingGhost) == False)
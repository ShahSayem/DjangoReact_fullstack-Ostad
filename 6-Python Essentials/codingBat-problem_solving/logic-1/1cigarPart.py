def cigarParty(cigars, isWeekend):
    if (isWeekend):
        return (cigars >= 40)
    else:
        return 40 <= cigars <= 60
    #(cigars >= 40 and cigars <= 60 )
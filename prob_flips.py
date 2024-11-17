import math

def single_neg(weak, moderate, severe, deck_prob):

    if 14 in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,1)
        weak_A = math.comb(len(weak)-1,1) * math.comb(len(deck_prob)-len(weak)-1,1) + math.comb(len(weak)-1,2)
        moderate_A = math.comb(len(moderate),2) + math.comb(len(moderate),1)* math.comb(len(severe)-1,1)
        severe_A = math.comb(len(severe)-1,2)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-2,1)
    elif 14 in severe and 0 not in weak:
        bj_A = 0
        weak_A = math.comb(len(weak),1) * math.comb(len(deck_prob)-len(weak)-1,1) + math.comb(len(weak),2)
        moderate_A = math.comb(len(moderate),2) + math.comb(len(moderate),1)* math.comb(len(severe)-1,1)
        severe_A = math.comb(len(severe)-1,2)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,1)
    elif 14 not in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,1)
        weak_A = math.comb(len(weak)-1,1) * math.comb(len(deck_prob)-len(weak)-1,1) + math.comb(len(weak),2)
        moderate_A = math.comb(len(moderate),2) + math.comb(len(moderate),1)* math.comb(len(severe),1)
        severe_A = math.comb(len(severe),2)
        rj_A = 0
    else:
        bj_A = 0
        weak_A = math.comb(len(weak),1) * math.comb(len(deck_prob)-len(weak),1) + math.comb(len(weak),2)
        moderate_A = math.comb(len(moderate),2) + math.comb(len(moderate),1)* math.comb(len(severe),1)
        severe_A = math.comb(len(severe),2)
        rj_A = 0

    return bj_A, weak_A, moderate_A, severe_A, rj_A

def double_neg(weak, moderate, severe, deck_prob):
    if 14 in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,2)
        weak_A = math.comb(len(weak)-1,1) * math.comb(len(deck_prob)-len(weak)-1,2) + math.comb(len(weak)-1,3) + math.comb(len(weak)-1,2)* math.comb(len(deck_prob)-len(weak)-1,1)
        moderate_A = math.comb(len(moderate),3) + math.comb(len(moderate),2)* math.comb(len(severe)-1,1) + math.comb(len(moderate),1)* math.comb(len(severe)-1,2)
        severe_A = math.comb(len(severe)-1,3)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-2,2)
    elif 14 in severe and 0 not in weak:
        bj_A = 0
        weak_A = math.comb(len(weak),1) * math.comb(len(deck_prob)-len(weak)-1,2) + math.comb(len(weak),3) + math.comb(len(weak),2)* math.comb(len(deck_prob)-len(weak)-1,1)
        moderate_A = math.comb(len(moderate),3) + math.comb(len(moderate),2)* math.comb(len(severe)-1,1) + math.comb(len(moderate),1)* math.comb(len(severe)-1,2)
        severe_A = math.comb(len(severe)-1,3)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,2)
    elif 14 not in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,2)
        weak_A = math.comb(len(weak)-1,1) * math.comb(len(deck_prob)-len(weak)-1,2) + math.comb(len(weak)-1,2) * math.comb(len(deck_prob)-len(weak)-1,1) + math.comb(len(weak)-1,3)
        moderate_A = math.comb(len(moderate),3) + math.comb(len(moderate),2)* math.comb(len(severe),1) + math.comb(len(moderate),1)* math.comb(len(severe),2)
        severe_A = math.comb(len(severe),3)
        rj_A = 0
    else:
        bj_A = 0
        weak_A = math.comb(len(weak),1) * math.comb(len(deck_prob)-len(weak),2) + math.comb(len(weak),2) * math.comb(len(deck_prob)-len(weak),1) + math.comb(len(weak),3)
        moderate_A = math.comb(len(moderate),3) + + math.comb(len(moderate),2)* math.comb(len(severe),1) + math.comb(len(moderate),1)* math.comb(len(severe),2)
        severe_A = math.comb(len(severe),3)
        rj_A = 0

    return bj_A, weak_A, moderate_A, severe_A, rj_A

def triple_neg(weak, moderate, severe, deck_prob):
    if 14 in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,3)
        weak_A = math.comb(len(weak)-1,4) + math.comb(len(weak)-1,3) * math.comb(len(deck_prob)-len(weak)-1,1) + math.comb(len(weak)-1,2) * math.comb(len(deck_prob)-len(weak)-1,2) + math.comb(len(weak)-1,1)* math.comb(len(deck_prob)-len(weak)-1,3)
        moderate_A = math.comb(len(moderate),4) + math.comb(len(moderate),3)* math.comb(len(severe)-1,1) + math.comb(len(moderate),2)* math.comb(len(severe)-1,2) + math.comb(len(moderate),1)* math.comb(len(severe)-1,3)
        severe_A = math.comb(len(severe)-1,4)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-2,3)
    elif 14 in severe and 0 not in weak:
        bj_A = 0
        weak_A =  math.comb(len(weak),4) + math.comb(len(weak),3) * math.comb(len(deck_prob)-len(weak)-1,1) + math.comb(len(weak),2)* math.comb(len(deck_prob)-len(weak)-1,2) + math.comb(len(weak),1)* math.comb(len(deck_prob)-len(weak)-1,3)
        moderate_A = math.comb(len(moderate),4) + math.comb(len(moderate),3)* math.comb(len(severe)-1,1) + math.comb(len(moderate),2)* math.comb(len(severe)-1,2) + math.comb(len(moderate),1)* math.comb(len(severe)-1,3)
        severe_A = math.comb(len(severe)-1,4)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,3)
    elif 14 not in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,3)
        weak_A = math.comb(len(weak)-1,4) + math.comb(len(weak)-1,3) * math.comb(len(deck_prob)-len(weak)-1,1) + math.comb(len(weak)-1,2) * math.comb(len(deck_prob)-len(weak)-1,2) + math.comb(len(weak)-1,1) * math.comb(len(deck_prob)-len(weak)-1,3)
        moderate_A = math.comb(len(moderate),4) + math.comb(len(moderate),3)* math.comb(len(severe),1) + math.comb(len(moderate),2)* math.comb(len(severe),2) + math.comb(len(moderate),1)* math.comb(len(severe),3)
        severe_A = math.comb(len(severe),4)
        rj_A = 0
    else:
        bj_A = 0
        weak_A = math.comb(len(weak),4) + math.comb(len(weak),3) * math.comb(len(deck_prob)-len(weak),1) + math.comb(len(weak),2) * math.comb(len(deck_prob)-len(weak),2) + math.comb(len(weak),1) * math.comb(len(deck_prob)-len(weak),3)
        moderate_A = math.comb(len(moderate),4) + + math.comb(len(moderate),3)* math.comb(len(severe),1) + math.comb(len(moderate),2)* math.comb(len(severe),2) + math.comb(len(moderate),1)* math.comb(len(severe),3)
        severe_A = math.comb(len(severe),4)
        rj_A = 0

    return bj_A, weak_A, moderate_A, severe_A, rj_A

def single_pos(weak, moderate, severe, deck_prob):
    if 14 in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,1)
        weak_A = math.comb(len(weak)-1,2)
        moderate_A = math.comb(len(moderate),2) + math.comb(len(moderate),1)* math.comb(len(weak)-1,1)
        severe_A = math.comb(len(severe)-1,1) * math.comb(len(deck_prob)-len(severe)-1,1) + math.comb(len(severe)-1,2)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-2,1)
    elif 14 in severe and 0 not in weak:
        bj_A = 0
        weak_A = math.comb(len(weak)-1,2)  
        moderate_A = math.comb(len(moderate),2) + math.comb(len(moderate),1)* math.comb(len(weak)-1,1)
        severe_A = math.comb(len(severe),1) * math.comb(len(deck_prob)-len(severe),1) + math.comb(len(severe),2)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,1)
    elif 14 not in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,1)
        weak_A = math.comb(len(weak),2)
        moderate_A = math.comb(len(moderate),2) + math.comb(len(moderate),1)* math.comb(len(weak),1)
        severe_A = math.comb(len(severe)-1,1) * math.comb(len(deck_prob)-len(severe)-1,1) + math.comb(len(severe),2)
        rj_A = 0
    else:
        bj_A = 0
        weak_A = math.comb(len(weak),2)
        moderate_A = math.comb(len(moderate),2) + math.comb(len(moderate),1)* math.comb(len(weak),1)
        severe_A = math.comb(len(severe),1) * math.comb(len(deck_prob)-len(severe),1) + math.comb(len(severe),2)
        rj_A = 0

    return bj_A, weak_A, moderate_A, severe_A, rj_A

def double_pos(weak, moderate, severe, deck_prob):
    if 14 in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,2)
        weak_A = math.comb(len(weak)-1,3)
        moderate_A = math.comb(len(moderate),3) + math.comb(len(moderate),2)* math.comb(len(weak)-1,1) + math.comb(len(moderate),1)* math.comb(len(weak)-1,2)
        severe_A = math.comb(len(severe)-1,1) * math.comb(len(deck_prob)-len(severe)-1,2) + math.comb(len(severe)-1,3) + math.comb(len(severe)-1,2)* math.comb(len(deck_prob)-len(severe)-1,1)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-2,2)
    elif 14 in severe and 0 not in weak:
        bj_A = 0
        weak_A = math.comb(len(weak)-1,3)
        moderate_A = math.comb(len(moderate),3) + math.comb(len(moderate),2)* math.comb(len(weak)-1,1) + math.comb(len(moderate),1)* math.comb(len(weak)-1,2)
        severe_A = math.comb(len(severe)-1,1) * math.comb(len(deck_prob)-len(severe),2) + math.comb(len(severe),3) + math.comb(len(severe),2)* math.comb(len(deck_prob)-len(severe),1)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,2)
    elif 14 not in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,2)
        weak_A = math.comb(len(weak)-1,3)
        moderate_A = math.comb(len(moderate),3) + math.comb(len(moderate),2)* math.comb(len(weak)-1,1) + math.comb(len(moderate),1)* math.comb(len(weak)-1,2)
        severe_A = math.comb(len(severe),1) * math.comb(len(deck_prob)-len(severe)-1,2) + math.comb(len(severe),2) * math.comb(len(deck_prob)-len(severe)-1,1) + math.comb(len(severe),3)
        rj_A = 0
    else:
        bj_A = 0
        weak_A = math.comb(len(weak),3)
        moderate_A = math.comb(len(moderate),3) + math.comb(len(moderate),2)* math.comb(len(weak),1) + math.comb(len(moderate),1)* math.comb(len(weak),2)
        severe_A = math.comb(len(severe),1) * math.comb(len(deck_prob)-len(severe),2) + math.comb(len(severe),2) * math.comb(len(deck_prob)-len(severe),1) + math.comb(len(severe),3)
        rj_A = 0

    return bj_A, weak_A, moderate_A, severe_A, rj_A

def triple_pos(weak, moderate, severe, deck_prob):
    if 14 in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,3)
        weak_A = math.comb(len(weak)-1,4)
        moderate_A = math.comb(len(moderate),4) + math.comb(len(moderate),3)* math.comb(len(weak)-1,1) + math.comb(len(moderate),2)* math.comb(len(weak)-1,2) + math.comb(len(moderate),1)* math.comb(len(weak)-1,3)
        severe_A = math.comb(len(severe)-1,4) + math.comb(len(severe)-1,3) * math.comb(len(deck_prob)-len(severe)-1,1) + math.comb(len(severe)-1,2) * math.comb(len(deck_prob)-len(severe)-1,2) + math.comb(len(severe)-1,1)* math.comb(len(deck_prob)-len(severe)-1,3)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-2,3)
    elif 14 in severe and 0 not in weak:
        bj_A = 0
        weak_A = math.comb(len(weak),4)
        moderate_A = math.comb(len(moderate),4) + math.comb(len(moderate),3)* math.comb(len(weak),1) + math.comb(len(moderate),2)* math.comb(len(weak),2) + math.comb(len(moderate),1)* math.comb(len(weak),3)
        severe_A = math.comb(len(severe)-1,4) + math.comb(len(severe)-1,3) * math.comb(len(deck_prob)-len(severe)-1,1)  + math.comb(len(severe)-1,2) * math.comb(len(deck_prob)-len(severe)-1,2) + math.comb(len(severe)-1,1) * math.comb(len(deck_prob)-len(severe)-1,3)
        rj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,3)
    elif 14 not in severe and 0 in weak:
        bj_A = math.comb(1,1) * math.comb(len(deck_prob)-1,3)
        weak_A =math.comb(len(weak)-1,4)
        moderate_A = math.comb(len(moderate),4) + math.comb(len(moderate),3)* math.comb(len(weak)-1,1) + math.comb(len(moderate),2)* math.comb(len(weak)-1,2) + math.comb(len(moderate),1)* math.comb(len(weak)-1,3)
        severe_A = math.comb(len(severe),4) + math.comb(len(severe),3) * math.comb(len(deck_prob)-len(severe)-1,1) + math.comb(len(severe),2) * math.comb(len(deck_prob)-len(severe)-1,2) + math.comb(len(severe),1) * math.comb(len(deck_prob)-len(severe)-1,3)
        rj_A = 0
    else:
        bj_A = 0
        weak_A = math.comb(len(weak),4)
        moderate_A = math.comb(len(moderate),4) + + math.comb(len(moderate),3)* math.comb(len(weak),1) + math.comb(len(moderate),2)* math.comb(len(weak),2) + math.comb(len(moderate),1)* math.comb(len(weak),3)
        severe_A = math.comb(len(severe),4) + math.comb(len(severe),3) * math.comb(len(deck_prob)-len(severe),1) + math.comb(len(severe),2) * math.comb(len(deck_prob)-len(severe),2) + math.comb(len(severe),1) * math.comb(len(deck_prob)-len(severe),3)
        rj_A = 0

    return bj_A, weak_A, moderate_A, severe_A, rj_A
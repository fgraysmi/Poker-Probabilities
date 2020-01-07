# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:51:09 2017

@author: frase
"""

import random
import itertools


class card(object):
    #initializes the class with an x and a y value
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
    
    def getSuit(self):
        return self.suit
    
    def getValue(self):
        if self.value=='A':
            return 14
        if self.value=='K':
            return 13
        if self.value=='Q':
            return 12
        if self.value=='J':
            return 11
        else:
            return int(self.value)
    
    def __eq__(self,other):
        if self.getValue()==other.getValue() and self.getSuit()==other.getSuit():
            return True
        else:
            return False
            
    def getColor(self):
        if self.suite=='H' or self.suite=='D':
            return 'R'
        else:
            return 'B'
            
    def __str__(self):
        return str(self.suit)+str(self.value)
        

def createDeck():
    values_list=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits_list=['H','D','C','S']
    deck=[]
    for suit in suits_list:
        for val in values_list:
            new_card=card(suit,val)
            deck.append(new_card)
    return deck

def flush(hand):
    if hand[0].getSuit()==hand[1].getSuit()==hand[2].getSuit()==hand[3].getSuit()==hand[4].getSuit():
        return True
    else:
        return False
    
def straight(hand):
    values=[]
    for cards in hand:
        values.append(cards.getValue())
    values.sort()
    if values[4]-values[3]==1 and values[3]-values[2]==1 and values[2]-values[1]==1 and values[1]-values[0]==1:
        return True
    else:
        return False
        
def straight_flush(hand):
    if straight(hand) and flush(hand):
        return True
    else:
        return False

def four_of_a_kind(hand):
    values=[]
    for cards in hand:
        values.append(cards.getValue())
    values.sort()
    if values[4]==values[3]==values[2]==values[1] or values[3]==values[2]==values[1]==values[0]:
        return True
    else:
        return False

def three_of_a_kind(hand):
    values=[]
    for cards in hand:
        values.append(cards.getValue())
    values.sort()
    if values[4]==values[3]==values[2] or values[3]==values[2]==values[1] or values[2]==values[1]==values[0]:
        return True
    else:
        return False  
        
def two_pair(hand):
    values=[]
    for cards in hand:
        values.append(cards.getValue())
    values.sort()
    if (values[4]==values[3] and values[2]==values[1]) or (values[3]==values[2] and values[1]==values[0]):
        return True
    else:
        return False 
        
def pair(hand):
    values=[]
    for cards in hand:
        values.append(cards.getValue())
    values.sort()
    if values[4]==values[3] or values[3]==values[2] or values[2]==values[1] or values[1]==values[0]:
        return True
    else:
        return False       

def full_house(hand):
    values=[]
    for cards in hand:
        values.append(cards.getValue())
    values.sort()
    if (values[4]==values[3]==values[2] and values[1]==values[0]) or (values[4]==values[3] and values[2]==values[1]==values[0]):
        return True
    else:
        return False

def high_card(hand):
    values=[]
    for cards in hand:
        values.append(cards.getValue())
    values.sort(reverse=True)
    return values[0]
        
def scoring(hand):
    score=0
    if straight_flush(hand)==True:
        score=high_card(hand)+800
    elif four_of_a_kind(hand)==True:
        score=score+700
        values=[]
        for cards in hand:
            values.append(cards.getValue())
        values.sort()
        if values[4]==values[3]==values[2]==values[1]:
            score=score+values[4]
        else:
            score=score+values[0]
    elif full_house(hand)==True:
        score=score+600
        values=[]
        for cards in hand:
            values.append(cards.getValue())
        values.sort()
        if values[4]==values[3]==values[2]:
            score=score+values[4]
        else:
            score=score+values[0]        
    elif flush(hand)==True:
        score=high_card(hand)+500
    elif straight(hand)==True:
        score=high_card(hand)+400
    elif three_of_a_kind(hand)==True:
        score=score+300
        values=[]
        for cards in hand:
            values.append(cards.getValue())
        values.sort()
        if values[4]==values[3]==values[2]:
            score=score+values[4]
        else:
            score=score+values[0]  
    elif two_pair(hand)==True:
        score=score+200
        values=[]
        for cards in hand:
            values.append(cards.getValue())
        values.sort()
        if values[4]==values[3]:
            score=score+values[4]
        else:
            score=score+values[3] 
    elif pair(hand)==True:
        score=score+100
        values=[]
        for cards in hand:
            values.append(cards.getValue())
        values.sort()
        if values[4]==values[3]:
            score=score+values[4]
        elif values[3]==values[2]:
            score=score+values[3]
        elif values[2]==values[1]:
            score=score+values[2]
        else:
            score=score+values[1]
    else:
        score=high_card(hand)
    return score
        
        
#built this just to check the scoring mechanism
def deal(players):
    deck=createDeck()       
    random.shuffle(deck)
    hands=[]
    while players>0:
        hands.append(deck[0:5])
        deck=deck[5:]
        players-=1
    return hands


def inputHand():
    suit_list=['D','S','H','C']
    value_list=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    while True:
        try:
            card1_suit=input('Enter the suit of your first card (D,S,H,C): ')
            assert card1_suit.upper() in suit_list
            break
        except AssertionError:
            print('Must select a valid suit!')
    while True:
        try:
            card1_val=input('Enter the value of your first card (2,3,4,5,6,7,8,9,10,J,Q,K,A): ')
            assert card1_val.upper() in value_list
            break
        except AssertionError:
            print('Must select a valid value!')
    while True:
        try:
            while True:
                try:
                    card2_suit=input('Enter the suit of your second card (D,S,H,C): ')
                    assert card2_suit.upper() in suit_list
                    break
                except AssertionError:
                    print('Must select a valid suit!')
            while True:
                try:
                    card2_val=input('Enter the value of your second card (2,3,4,5,6,7,8,9,10,J,Q,K,A): ')
                    assert card2_val.upper() in value_list
                    break
                except AssertionError:
                    print('Must select a valid value!')
            assert not(card1_suit==card2_suit and card1_val==card2_val)
            break
        except AssertionError:
            print('Cannot input the same card twice!')
    return [card(card1_suit,card1_val), card(card2_suit,card2_val)]

    
def filterDeck(hand):
    deck=createDeck()
    newdeck=[]
    for cards in deck:
        if cards not in hand:
            newdeck.append(cards)
    return newdeck

            
def inputFlop(hand):
    suit_list=['D','S','H','C']
    value_list=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    while True:
        try:
            while True:
                try:
                    card1_suit=input('Enter the suit of the first flop card (D,S,H,C): ')
                    assert card1_suit.upper() in suit_list
                    break
                except AssertionError:
                    print('Must select a valid suit!')
            while True:
                try:
                    card1_val=input('Enter the value of the first flop card (2,3,4,5,6,7,8,9,10,J,Q,K,A): ')
                    assert card1_val.upper() in value_list
                    card1=card(card1_suit,card1_val)
                    break
                except AssertionError:
                    print('Must select a valid value!')
            assert card1 not in hand
            break
        except AssertionError:
            print('Cannot enter the same value twice!')
    while True:
        try:
            while True:
                try:
                    card2_suit=input('Enter the suit of the second flop card (D,S,H,C): ')
                    assert card2_suit.upper() in suit_list
                    break
                except AssertionError:
                    print('Must select a valid suit!')
            while True:
                try:
                    card2_val=input('Enter the value of the second flop card (2,3,4,5,6,7,8,9,10,J,Q,K,A): ')
                    assert card2_val.upper() in value_list
                    card2=card(card2_suit,card2_val)
                    break
                except AssertionError:
                    print('Must select a valid value!')
            assert card2!=card1 and card2 not in hand
            break
        except AssertionError:
            print('Cannot enter the same value twice!')
    while True:
        try:
            while True:
                try:
                    card3_suit=input('Enter the suit of the third flop card (D,S,H,C): ')
                    assert card3_suit.upper() in suit_list
                    break
                except AssertionError:
                    print('Must select a valid suit!')
            while True:
                try:
                    card3_val=input('Enter the value of the third flop card (2,3,4,5,6,7,8,9,10,J,Q,K,A): ')
                    assert card3_val.upper() in value_list
                    card3=card(card3_suit,card3_val)
                    break
                except AssertionError:
                    print('Must select a valid value!')
            assert card3!=card1 and card3!=card2 and card3 not in hand
            break
        except AssertionError:
            print('Cannot enter the same value twice!')
    return [card1,card2,card3]



               

def inputTurn(hand):
    suit_list=['D','S','H','C']
    value_list=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    while True:
        try:
            while True:
                try:
                    card1_suit=input('Enter the suit of the turn card (D,S,H,C): ')
                    assert card1_suit.upper() in suit_list
                    break
                except AssertionError:
                    print('Must select a valid suit!')
            while True:
                try:
                    card1_val=input('Enter the value of the turn card (2,3,4,5,6,7,8,9,10,J,Q,K,A): ')
                    assert card1_val.upper() in value_list
                    card1=card(card1_suit,card1_val)
                    break
                except AssertionError:
                    print('Must select a valid value!')
            assert card1 not in hand
            break
        except AssertionError:
            print('Cannot enter the same value twice!')
    return [card1]
    

def inputRiver(hand):
    suit_list=['D','S','H','C']
    value_list=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    while True:
        try:
            while True:
                try:
                    card1_suit=input('Enter the suit of the river card (D,S,H,C): ')
                    assert card1_suit.upper() in suit_list
                    break
                except AssertionError:
                    print('Must select a valid suit!')
            while True:
                try:
                    card1_val=input('Enter the value of the river card (2,3,4,5,6,7,8,9,10,J,Q,K,A): ')
                    assert card1_val.upper() in value_list
                    card1=card(card1_suit,card1_val)
                    break
                except AssertionError:
                    print('Must select a valid value!')
            assert card1 not in hand
            break
        except AssertionError:
            print('Cannot enter the same value twice!')
    return [card1]


def firstRound():
    hand=inputHand()
    f_deck=filterDeck(hand)
    full_hands=[]
    hand_count=0
    max_score=0
    full_score=0
    best_hand=[]
    better_hand_count=0
    for p_hands in itertools.permutations(f_deck, 3):
        full_hands.append(list(p_hands)+hand)
    for hands in full_hands:
        hand_score = scoring(hands)
        if hand_score>max_score:
            max_score=hand_score
            best_hand=hands
            hand_count+=1
            full_score+=hand_score
    print(float(full_score)/float(hand_count))
    return hand
    
def secondRound():
    preflop=firstRound()
    flop=inputFlop(preflop)
    hand=preflop+flop
    hand_score=scoring(hand)
    f_deck=filterDeck(hand)
    better_hand=0
    worse_hand=0
    same_hand=0
    full_hands=[]
    for p_hands in itertools.permutations(f_deck, 2):
        full_hands.append(list(p_hands)+flop)
    for hands in full_hands:
        p_score = scoring(hands)
        if p_score>hand_score:
            better_hand+=1
        elif p_score<hand_score:
            worse_hand+=1
        else:
            same_hand+=1
    print(float(worse_hand)/float(better_hand+worse_hand+same_hand))
    return preflop, flop, hand

def thirdRound():
    preflop, flop, hand=secondRound()
    turn=inputTurn(hand)
    table_cards=flop+turn
    best_score=0
    f_deck=filterDeck(hand)
    full_hands=[]
    better_hand=0
    worse_hand=0
    same_hand=0
    all_cards=hand+turn
    for p_hands in itertools.permutations(all_cards, 5):
        p_score=scoring(p_hands)
        if p_score>best_score:
            best_score=p_score
    for card_combos in itertools.permutations(table_cards,3):
        for p_hands in itertools.permutations(f_deck, 2):
            full_hands.append(list(p_hands)+list(card_combos))
    for p_hands in itertools.permutations(f_deck,1):
        full_hands.append(list(p_hands)+table_cards)
    for hands in full_hands:
        p_score = scoring(hands)
        if p_score>best_score:
            better_hand+=1
        elif p_score<best_score:
            worse_hand+=1
        else:
            same_hand+=1
    print(float(worse_hand)/float(better_hand+worse_hand+same_hand))
    return preflop, flop, turn, hand

    
    
    
    
def fourthRound():
    preflop, flop, turn, hand = thirdRound()
    river=inputRiver(hand)
    table_cards=flop+turn+river
    table_score=scoring(table_cards)
    f_deck=filterDeck(hand)
    all_cards=hand+turn+river
    full_hands=[]
    better_hand=0
    worse_hand=0
    same_hand=0
    best_score=0
    for p_hands in itertools.permutations(all_cards,5):
        p_score=scoring(p_hands)
        if p_score>best_score:
            best_score=p_score
    for card_combos in itertools.permutations(table_cards,3):
        for p_hands in itertools.permutations(f_deck,2):
            full_hands.append(list(p_hands)+list(card_combos))
    for card_combos in itertools.permutations(table_cards,4):
        for p_hands in itertools.permutations(f_deck,1):
            full_hands.append(list(p_hands)+list(card_combos))
    full_hands.append(table_cards)
    for hands in full_hands:
        p_score = scoring(hands)
        if p_score>best_score:
            better_hand+=1
        elif p_score<best_score:
            worse_hand+=1
        else:
            same_hand+=1
    return (float(worse_hand)/float(better_hand+worse_hand+same_hand))
    
            
    



#!/usr/bin/env python
# coding: utf-8

# In[103]:


# Rock, paper and scissors game!

import random # To shuffle the list

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_list = [rock, paper, scissors]
computer_list = hand_list
print("Player choice:\n")
hand = int(input("Which will you choose? 0, 1 or 2? (0 = rock, 1 = paper, 3 = scissors)\n"))


print(hand_list[hand])

print("Computer choice: \n")

random.shuffle(computer_list) 

print(computer_list[0])

print("Result:\n")

# Identifyng the player choice
if hand == 0:
    player_choice = 'rock'
    
elif hand == 1:
    player_choice = 'paper'
    
else:
    player_choice = 'scissors'

hand_list = [rock, paper, scissors]
# Identifyng the player choice    
if computer_list[0] == hand_list[0]:
    computer_choice = 'rock'
    
elif computer_list[0] == hand_list[1]:
    computer_choice = 'paper'
    
else:
    computer_choice = 'scissors'

# Comparing the choices   
if player_choice == 'rock' and computer_choice == 'scissors' or player_choice == 'paper' and computer_choice == 'rock' or player_choice == 'scissors' and computer_choice == 'paper':
    print("YOU WIN")

elif player_choice == computer_choice:
    print("IT'S A DRAW!")
    
else:
    print("YOU LOSE")


# In[99]:


print(computer_choice)
print(computer_list[0])
print(player_choice)


# In[90]:


computer_list[0] == hand_list[2]


# In[87]:


print(hand_list[2])


# In[ ]:





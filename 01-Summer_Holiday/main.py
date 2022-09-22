""""
Program Name: U2A0MSH My Summer Holiday

Program Description: This program gives an account of my holidays over the summer.

Program Author: MilkFlavor [フレーバー]

Program Date: 2022.09.21
"""
import os

def main():
  start = input('Would you like to hear about my summer? [y/n]\n')
  if start == 'y':
    os.system('clear')
    story()
  else:
    exit()

def story():
  print("Alright my summer went something like this. During the first month of summer I was stuck inside completing a a civics course for extra credit.\n")
  print("I spent most of my time just playing games and sleeping and going to class if I really had to. The classes were nice and the teachers were helpful for the most part. I enjoyed some assignment and completly dispised others. But all in all, it was a full filling July.\n")
  print("Now that summer school was over I had time to play games waste the rest of my summer. However, due to some over enthusiastic friends and strict parents, I was forced to work and join my friends at the gym\n")
  print("At first going to the gym was difficult, for context my friends have been going there ever since July while I just started. However, with the mass amount of motivation and a lot of will power I was able to keep a consistant work schedual. I wasn't only going to the gym, I was also asked by my parents to join a voulenteering job. And luckily my local library was just rebuilt and was lacking in man power. So I spent the rest of the summer going to the gym with friends and racking up voulenteering hours at the library.\n")
  print("Even though some people might think that I wasted summer, I belive that I learned a lot about myself. I learned to eat healthy, and create scheduals. This was definetly a summer to remember.")

if __name__ == '__main__':
  main()
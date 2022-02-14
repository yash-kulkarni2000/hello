# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:27:02 2022

@author: user
"""

from temp import albums

SONGS_LIST_INDEX = 3
SONGS_TITLE_INDEX = 1

while True:
    print("Enter your choice: ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{0} : {1}". format(index + 1 ,title))
        
    choice = int(input())
    
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break
        
    print("Enter your song choice: ")
    for index, (song_number, song_name) in enumerate(songs_list):
        print("{} : {}".format(index + 1, song_name))
        
    song_choice = int(input())
    
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONGS_TITLE_INDEX]
        print("playing {}".format(title))
    print("&&&" * 40)

#!/usr/bin/env python
# coding: utf-8
 
 
import urllib.request
 
url = "http://heeeeeeeey.com"
resposta = urllib.request.urlopen(url)
 
line = resposta.readline().decode("utf-8")
 
#line = 'Made by <a href="http://bod.ge">Mike Bodge</a> <a href="http://itunes.apple.com/us/album/greatest-hits-naughtys-nicest/id50235454?uo=4">iTunes</a>'
while line != '' :
       
        if '<a' in line :
                index = line.find('<a')
                line = line[index:]
                if '"' in line :
                        index = line.find('"')
                        line = line[index + 1:]
                        if '"' in line :
                                index = line.find('"')
                                link = line[:index]
                                line = line[index:]
                                print(link)
                               
                        else :
                                line = resposta.readline().decode("utf-8")
                else :
                        line = resposta.readline().decode("utf-8")     
        else :                 
                line = resposta.readline().decode("utf-8")

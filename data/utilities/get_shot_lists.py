# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 04:30:09 2021

@author: TianrunWang
"""
import os,inspect
import pandas as pd

class GetShotLists:
    
    def __init__(self,path):
        self.SL = pd.read_csv(path)
        
    def getshotlist(self):
        SL = self.SL
        shot_list = []
        for i in range(len(SL)):
            shots = SL['FrameLists'][i].split(',')#[1:-2]
            shot_list.append(shots)    
        return shot_list
        

shot_object = GetShotLists("knnw_labels.csv")
shot_list = shot_object.getshotlist()


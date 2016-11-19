import Tkinter
import matplotlib.pyplot as plt

temp = [(1,{'happy':'0.56','sad':'0.10','neutral':'0.33','angry':'0.15'}),
        (2,{'happy':'0.20','sad':'0.60','neutral':'0.15','angry':'0.40'}),
        (3,{'happy':'0.45','sad':'0.25','neutral':'0.50','angry':'0.05'}),
        (4,{'happy':'0.85','sad':'0.01','neutral':'0.20','angry':'0.08'}),
        (5,{'happy':'0.05','sad':'0.23','neutral':'0.67','angry':'0.10'}),
        (6,{'happy':'0.56','sad':'0.10','neutral':'0.33','angry':'0.15'}),
        (7,{'happy':'0.20','sad':'0.60','neutral':'0.15','angry':'0.40'}),
        (8,{'happy':'0.45','sad':'0.25','neutral':'0.50','angry':'0.05'}),
        (9,{'happy':'0.85','sad':'0.01','neutral':'0.20','angry':'0.08'}),
        (10,{'happy':'0.05','sad':'0.23','neutral':'0.67','angry':'0.10'}),
        (11,{'happy':'0.56','sad':'0.10','neutral':'0.33','angry':'0.15'}),
        (12,{'happy':'0.20','sad':'0.60','neutral':'0.15','angry':'0.40'}),
        (13,{'happy':'0.45','sad':'0.25','neutral':'0.50','angry':'0.05'}),
        (14,{'happy':'0.85','sad':'0.01','neutral':'0.20','angry':'0.08'}),
        (15,{'happy':'0.05','sad':'0.23','neutral':'0.67','angry':'0.10'})]

happy = [x[1]['happy'] for x in temp]
sad = []
neutral = filter(lambda val : val[1]['neutral'])
angry = filter(lambda val : val[1]['angry'])

print happy
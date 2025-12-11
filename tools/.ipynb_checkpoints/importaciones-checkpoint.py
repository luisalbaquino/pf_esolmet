import pandas as pd

def importa_excel(f):
    tmx = pd.read_csv(f,encoding="UTF-8",sep=",",skiprows=[0,2,3],index_col=0, parse_dates=True)
    tmx = tmx[tmx.index.year==2023]
    return tmx
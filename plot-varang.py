#!/usr/bin/python

"""
читаем файлы из командной строки и строим данные на одном графике.

все файлы должны иметь одинаковый формат.

предполагается, что энергия во всех данных одинакова.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

mang="12"

def plotData(x,y,figname,xlab,ylab,title):
  """
  plot y with x
  """
  
  fig,ax=plt.subplots(layout='constrained')

  ax.set_title(title)
  for t in y: 
    ax.plot(x,t,'r.-')
  ax.set_xscale('log')
  ax.set_xlabel(xlab)
  ax.set_ylabel(ylab)
  ax.grid(True)

  fig.align_labels()

  fig.savefig(figname)

  plt.close()


def main(args):
  """
  main function
  """
  if len(args) <= 1:
    sys.exit("pass to the script at least one data file.")
  
  e=[]
  y=[]
  ang=[]
  fk=[]
  for itm in args[1:]:
    x,e,p,ang,fk=np.loadtxt(itm, unpack=True)
    y.append(p)
  p=np.array(y)

  fgn=f"sun-ang{mang}.pdf"
  plotData(e,p,fgn,f'$E$',r"$P$",f"survival prob. for Sun, varying angle {mang}")


if __name__ == "__main__":
  try:
    main(sys.argv)
  except KeyboardInterrupt:
    sys.exit("Interrupted by user")

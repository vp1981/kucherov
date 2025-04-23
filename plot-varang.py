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

def plotData(x,y,scales,figname,xlab,ylab,title):
  """
  plot y with x
  """
  
  fig,ax=plt.subplots(layout='constrained')

  ax.set_title(title)
  for prb, s in zip(y,scales):
    fc=int(100*np.float64(s[0]))
    ax.plot(x,prb,'.-', label=f"{fc}%")
  ax.set_xscale('log')
  ax.set_xlabel(xlab)
  ax.set_ylabel(ylab)
  ax.grid(True)
  hdl,lbs=ax.get_legend_handles_labels()
  ax.legend(hdl,lbs)

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
  sc=[]
  for itm in args[1:]:
    x,e,p,ang,fk=np.loadtxt(itm, unpack=True)
    y.append(p)
    sc.append(fk)
  p=np.array(y)
  
  fgn=f"sun-ang{mang}.pdf"
  tit="Survival prob. for Sun\nAngle $\\theta_{" + f"{mang}" + "}$ variation"
  plotData(e,p,sc,fgn,r'$E$',r"$\mathsf{P}$",tit)


if __name__ == "__main__":
  try:
    main(sys.argv)
  except KeyboardInterrupt:
    sys.exit("Interrupted by user")

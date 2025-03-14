#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt


def plotData(x,y,figname,xlab,ylab,title):
  """
  plot y with x
  """
  
  fig,ax=plt.subplots(layout='constrained')

  ax.set_title(title)
  
  ax.plot(x,y,'r.-')
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

  for itm in args[1:]:
    x,e,p,ang,fk=np.loadtxt(itm, unpack=True)
    fgn="sun-ang12.pdf"
    plotData(ang,p,fgn,r'$\theta_{12}$',r"$P$",f"survival prob. for Sun, E={e}")


if __name__ == "__main__":
  try:
    main(sys.argv)
  except KeyboardInterrupt:
    sys.exit("Interrupted by user")

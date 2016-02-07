

import matplotlib
#matplotlib.use('Agg')# //Must be before importing matplotlib.pyplot or pylab!
#import Image
#import matplotlib.pyplot as plt

import pylab as plt
from pylab import *

import numpy as np
#import scipy does not work.
import scipy
import time; tic=time.clock()
#from scipy import loadtxt, size, shape, zeros, mod, floor, mean
from pylab import figure, plot, xlabel, ylabel, legend, xlim, ylim, show, hold, squeeze, sqrt
from bsmart import granger # Load the Granger calculation tool

#t = np.arange(0.0, 1.0+0.01, 0.01)# declare a 3d numpy array. for plotting time samples.


#os.chdir(h.results_dir)
#os.chdir('results') changingdir should be unncessary. Time_courses are already imported.
#time_courses


#These 4 lines convert from NEURON vector to python list, to numpy array.
"""
lfp1=np.array(h.ecpv.to_python())
lfp2=np.array(h.ecpv2.to_python())

vsum1=np.array(h.vsum1.to_python())
vsum2=np.array(h.vsum2.to_python())

becpv=np.array(h.becpv.to_python())
becpv2=np.array(h.becpv2.to_python())

bvsum1=np.array(h.bvsum1.to_python())
bvsum2=np.array(h.bvsum2.to_python())

plt.figure(1)
plt.hold(True)
dfft = abs(scipy.fft(becpv))# ,#h.record_soma))
datafft = dfft[1:250]
plt.plot(datafft)

dfft = abs(scipy.fft(becpv2))# ,#h.record_soma))
datafft = dfft[1:250]
plt.plot(datafft)


#plt.plot(becpv2)
plt.title('LFP signals hippocampus and neocortex before median filter')
#LFP is a sum of synchronous movement of APs down adjacent dendrites with the same orientation
#Filtered with a median filter to remove spikes.
plt.hold(False)

plt.figure(2)
plt.hold(True)

dfft = abs(scipy.fft(bvsum1))# ,#h.record_soma))
datafft = dfft[1:250]
plt.plot(datafft)
dfft = abs(scipy.fft(bvsum2))# ,#h.record_soma))
datafft = dfft[1:250]
plt.plot(datafft)

plt.title('averaged membrane potential signals hippocampus and neocortex before median filter')
#LFP is a sum of synchronous movement of APs down adjacent dendrites with the same orientation
#Filtered with a median filter to remove spikes.
plt.hold(False)

"""
#print lfp1
#print lfp2
plt.figure(3)
plt.hold(True)

plt.plot(lfp1)

plt.plot(lfp2)
plt.title('LFP signals hippocampus and neocortex')
#LFP is a sum of synchronous movement of APs down adjacent dendrites with the same orientation
#Filtered with a median filter to remove spikes.
plt.hold(False)

plt.figure(4)
plt.hold(True)

plt.plot(vsum1)
plt.plot(vsum2)
plt.title('averaged membrane potentials hippocampus and neocortex')

plt.hold(False)


plt.figure(5)
plt.hold(True)
#datafft =abs(scipy.fft(vectorslist[indegree]))# abs(scipy.fft(lfp1))
dfft = abs(scipy.fft(lfp1))# ,#h.record_soma))
datafft = dfft[1:250]
plt.plot(datafft)
dfft2 = abs(scipy.fft(lfp2))# ,#h.record_soma))
datafft2 = dfft2[1:250]
plt.title("FFT power spectrum of the LFP")
#interactive(True)
#figure(figsize=(8, 6), dpi=80)
plt.plot(datafft2)
plt.hold(False)
"""
#if vsum1!=0:
plt.figure(6)
plt.hold(True)
#datafft =abs(scipy.fft(vectorslist[indegree]))# abs(scipy.fft(lfp1))
dfft = abs(scipy.fft(vsum1))# ,#h.record_soma))
datafft = dfft[1:250]
plt.plot(datafft)
dfft2 = abs(scipy.fft(vsum2))# ,#h.record_soma))
datafft2 = dfft2[1:250]
#interactive(True)
#figure(figsize=(8, 6), dpi=80)
plt.plot(datafft2)
plt.title('FFT power spectrum average membrane polential')
plt.hold(False)

print lfp1 
results=[] # Initialize list to store results            
print 'Calculating Granger...'

lfp1=[]
lfp2=[]

#outfile = TemporaryFile()

change_iterator=h.run_iter
weight_value=h.run_iter

f1 = open(str(change_iterator)+str(weight_value)+'savelfp1', 'w')
np.save(f1, np.array(lfp1))

f2 = open(str(change_iterator)+str(weight_value)+'savelfp2', 'w')
np.save(f2, np.array(lfp2))

#I may as well send these files to matlab here too.


#f1 = open(str(change_iterator)+str(weight_value)+'savelfp1', 'w')
np.save(f1, np.array(lfp1))

from scipy import stats
    
#print len(lfp2), len(lfp1)
print lfp1
print lfp2    
""" 


vsum1 = np.array(vsum1)
vsum2 = np.array(vsum2)
#vtotal=vtotal/2 #so its an average again.
in_trace = np.array(in_trace)
out_trace = np.array(in_trace)
in_trace=in_trace/ncell

vsum1=np.subtract(vsum1,in_trace)

#vsum2=vsum2-in_trace/int(ncell) #remove the contribution of indegree cell

F,pp,cohe,Fx2y,Fy2x,Fxy=granger( in_trace , vsum1 , order=20)# nfs2[0], nfs2[1] ,


print "Plotting..."

###
plt.figure(7)
###

# Plot Granger spectra
plt.hold(True) #Matlab style hold
labels=list()
labels=['Fx2y','Fy2x','Fxy','cohe','pp']
alldata=list()
colors=[[0,0,1],[1,0,0],[0,0.5,0.5],[0.5,1,0],[1,0.5,1]]
F1=F
plt.plot(F,Fx2y,label='causality of channel X to channel Y',linewidth=2,c=colors[0])
plt.plot(F,Fy2x,label='causality of channel Y to channel X',linewidth=2,c=colors[1])

plt.plot(F,Fxy,label='causality of channel X to channel Y',linewidth=2,c=colors[2])
plt.plot(F,Fy2x,label='causality of channel Y to channel X',linewidth=2,c=colors[3])
plt.title('GSC components of average membrane potential compared with cell of high indegree')

plt.legend()

#what if I had no such command about the axis would it set limits itself?
#plt.set_autoscale_on(True)
#plt.autoscale_view(True,True,True)
plt.ylim(-3,6)

#plt.ylim(-1,2)
#plt.xlim(0,2)
plt.hold(False) #Matlab style hold

plt.figure(8)
plt.hold(True) #Matlab style hold

plt.plot(F,pp,label='causality of channel X to channel Y',linewidth=2,c=colors[2])
plt.plot(F,cohe,label='coherance between two signals Y to channel X',linewidth=2,c=colors[3])
#plt.ylim(0,9)
#plt.xlim(0,4)
plt.hold(False) #Matlab style hold
plt.legend()
plt.title('GSC coherance and causality LFPs')


vsum1[:]=vsum2[:]+in_trace[:]/int(ncell) #add back the contribution of indegree cell
vsum1[:]=vsum2[:]-out_trace[:]/int(ncell) #remove the contribution of outdegree cell



#vtotal=vtotal+in_trace/ncell#add in degree cells contribution back.

#vtotal=vtotal-out_trace/ncell # subtract out degrees contribution
F,pp,cohe,Fx2y,Fy2x,Fxy=granger( vsum1 ,out_trace , order=20)# nfs2[0], nfs2[1] ,

###
plt.figure(9)
###

# Plot Granger spectra
plt.hold(True) #Matlab style hold
labels=list()
labels=['Fx2y','Fy2x','Fxy','cohe','pp']
alldata=list()
colors=[[0,0,1],[1,0,0],[0,0.5,0.5],[0.5,1,0],[1,0.5,1]]
F1=F
plt.plot(F,Fx2y,label='causality of channel X to channel Y',linewidth=2,c=colors[0])
plt.plot(F,Fy2x,label='causality of channel Y to channel X',linewidth=2,c=colors[1])

plt.plot(F,Fxy,label='causality of channel X to channel Y',linewidth=2,c=colors[2])
plt.plot(F,Fy2x,label='causality of channel Y to channel X',linewidth=2,c=colors[3])
plt.hold(False) #Matlab style hold
plt.legend()
plt.ylim(-10,10)
#plt.xlim(0,2)
plt.title('GSC components of averaged membrane with cell membrane time course of cell high out degree')


"""
F is the frequency vector for the remaining quantities
pp is the spectral power
cohe is the coherence
Fx2y is the causality of channel X to channel Y
Fy2x is the causality of channel Y to channel X
Fxy is the "instantaneous" causality (cohe-Fx2y-Fy2x I think)"""

plt.figure(10)
plt.hold(True) #Matlab style hold

plt.plot(F,pp,label='causality of channel X to channel Y',linewidth=2,c=colors[2])
plt.plot(F,cohe,label='coherance between two signals Y to channel X',linewidth=2,c=colors[3])
#plt.ylim(-0,9)
#plt.xlim(0,4)
plt.legend()
plt.hold(False) #Matlab style hold
plt.title('GSC components of coherance and causality for average membrane potential')

plt.show()

"""
print "does not get here"
print os.getcwd()
print h.getcwd()
print matplotlib.use('Agg')
#print Agg
print plt
plt.savefig(str(change_iterator)+str(weight_value)+'SGCLFP.png')

#print "does not get here"
plt.hold(False)


#alldata.append(results)
plt.xlim(0,150)
plt.ylim(-0.10,1) # Need to define explicitly since otherwise plot tries to approximate infinity
weight_value=0
weight_value=h.i#h.w



plt.xlabel('Frequency (Hz)')
plt.ylabel('power')
run_iterator=str(h.run_iterator)
plt.title(str(run_iterator)+str(weight_value)+' SGC of LFP ch1,ch2')
plt.legend()

#plt.savefig(str(change_iterator)+str(weight_value)+'SGCofLFP.png')
plt.show()
plt.close
#End first SGC plot

plt.hold(False)
print 'plotted GC'

F,pp,cohe,Fx2y,Fy2x,Fxy=granger(vectorslist[indegree], vectorslist[outdegree],order=20) 
#vectorslist[int(h.i)]


print "Plotting..."


###
plt.figure(2)
###
# Plot Granger spectra
plt.hold(True) #Matlab style hold
labels=list()
labels=['Fx2y','Fy2x','Fxy','cohe','pp']
alldata=list()
colors=[[0,0,0.5],[0.5,0,0],[0,0.5,0.5],[0.5,0.5,0],[0.5,0.5,0.5]]
plt.plot(F,Fx2y,label='causality of channel X to channel Y',linewidth=2,c=colors[0])
plt.plot(F,Fy2x,label='causality of channel Y to channel X',linewidth=2,c=colors[1])
#plot(F,Fxy,label='instantaneous causalit',linewidth=2,c=colors[2])
#plot(F,cohe,label='coherance',linewidth=2,c=colors[3])
#plot(F,pp,label='spectral power',linewidth=2,c=colors[4])
alldata.append(results)
plt.xlim(0,50)
plt.ylim(0,4) # Need to define explicitly since otherwise plot tries to approximate infinity
weight_value=0
weight_value=h.w
change_iterator=h.change_iterator
plt.xlabel('Frequency (Hz)')
plt.ylabel('power')
plt.title(str(change_iterator)+str(weight_value)+' SGC of neuron 24 and 9')
plt.legend()
#show()
#plt.savefig(str(change_iterator)+str(weight_value)+'SGCofMembtimecourse.png')
plt.show()
plt.close


hold(False)
print 'plotted GC'



datafft =abs(scipy.fft(vectorslist[indegree]))# abs(scipy.fft(lfp1))
datafft2 =abs(scipy.fft(vectorslist[outdegree]))# abs(scipy.fft(lfp2))
datafft2 = datafft2[1:200]
datafft = datafft[1:200]

###
plt.figure(3)
###
hold(True)

plt.plot(datafft,label='indegree cell')
plt.plot(datafft2,label='outdegree cell')
#The MATLAB convention is to counter intuitively supply labels after the plot command is given.
plt.xlabel('Frequency (Hz)')
plt.ylabel('power')
plt.title('Fourier transform of high indgree and high outdegree cell')
plt.show()
plt.hold(False)

#plt.savefig(str(change_iterator)+str(weight_value)+'FFT.png')
plt.close()


##
# The question that FFT spectrum answers is what kind of filter is 
# The neural network.
##



print 'plottedFFT'
""" 
"""
###
###
plt.plot(datafft2,label='FFT of LFP channel 2')
plt.plot(datafft,label='FFT of LFP channel 1')
plt.title('Fourier LFP chan1 and LFP chan2')

#show()
plt.hold(False)
#plt.savefig(str(change_iterator)+str(weight_value)+'FFTofLFP2.png')
plt.close()
plt.show()
##
plt.figure(5)

# Prefer to make these plots before binning of the vectors.

dend_tvec = h.dend_tvec.to_python()
ones=[1]*len(dend_tvec)
plt.scatter(dend_tvec,ones)
plt.show()
#plt.savefig(str(change_iterator)+str(weight_value)+'spikes_dendrite.png')
plt.close()

plt.figure(6)


ones=[1]*len(axon_tvec)

plt.scatter(axon_tvec,ones)
plt.show()
#plt.savefig(str(change_iterator)+str(weight_value)+'spikes_axon.png')
plt.close()

toc=time.clock()
print toc
print 'Done; elapsed time was %0.1f seconds.' % (toc-tic)


corrbd2=stats.spearmanr(lfp1 , lfp2)
corrbd1=stats.spearmanr(vectorslist[indegree] , vectorslist[outdegree])


plt.figure(7)
im=imshow(Matrix2)
plt.colorbar(im)
plt.xlabel('columns = targets')
plt.ylabel('rows = sources')
plt.title('Adjacency matrix')
#plt.savefig('connection_matrix3.png')  

plt.savefig(str(change_iterator)+str(weight_value)+'adjacency_matrix.png')
plt.close()
  
"""


#os.chdir(h.workingdir)


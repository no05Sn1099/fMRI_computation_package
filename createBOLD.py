def createBOLD(neuralImpulse,noiseSD):
    
    
    # neuralImpulse: should be integer
    # noiseSD: 0.01? or other small number
    

    # set the HRF
    tau = 2 # smaller: large amplitude of HRF
    delta = 2 # delay of HRF
    t = np.arange(0,31,1) # 30 sec
    tshift = np.maximum(t-delta,0) # if t-delta < 0, then replace it with 0
    hrf = (tshift/tau)**2*np.exp(-tshift/tau)/(2*tau) # gamma distribution
    #plt.plot(hrf)
    #plt.show()
    
    
    # baseline and stimuli presented time
    baseline = 100
    ts = np.zeros(len(t))
    sti_s = 1 # impulse start
    sti_e = 2 # impulse end
    ts[sti_s], ts[sti_e] = neuralImpulse, neuralImpulse
    
    
    # convolve HRF
    win_size = len(hrf)
    #BOLD = baseline + np.convolve(ts,hrf)[int(win_size/2):-int((win_size/2-1))]
    BOLD = baseline + np.convolve(ts,hrf)[:-int((win_size)-1)]
    
    
    # add noise
    noise = np.random.normal(0,noiseSD,len(BOLD))
    BOLD = noise + BOLD
    
    #plt.plot(BOLD)
    #plt.show()
    
    return BOLD

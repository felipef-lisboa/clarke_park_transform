#! /usr/bin/python3

# Tkinter test
print('Tkinter tests\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

from tkinter import *
from tkinter import ttk

import numpy as np
import matplotlib.pyplot as plt
import transforms as trs

### Function that transforms and
### plots the results
def ex_transform(*args):
    if mag_phaseA.get()=="" or mag_phaseB.get()=="" or mag_phaseC.get()=="" or freq.get()=="" or unit.get()=="" or delta.get()=="" or ang_phaseA.get()=="" or ang_phaseB.get()=="" or ang_phaseC.get()=="":
        return 0

    # Creates simulation time-space
    end_time = 10/float(freq.get())
    step_size = end_time/(1000)
    t = np.arange(0,end_time,step_size)
    wt = 2*np.pi*float(freq.get()) * t

    # Converts user input angle from degrees to radians
    rad_angA = float(ang_phaseA.get())*np.pi/180
    rad_angB = float(ang_phaseB.get())*np.pi/180
    rad_angC = float(ang_phaseC.get())*np.pi/180

    # Generates the three-phase system ABC
    if mag_val.get()=="peak":
        A = float(mag_phaseA.get())*np.sin(wt+rad_angA)
        B = float(mag_phaseB.get())*np.sin(wt+rad_angB)
        C = float(mag_phaseC.get())*np.sin(wt+rad_angC)
    else:
        if mag_val.get()=="rms":
            A = (np.sqrt(2)*float(mag_phaseA.get()))*np.sin(wt+rad_angA)
            B = (np.sqrt(2)*float(mag_phaseB.get()))*np.sin(wt+rad_angB)
            C = (np.sqrt(2)*float(mag_phaseC.get()))*np.sin(wt+rad_angC)
        else:
            return 0

    # Apply the selected fault
    if fault.get() == 'Monophasic A':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            A[ii]=0
    elif fault.get() == 'Monophasic B':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            B[ii]=0
    elif fault.get() == 'Monophasic C':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            C[ii]=0
    elif fault.get() == 'Two-phase A-B-ground':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            A[ii]=0
            B[ii]=0
    elif fault.get() == 'Two-phase A-B':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            A[ii]=B[ii]
    elif fault.get() == 'Two-phase B-C-ground':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            B[ii]=0
            C[ii]=0
    elif fault.get() == 'Two-phase B-C':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            B[ii]=C[ii]
    elif fault.get() == 'Two-phase C-A-ground':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            C[ii]=0
            A[ii]=0
    elif fault.get() == 'Two-phase C-A':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            C[ii]=A[ii]
    elif fault.get() == 'Three-phase-ground':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            C[ii]=0
            B[ii]=0
            A[ii]=0
    elif fault.get() == 'Three-phase':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            C[ii]=A[ii]
            B[ii]=A[ii]
    elif fault.get() == 'Sag A':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            A[ii]=A[ii]*float(sag.get())/100
    elif fault.get() == 'Sag AB':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            A[ii]=A[ii]*float(sag.get())/100
            B[ii]=B[ii]*float(sag.get())/100
    elif fault.get() == 'Sag ABC':
        for ii in range(int(len(t)/4), int(3*len(t)/4)):
            A[ii]=A[ii]*float(sag.get())/100
            B[ii]=B[ii]*float(sag.get())/100
            C[ii]=C[ii]*float(sag.get())/100

    # Converts user input delta from degrees to radians
    delta_rad = float(delta.get())*np.pi/180 # convert delta to radians
    ## Call to transformation functions ##
    # Clarke Transform: ABC to Alpha-Beta-0
    alpha, beta, zero1 = trs.abc_to_alphaBeta0(A,B,C)

    # Clarke to Park Transform: Alpha-Beta-0 to dq0
    d, q, zero2 = trs.alphaBeta0_to_dq0(alpha, beta, zero1, wt, delta_rad)

    # Inverse Park Transform: dq0 to ABC
    a,b,c = trs.dq0_to_abc(d, q, zero2, wt, delta_rad)

    plt.clf() # clear any previous plots
    # Plot the 3-phase system
    plt.subplot(411)
    plt.plot(t, A, label="A")
    plt.plot(t, B, label="B")
    plt.plot(t, C, label="C")
    plt.ylabel(unit.get())
    plt.legend(ncol=3,loc=4)
    plt.grid('on')

    # Plot the alphaBeta0 system
    plt.subplot(412)
    plt.plot(t, alpha, label="\u03B1")
    plt.plot(t, beta, label="\u03B2")
    plt.plot(t, zero1, label="zero")
    plt.ylabel(unit.get())
    plt.legend(ncol=3,loc=4)
    plt.grid('on')

    # Plot the dq0 system
    plt.subplot(413)
    plt.plot(t, d, label="d")
    plt.plot(t, q, label="q")
    plt.plot(t, zero2, '-', label="zero")
    plt.xlabel('Time [s]')
    plt.ylabel(unit.get())
    plt.legend(ncol=3,loc=4)
    plt.grid('on')

    # Plot the abc transformed from dq0
    plt.subplot(414)
    plt.plot(t, a, label="A")
    plt.plot(t, b, label="B")
    plt.plot(t, c, label="C")
    plt.ylabel(unit.get())
    plt.legend(ncol=3,loc=4)
    plt.grid('on')
    plt.show()
########################################
#### Function to validate user input
def validate_val(char):
    return  char=="." or char.isdigit() or char=="-"
########################################

root = Tk()
root.title("Clarke's and Park's Transformations")
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

validation = mainframe.register(validate_val)

### Creating variables to store user input
mag_phaseA = StringVar() # stores magnitude of phase A
ang_phaseA = StringVar() # stores angle of phase A
mag_phaseB = StringVar() # stores magnitude of phase B
ang_phaseB = StringVar() # stores angle of phase B
mag_phaseC = StringVar() # stores magnitude of phase C
ang_phaseC = StringVar() # stores angle of phase C
freq = StringVar() # stores the system frequency os oscilation
unit = StringVar() # stores the system unit
fault = StringVar() # stores the system fault type
mag_val = StringVar() # stores the type of magnitude used
delta = StringVar() # stores the angle in degrees between the A and d axis in clarke trans.
sag= StringVar() # stores the voltage sag in % for sag faults
########################################

# Creates label and Combobox for system unit
ttk.Label(mainframe, text="Unit:").grid(column=1, row=1, sticky=E)
unit_combobox = ttk.Combobox(mainframe, state="readonly", textvariable=unit, width=15)
unit_combobox.grid(column=2,row=1, sticky=(W,E))
unit_combobox['values'] = ('Voltage [V]', 'Voltage [kV]')
unit_combobox.bind('<FocusOut>', lambda e: unit_combobox.selection_clear())
unit_combobox.current(0)
########################################

# Creates label and radio buttons for magnitude selection
ttk.Label(mainframe, text="Magnitude:"). grid(column=1, row=2, sticky=E)
## creates frame to hold radio buttons nicely
radio_frame=ttk.Frame(mainframe, padding=("10 0 0 0"))
radio_frame.grid(column=2, row=2, sticky=(W, E))
peak_val = ttk.Radiobutton(radio_frame, text="Peak", variable=mag_val, value="peak")
peak_val.grid(column=1, row=1, sticky=(W, E))
rms_val = ttk.Radiobutton(radio_frame, text="RMS", variable=mag_val, value="rms")
rms_val.grid(column=2,row=1, sticky=(W, E))
rms_val.invoke()
########################################

# Creates label and text entry for frequency
ttk.Label(mainframe, text="Frequency [Hz]:").grid(column=1, row=3, sticky=W)
freq_entry = ttk.Entry(mainframe, validate="key", validatecommand=(validation, '%S'), width=7, textvariable=freq)
freq_entry.grid(column=2, row=3, sticky=W)
freq_entry.insert(0, "60")
########################################

# Creates label and Combobox for fault type
ttk.Label(mainframe, text="Fault:").grid(column=1, row=4, sticky=E)
fault_combobox = ttk.Combobox(mainframe, state="readonly", textvariable=fault, width=15)
fault_combobox.grid(column=2,row=4, sticky=(W,E))
fault_combobox['values'] = ('None','Monophasic A', 'Monophasic B', 'Monophasic C', 'Two-phase A-B-ground', 'Two-phase A-B', 'Two-phase B-C-ground', 'Two-phase B-C','Two-phase C-A-ground', 'Two-phase C-A', 'Three-phase-ground', 'Three-phase', 'Sag A', 'Sag AB', 'Sag ABC')
fault_combobox.bind('<FocusOut>', lambda e: fault_combobox.selection_clear())
fault_combobox.current(0)
########################################

# Creates label and text entry for magnitude of phase A
ttk.Label(mainframe, text="Phase A:", padding=("10 0 0 0")).grid(column=3, row=1, sticky=E)
mag_phaseA_entry = ttk.Entry(mainframe, validate="key", validatecommand=(validation, '%S'), width=7, textvariable=mag_phaseA)
mag_phaseA_entry.grid(column=4, row=1, sticky=(W, E), pady=3)
mag_phaseA_entry.insert(0,"1")
########################################
# Creates label and text entry for angle of phase A
ttk.Label(mainframe, text="angle:", padding=("5 0 0 0")).grid(column=5, row=1, sticky=E)
ang_phaseA_entry = ttk.Entry(mainframe, validate="key", validatecommand=(validation, '%S'), width=7, textvariable=ang_phaseA)
ang_phaseA_entry.grid(column=6, row=1, sticky=(W), pady=3)
ang_phaseA_entry.insert(0,"0")
########################################

# Creates label and text entry for magnitude of phase B
ttk.Label(mainframe, text="Phase B:",padding=("10 0 0 0")).grid(column=3, row=2, sticky=E)
mag_phaseB_entry = ttk.Entry(mainframe, validate="key", validatecommand=(validation, '%S'), width=7, textvariable=mag_phaseB)
mag_phaseB_entry.grid(column=4, row=2, sticky=(W, E), pady=3)
mag_phaseB_entry.insert(0,"1")
########################################
# Creates label and text entry for angle of phase B
ttk.Label(mainframe, text="angle:",padding=("5 0 0 0")).grid(column=5, row=2, sticky=E)
ang_phaseB_entry = ttk.Entry(mainframe, validate="key", validatecommand=(validation, '%S'), width=7, textvariable=ang_phaseB)
ang_phaseB_entry.grid(column=6, row=2, sticky=(W), pady=3)
ang_phaseB_entry.insert(0,"120")
########################################

# Creates label and text entry for magnitude of phase C
ttk.Label(mainframe, text="Phase C:", padding=("10 0 0 0")).grid(column=3, row=3, sticky=E)
mag_phaseC_entry = ttk.Entry(mainframe, validate="key", validatecommand=(validation, '%S'), width=7, textvariable=mag_phaseC)
mag_phaseC_entry.grid(column=4, row=3, sticky=(W, E), pady=3)
mag_phaseC_entry.insert(0,"1")
########################################
# Creates label and text entry for angle of phase C
ttk.Label(mainframe, text="angle:", padding=("5 0 0 0")).grid(column=5, row=3, sticky=E)
ang_phaseC_entry = ttk.Entry(mainframe, validate="key", validatecommand=(validation, '%S'), width=7, textvariable=ang_phaseC)
ang_phaseC_entry.grid(column=6, row=3, sticky=(W), pady=3)
ang_phaseC_entry.insert(0,"240")
########################################

# Creates label and text entry for delta
ttk.Label(mainframe, text="delta [degrees]:", padding=("10 0 0 0")).grid(column=3, row=4, sticky=E)
delta_entry = ttk.Entry(mainframe, validate="key", validatecommand=(validation, '%S'), width=7, textvariable=delta)
delta_entry.grid(column=4, row=4, sticky=(W,E), pady=3)
delta_entry.insert(0,"0")
########################################
# Creates label and tesxt entry for sag
ttk.Label(mainframe, text="sag %:", padding=("5 0 0 0")).grid(column=5, row=4, sticky=E)
sag_entry = ttk.Entry(mainframe, validate="key", validatecommand=(validation, '%S'), width=7, textvariable=sag)
sag_entry.grid(column=6, row=4, sticky=(W), pady=3)
sag_entry.insert(0,"50")


# Creates button to call transformation function
trans_button = ttk.Button(mainframe, text="Calculate", command=ex_transform,padding=("3 3 3 3"))
trans_button.grid(column=6, row=5, pady= 10,sticky=E)
########################################

root.mainloop() # Starts Tkinter loop

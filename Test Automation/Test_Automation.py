import visa, time, sys, os, shutl, pythoncom
from visa import *
from pyvisa import vpp43
import win32com.client as win32
from math import sqrt
import numpy as np

#This is the RF Switch Control Module
from Agilent_RF_Switch_Module import RF_Switch_Channel_Select

#Measurment loop
from Avaton_DFLB_Measurement_Loop_Module import DFLB_Measurement_Loop

#Importing ActiveX Control
BER = win32.gencache.EnsureDispatch("tmMeasurement.BER.1");
excel = win32.gencache.EnsureDispatch("Excel.Application")


#Configuring communication with the device

#Importing NOISECOM
noise = visa.instrument('GPIB::8')
noise.write('NA')

#Import TEK AWG
awg710 = visa.instrument("GPIB") # Recommendation: Use the GPIB port the device is connected to

#Connection to ParBERT
myinst = vpp43.open(resource_manager.session,"TCPIPO::localhost::5025::SOCKET", access_mode = 0, open timeout = 5000)




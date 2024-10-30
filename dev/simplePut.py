from cothread import catools
val = str("PCAP.ACTIVE")
response = catools.caput('BL20J-EA-PANDA-01:SEQ1:ENABLE', val, datatype=catools.DBR_STRING)
print(response)

# catools.caput('BL20J-EA-PANDA-01:SEQ1:ENABLE', "PCAP.ACTIVE", datatype=catools.DBR_CHAR_STR)

#!/usr/bin/env python3

from obspy import read

st = read("sinewave.mseed")
if st:
    st[0].plot()

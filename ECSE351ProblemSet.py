#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Thresholding Demonstration
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import threading



class ECSE351ProblemSet(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Thresholding Demonstration", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Thresholding Demonstration")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "ECSE351ProblemSet")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.relative_scale = relative_scale = 1
        self.mod_index = mod_index = .5
        self.f_mod = f_mod = 5000
        self.f_carrier = f_carrier = 10000
        self.AM_amp = AM_amp = 1

        ##################################################
        # Blocks
        ##################################################

        self._relative_scale_range = qtgui.Range(1, 100000, 10000, 1, 200)
        self._relative_scale_win = qtgui.RangeWidget(self._relative_scale_range, self.set_relative_scale, "'relative_scale'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._relative_scale_win)
        self._mod_index_range = qtgui.Range(0, 1, .1, .5, 200)
        self._mod_index_win = qtgui.RangeWidget(self._mod_index_range, self.set_mod_index, "'mod_index'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._mod_index_win)
        self._f_mod_range = qtgui.Range(2500, 10000, 250, 5000, 200)
        self._f_mod_win = qtgui.RangeWidget(self._f_mod_range, self.set_f_mod, "'f_mod'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._f_mod_win)
        self._f_carrier_range = qtgui.Range(5000, 15000, .1, 10000, 200)
        self._f_carrier_win = qtgui.RangeWidget(self._f_carrier_range, self.set_f_carrier, "'f_carrier'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._f_carrier_win)
        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.blocks_throttle2_0_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_multiply_xx_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_divide_xx_0 = blocks.divide_cc(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_1_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f_carrier, 1, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f_carrier, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 200, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f_mod, 1, 0, 0)
        self.analog_const_source_x_3_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, relative_scale)
        self.analog_const_source_x_1_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 1.0)
        self.analog_const_source_x_1 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 1.0)
        self.analog_const_source_x_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, mod_index)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, mod_index)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=samp_rate,
        	audio_decim=1,
        	audio_pass=5000,
        	audio_stop=5500,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_am_demod_cf_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_const_source_x_1_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_const_source_x_3_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.analog_am_demod_cf_0, 0))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_throttle2_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.blocks_divide_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "ECSE351ProblemSet")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_relative_scale(self):
        return self.relative_scale

    def set_relative_scale(self, relative_scale):
        self.relative_scale = relative_scale
        self.analog_const_source_x_3_0.set_offset(self.relative_scale)

    def get_mod_index(self):
        return self.mod_index

    def set_mod_index(self, mod_index):
        self.mod_index = mod_index
        self.analog_const_source_x_0.set_offset(self.mod_index)
        self.analog_const_source_x_0_0.set_offset(self.mod_index)

    def get_f_mod(self):
        return self.f_mod

    def set_f_mod(self, f_mod):
        self.f_mod = f_mod
        self.analog_sig_source_x_0.set_frequency(self.f_mod)

    def get_f_carrier(self):
        return self.f_carrier

    def set_f_carrier(self, f_carrier):
        self.f_carrier = f_carrier
        self.analog_sig_source_x_1.set_frequency(self.f_carrier)
        self.analog_sig_source_x_1_0.set_frequency(self.f_carrier)

    def get_AM_amp(self):
        return self.AM_amp

    def set_AM_amp(self, AM_amp):
        self.AM_amp = AM_amp




def main(top_block_cls=ECSE351ProblemSet, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()

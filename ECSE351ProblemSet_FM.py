#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: pieterverbeek
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



class ECSE351ProblemSet_FM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "ECSE351ProblemSet_FM")

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
        self.sensitivity_2 = sensitivity_2 = .5
        self.sensitivity_1 = sensitivity_1 = 10000
        self.scale = scale = 1
        self.samp_rate = samp_rate = 500000
        self.f_mod_2 = f_mod_2 = 1000
        self.f_mod_1 = f_mod_1 = 1000
        self.FM_amp = FM_amp = 1

        ##################################################
        # Blocks
        ##################################################

        self._sensitivity_2_range = qtgui.Range(0, 10, .2, .5, 200)
        self._sensitivity_2_win = qtgui.RangeWidget(self._sensitivity_2_range, self.set_sensitivity_2, "'sensitivity_2'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._sensitivity_2_win)
        self._sensitivity_1_range = qtgui.Range(5000, 15000, .1, 10000, 200)
        self._sensitivity_1_win = qtgui.RangeWidget(self._sensitivity_1_range, self.set_sensitivity_1, "'sensitivity_1'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._sensitivity_1_win)
        self._scale_range = qtgui.Range(1, 100000, 100, 1, 200)
        self._scale_win = qtgui.RangeWidget(self._scale_range, self.set_scale, "'scale'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._scale_win)
        self._f_mod_2_range = qtgui.Range(1, 100000, 100, 1000, 200)
        self._f_mod_2_win = qtgui.RangeWidget(self._f_mod_2_range, self.set_f_mod_2, "'f_mod_2'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._f_mod_2_win)
        self._f_mod_1_range = qtgui.Range(1, 100000, 100, 1000, 200)
        self._f_mod_1_win = qtgui.RangeWidget(self._f_mod_1_range, self.set_f_mod_1, "'f_mod_1'", "eng_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._f_mod_1_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_vco_c_0_0 = blocks.vco_c(sensitivity_2, 15000, 1)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, sensitivity_1, 1)
        self.blocks_divide_xx_0 = blocks.divide_cc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, f_mod_2, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, f_mod_1, 1, 0, 0)
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=samp_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=10,
        	tau=(75e-6),
        )
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, scale)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.analog_fm_demod_cf_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.analog_fm_demod_cf_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_vco_c_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.analog_fm_demod_cf_0, 0))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_vco_c_0_0, 0), (self.blocks_divide_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "ECSE351ProblemSet_FM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sensitivity_2(self):
        return self.sensitivity_2

    def set_sensitivity_2(self, sensitivity_2):
        self.sensitivity_2 = sensitivity_2

    def get_sensitivity_1(self):
        return self.sensitivity_1

    def set_sensitivity_1(self, sensitivity_1):
        self.sensitivity_1 = sensitivity_1

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale
        self.analog_const_source_x_0.set_offset(self.scale)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_f_mod_2(self):
        return self.f_mod_2

    def set_f_mod_2(self, f_mod_2):
        self.f_mod_2 = f_mod_2
        self.analog_sig_source_x_0_0.set_frequency(self.f_mod_2)

    def get_f_mod_1(self):
        return self.f_mod_1

    def set_f_mod_1(self, f_mod_1):
        self.f_mod_1 = f_mod_1
        self.analog_sig_source_x_0.set_frequency(self.f_mod_1)

    def get_FM_amp(self):
        return self.FM_amp

    def set_FM_amp(self, FM_amp):
        self.FM_amp = FM_amp




def main(top_block_cls=ECSE351ProblemSet_FM, options=None):

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

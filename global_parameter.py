# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:17:32 2016

@author: rpo
"""

# STAGE POSITIONS
gbl_receiver_x_pos=0.0
gbl_receiver_y_pos=0.0
gbl_receiver_z_pos=0.0
gbl_donor_x_pos=0.0
gbl_donor_y_pos=0.0
gbl_zstage_pos=0.0
gbl_laser_power=0.0

# SOFTWARE LIMITS
gbl_receiver_x_lim_down = 0.00
gbl_receiver_x_lim_up =3.0
gbl_receiver_y_lim_down =0.0
gbl_receiver_y_lim_up =3.0
gbl_receiver_z_lim_down =0.0
gbl_receiver_z_lim_up =3.0
gbl_donor_x_lim_down = 0.0
gbl_donor_x_lim_up = 100.0
gbl_donor_y_lim_down = 0.0
gbl_donor_y_lim_up = 100.0
gbl_zstage_lim_down = 0.0
gbl_zstage_lim_up = 100.0
gbl_laser_power_lim_down = 0.0
gbl_laser_power_lim_up = 100.0

# SCRIPT
gbl_donor_x_refresh_bound = 30
gbl_donor_y_refresh_bound = 15
gbl_donor_refresh_distance=0.05 #mm
gbl_super_pause = False
gbl_super_stop = False
gbl_super_settling_delay=0.5 #s


# Dictionary
gbl_dict = { # STAGE POSITIONS
            'gbl_receiver_x_pos' : gbl_receiver_x_pos,
            'gbl_receiver_y_pos' : gbl_receiver_y_pos,
            'gbl_receiver_z_pos' : gbl_receiver_z_pos,
            'gbl_donor_x_pos' : gbl_donor_x_pos,
            'gbl_donor_y_pos' : gbl_donor_y_pos,
            'gbl_zstage_pos' : gbl_zstage_pos,
            'gbl_laser_power' : gbl_laser_power,
            'gbl_receiver_x_lim_down' : gbl_receiver_x_lim_down,
            'gbl_receiver_x_lim_up' : gbl_receiver_x_lim_up,
            'gbl_receiver_y_lim_down' : gbl_receiver_y_lim_down,
            'gbl_receiver_y_lim_up' : gbl_receiver_y_lim_up,
            'gbl_receiver_z_lim_down' : gbl_receiver_z_lim_down,
            'gbl_receiver_z_lim_up' : gbl_receiver_z_lim_up,
            'gbl_donor_x_lim_down' : gbl_donor_x_lim_down,
            'gbl_donor_x_lim_up' : gbl_donor_x_lim_up,
            'gbl_donor_y_lim_down' : gbl_donor_y_lim_down,
            'gbl_donor_y_lim_up' : gbl_donor_y_lim_up,
            'gbl_zstage_lim_down' : gbl_zstage_lim_down,
            'gbl_zstage_lim_up' : gbl_zstage_lim_up,
            'gbl_laser_power_lim_down' : gbl_laser_power_lim_down,
            'gbl_laser_power_lim_up' : gbl_laser_power_lim_up,
            'gbl_donor_x_refresh_bound' : gbl_donor_x_refresh_bound,
            'gbl_donor_y_refresh_bound' : gbl_donor_y_refresh_bound,
            'gbl_donor_refresh_distance' : gbl_donor_refresh_distance,
            'gbl_super_pause' : gbl_super_pause,
            'gbl_super_stop' : gbl_super_stop,
            'gbl_super_settling_delay' : gbl_super_settling_delay,
            }
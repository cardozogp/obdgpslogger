/* Copyright 2009 Gary Briggs

This file is part of obdgpslogger.

obdgpslogger is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

obdgpslogger is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with obdgpslogger.  If not, see <http://www.gnu.org/licenses/>.
*/

/** \file
 \brief Tool-wide configuration
 */
#ifndef __OBDCONFIGFILE_H
#define __OBDCONFIGFILE_H

#ifdef __cplusplus
extern "C" {
#endif //  __cplusplus

/// This is the config we create
struct OBDGPSConfig {
	const char *obd_device; //< Full path to the obd device
	const char *gps_device; //< Full path to the gps device
	int samplerate; //< SampleRate [number-per-second]
	int optimisations; //< Enable Optimsations
	const char *log_columns; //< Columns to log [comma-separated]
};

/// Load a config, return a struct. Must be free'd using freeOBDGPSConfig
struct OBDGPSConfig *obd_loadConfig(int verbose);

/// Free a config created by loadOBDGPSConfig
void obd_freeConfig(struct OBDGPSConfig *c);

#ifdef __cplusplus
}
#endif //  __cplusplus

#endif //__OBDCONFIGFILE_H


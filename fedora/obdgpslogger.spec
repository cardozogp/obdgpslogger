Name:		obdgpslogger
Version:	0.16
Release:	2%{?dist}
Summary:	Suite of tools to log OBDII and GPS Data

Group:		Applications/Engineering
License:	GPLv2+
URL:		http://icculus.org/obdgpslogger/
Source0:	http://icculus.org/obdgpslogger/downloads/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gpsd-devel
BuildRequires:	dbus-devel
BuildRequires:	bluez-libs-devel
BuildRequires:	fltk-devel
BuildRequires:	fltk-fluid
BuildRequires:	zlib-devel
BuildRequires:	sqlite-devel

%description
OBDII is a standard for getting diagnostic information from your car.
The main tool, obdgpslogger, is a command-line tool to log that data,
with your GPS position, to a database. Provided alongside are various
tools used to convert logs to formats such as CSV or Google Earth KML.
The package also contains an OBDII and ELM327 simulator, obdsim.


%prep
%setup -q
# Removing libs to ensure library code can't leak into the build
rm -rf libs


%build
mkdir build
cd build
%{cmake} -DOBD_SQLITE_INCLUDED_LIB=Off -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}


%install
cd build
make install DESTDIR=%{buildroot}


%files
%doc README COPYING ChangeLog TODO
%{_bindir}/obdgpslogger
%{_bindir}/obdsim
%{_bindir}/obdgui
%{_bindir}/obd2kml
%{_bindir}/obd2csv
%{_bindir}/obd2gpx
%{_bindir}/obdlogrepair
%{_mandir}/man1/obd2csv.1*
%{_mandir}/man1/obd2kml.1*
%{_mandir}/man1/obdgpslogger.1*
%{_mandir}/man1/obdlogrepair.1*
%{_mandir}/man1/obd2gpx.1*
%{_mandir}/man1/obdgui.1*
%{_mandir}/man1/obdsim.1*
%{_mandir}/man5/dot-obdgpslogger.5*



%changelog
* Mon Jun 06 2011 Gary Briggs <chunky@icculus.org> - 0.16-2
- Packaging update based on feedback in RH Bugzilla #709125
- Clean up comments and description section, fix make smp flags
* Sat May 28 2011 Gary Briggs <chunky@icculus.org> - 0.16-1
- Initial release of RPM .spec


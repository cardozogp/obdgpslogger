Name:		obdgpslogger
Version:	0.16
Release:	1%{?dist}
Summary:	Suite of tools to log OBDII and GPS Data

Group:		Applications/Engineering
License:	GPLv2+
URL:		http://icculus.org/obdgpslogger/
Source0:	http://icculus.org/obdgpslogger/downloads/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	cmake,gpsd-devel,dbus-devel,bluez-libs-devel,fltk-devel,fltk-fluid,zlib-devel
Requires:	bluez,gpsd

%description
OBDII is a standard for getting diagnostic information from your car.
The main tool, obdgpslogger, is a command-line tool to log that data,
with your GPS position, to a database. Provided alongside are various
tools used to convert logs to formats such as CSV or Google Eearth KML.
Also contained in the package is an OBDII and ELM327 simulator, obdsim,
that uses plugins to generate data


%prep
%setup -q


%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
%{__make} %{?jobs:-j%jobs}


%install
cd build
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf "%{buildroot}"


%files
%defattr(-,root,root,-)
%doc README COPYING ChangeLog
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*



%changelog
* Sat May 28 2011 Gary Briggs <chunky@icculus.org> - 0.16-1
- Initial release of RPM .spec


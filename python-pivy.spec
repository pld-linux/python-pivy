%define 	rel	5
%define 	module	pivy
Summary:	Coin binding for Python
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki Coin
Name:		python-%{module}
Version:	0.5.0
Release:	0.20110922.%{rel}
License:	ISC
Group:		Development/Languages/Python
# Source0:	http://pivy.coin3d.org/download/pivy/releases/%{version}/%{module}-%{version}.tar.bz2
Source0:	ftp://ftp.debian.org/debian/pool/main/p/pivy/pivy_%{version}~v609hg.orig.tar.bz2
# Source0-md5:	61cc9877c4ac369736540040c3d1cac8
URL:		http://pivy.coin3d.org/
BuildRequires:	Coin-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	SoQt-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	swig
BuildRequires:	swig-python
BuildRequires:	xorg-lib-libXmu-devel
Requires:	python-modules
Provides:	python-Pivy = %{version}-%{release}
Obsoletes:	python-Pivy < 0.5.0-0.20110922.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics
library with a C++ Application Programming Interface. Coin uses
scene-graph data structures to render real-time graphics suitable for
mostly all kinds of scientific and engineering visualization
applications.

%prep
%setup -qc
mv default-*/* .

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--install-lib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%dir %{py_sitedir}/pivy
%dir %{py_sitedir}/pivy/gui
%dir %{py_sitedir}/pivy/quarter
%dir %{py_sitedir}/pivy/quarter/devices
%dir %{py_sitedir}/pivy/quarter/eventhandlers
%dir %{py_sitedir}/pivy/quarter/plugins
%dir %{py_sitedir}/pivy/quarter/plugins/designer
%dir %{py_sitedir}/pivy/quarter/plugins/designer/python

%{py_sitedir}/pivy/*.py[co]
%{py_sitedir}/pivy/gui/*.py[co]
%{py_sitedir}/pivy/quarter/*.py[co]
%{py_sitedir}/pivy/quarter/devices/*.py[co]
%{py_sitedir}/pivy/quarter/eventhandlers/*.py[co]
%{py_sitedir}/pivy/quarter/plugins/designer/python/*.py[co]

%attr(755,root,root) %{py_sitedir}/pivy/_coin.so
%attr(755,root,root) %{py_sitedir}/pivy/gui/_soqt.so

%{py_sitedir}/Pivy-%{version}-py*.egg-info

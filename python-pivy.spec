#
# Conditional build:
%bcond_with	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module	pivy
Summary:	Coin binding for Python 2
Summary(pl.UTF-8):	Interfejs Pythona 2 do biblioteki Coin
Name:		python-%{module}
Version:	0.6.9
Release:	1
License:	ISC
Group:		Libraries/Python
#Source0Download: https://github.com/coin3d/pivy/releases
Source0:	https://github.com/coin3d/pivy/archive/%{version}/pivy-%{version}.tar.gz
# Source0-md5:	16a62b2f89226e06895501e3a62412ba
Patch0:		%{name}-swig-pyver.patch
URL:		https://github.com/coin3d/pivy
BuildRequires:	Coin-devel >= 4.0.0
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	Qt6Gui-devel >= 5
BuildRequires:	Qt6OpenGL-devel >= 5
BuildRequires:	SoQt-devel >= 1.6.3
BuildRequires:	cmake >= 3.5
%{?with_python2:BuildRequires:	python-devel >= 1:2.7}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	qt6-build
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
BuildRequires:	simage-devel
BuildRequires:	swig-python >= 3.0.8
BuildRequires:	xorg-lib-libXmu-devel
Requires:	Coin >= 4.0.0
Requires:	python-modules >= 1:2.7
Provides:	python-Pivy = %{version}-%{release}
Obsoletes:	python-Pivy < 0.5.0-0.20110922.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics
library with a C++ Application Programming Interface. Coin uses
scene-graph data structures to render real-time graphics suitable for
mostly all kinds of scientific and engineering visualization
applications.

%description -l pl.UTF-8
Pivy to wiązania biblioteki Coin dla Pythona. Coin to wysokopoziomowa
biblioteka grafiki 3D z interfejsem programistycznym (API) C++.
Wykorzystuje struktury danych scena-graf do renderowania w czasie
rzeczywistym grafiki w sposób nadający się do większości zastosowań w
wizualizacji naukowej i inżynierskiej.

%package gui
Summary:	GUI (SoQt) support for Python 2 Coin binding
Summary(pl.UTF-8): Obsługa GUI (SoQt) do wiązań biblioteki Coin dla Pythona 2
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	SoQt >= 1.6.3
Requires:	python-PySide2

%description gui
GUI (SoQt) support for Python 2 Coin binding.

%description gui -l pl.UTF-8
Obsługa GUI (SoQt) do wiązań biblioteki Coin dla Pythona 2.

%package -n python3-pivy
Summary:	Coin binding for Python 3
Summary(pl.UTF-8):	Interfejs Pythona 3 do biblioteki Coin
Group:		Libraries/Python
Requires:	Coin >= 4.0.0
Requires:	python3-modules >= 1:3.2

%description -n python3-pivy
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics
library with a C++ Application Programming Interface. Coin uses
scene-graph data structures to render real-time graphics suitable for
mostly all kinds of scientific and engineering visualization
applications.

%description -n python3-pivy -l pl.UTF-8
Pivy to wiązania biblioteki Coin dla Pythona. Coin to wysokopoziomowa
biblioteka grafiki 3D z interfejsem programistycznym (API) C++.
Wykorzystuje struktury danych scena-graf do renderowania w czasie
rzeczywistym grafiki w sposób nadający się do większości zastosowań w
wizualizacji naukowej i inżynierskiej.

%package -n python3-pivy-gui
Summary:	GUI (SoQt) support for Python 3 Coin binding
Summary(pl.UTF-8): Obsługa GUI (SoQt) do wiązań biblioteki Coin dla Pythona 3
Group:		Libraries/Python
Requires:	SoQt >= 1.6.3
Requires:	python3-PySide6
Requires:	python3-pivy = %{version}-%{release}

%description -n python3-pivy-gui
GUI (SoQt) support for Python 2 Coin binding.

%description -n python3-pivy-gui -l pl.UTF-8
Obsługa GUI (SoQt) do wiązań biblioteki Coin dla Pythona 2.

%prep
%setup -q -n pivy-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
mkdir -p build-2
cd build-2
%cmake ../ \
	-DPython_EXECUTABLE=%{__python} \
	-DPIVY_USE_QT6=ON
%{__make}
%endif

%if %{with python3}
mkdir -p build-3
cd build-3
%cmake ../ \
	-DPython_EXECUTABLE=%{__python3} \
	-DPIVY_USE_QT6=ON
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__make} -C build-2 install \
	DESTDIR=$RPM_BUILD_ROOT
%py_postclean
%endif

%if %{with python3}
%{__make} -C build-3 install \
	DESTDIR=$RPM_BUILD_ROOT
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS README.md THANKS
%dir %{py_sitedir}/pivy
%attr(755,root,root) %{py_sitedir}/pivy/_coin.so
%{py_sitedir}/pivy/*.py[co]
%{py_sitedir}/pivy/graphics
%{py_sitedir}/pivy/quarter
%{py_sitedir}/Pivy-%{version}-py*.egg-info

%files gui
%defattr(644,root,root,755)
%dir %{py_sitedir}/pivy/gui
%attr(755,root,root) %{py_sitedir}/pivy/gui/_soqt.so
%{py_sitedir}/pivy/gui/*.py[co]
%{py3_sitedir}/pivy/qt
%endif

%if %{with python3}
%files -n python3-pivy
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS README.md THANKS
%dir %{py3_sitedir}/pivy
%attr(755,root,root) %{py3_sitedir}/pivy/_coin.so
%{py3_sitedir}/pivy/*.py
%{py3_sitedir}/pivy/__pycache__
%{py3_sitedir}/pivy/graphics
%{py3_sitedir}/pivy/quarter
%{?with_qt:%{py3_sitedir}/pivy/qt}
#%{py3_sitedir}/Pivy-%{version}-py*.egg-info

%files -n python3-pivy-gui
%defattr(644,root,root,755)
%dir %{py3_sitedir}/pivy/gui
%attr(755,root,root) %{py3_sitedir}/pivy/gui/_soqt.so
%{py3_sitedir}/pivy/gui/*.py
%{py3_sitedir}/pivy/gui/__pycache__
%{py3_sitedir}/pivy/qt
%endif

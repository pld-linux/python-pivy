%define 	module	Pivy
Summary:	Coin binding for Python
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki Coin
Name:		python-%{module}
Version:	0.5.0
Release:	0.20110922.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Development/Languages/Python
# Source0:	http://pivy.coin3d.org/download/pivy/releases/%{version}/%{module}-%{version}.tar.bz2
Source0:	ftp://ftp.debian.org/debian/pool/main/p/pivy/pivy_%{version}~v609hg.orig.tar.bz2
# Source0-md5:	61cc9877c4ac369736540040c3d1cac8
URL:		http://pivy.coin3d.org/
BuildRequires:	Coin-devel
BuildRequires:	SoQt-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	Coin
Requires:	SoQt
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q -n default-8eab90908f2a

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir}


# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
# %{py_sitedir}/*.py[co]
# %attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/pivy
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-*.egg-info
%endif

#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	commit 9b9fddf
Summary:	A python client implementation of the STOMP protocol
Name:		python-stomper
Version:	0.2.9
Release:	2
License:	Apache v2.0
Group:		Development/Languages
# Latest releases didn't appear on pypi.
# https://github.com/oisinmulvihill/stomper/issues/8
#Source0:        https://pypi.python.org/packages/source/s/stomper/stomper-%{version}.tar.gz
Source0:	https://github.com/oisinmulvihill/stomper/archive/%{commit}/stomper-%{commit}.tar.gz
# Source0-md5:	9a86b59224aa322a46598cd0b1d72177
URL:		https://pypi.python.org/pypi/stomper
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with tests}
BuildRequires:	python-nose
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a python client implementation of the STOMP protocol. The
client is attempting to be transport layer neutral. This module
provides functions to create and parse STOMP messages in a programatic
fashion.

%prep
%setup -qc
mv stomper-%{commit}*/* .

%build
%py_build

%if %{with tests}
PYTHONPATH=. nosetests-%{py_ver} -q
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/stomper/tests

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/stomper
%{py_sitescriptdir}/stomper-%{version}-py*.egg-info

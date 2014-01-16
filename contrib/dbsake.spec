%if 0%{?rhel} == 5
%global pyvertag 26
%global pyver 2.6
%endif

%{!?python_sitelib: %global python_sitelib %(%{__python}%{?pyver} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           dbsake
Version:        1.0.4
Release:        1%{?dist}
Summary:        Database administration toolkit for MySQL
Group:          Applications/Databases

License:        GPLv2
URL:            https://github.com/abg/dbsake
Source0:        https://github.com/abg/dbsake/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python%{?pyvertag}-devel
BuildRequires:  python%{?pyvertag}-setuptools
Requires:       python%{?pyvertag}-setuptools

%description
DBSake is a collection of command-line tools to perform various DBA related
tasks for MySQL.


%prep
%setup -q -n %{name}-%{version}


%build
%{__python}%{?pyver} setup.py build


%install
rm -rf %{buildroot}
%{__python}%{?pyver} setup.py install -O1 --skip-build --root %{buildroot}

 
%files
%doc
# For noarch packages: sitelib
%{python_sitelib}/*
%{_bindir}/dbsake


%changelog
* Thu Jan 16 2014 Andrew Garner <andrew.garner@rackspace.com> - 1.0.3-1
- Added %%pyver and %%pyvertag to allow building against EPEL5
  where python2.6 is not the default python version
- New release

* Tue Jan 07 2014 Andrew Garner <andrew.garner@rackspace.com> - 1.0.2-1
- New release

* Mon Jan 06 2014 Andrew Garner <andrew.garner@rackspace.com> - 1.0.1-1
- New release

* Thu Jan 02 2014 Andrew Garner <andrew.garner@rackspace.com> - 1.0.0-1
- Initial spec from 1.0.0

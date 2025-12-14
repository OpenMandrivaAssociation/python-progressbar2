%global pypi_name progressbar2

Name:		python-%{pypi_name}
Summary:	A Progressbar library to provide visual progress to long running operations
Version:	4.5.0
Release:	1
License:	BSD
Group:		Development/Python
Url:		https://pypi.org/project/%{pypi_name}
Source:		https://files.pythonhosted.org/packages/source/p/progressbar2/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)

%description
A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of the line
is given by a number of widgets.

The progressbar module is very easy to use, yet very powerful. It will also
automatically enable features like auto-resizing when the system supports it.

%files
%{_bindir}/progressbar
%{python3_sitelib}/progressbar/
%{python3_sitelib}/progressbar2-%{version}.dist-info

%define		module_name	elisa
Summary:	"Good" plugins for Moovida
Summary(pl.UTF-8):	"Dobre" wtyczki dla Moovidy
Name:		moovida-plugins-good
Version:	1.0.7
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://www.moovida.com/media/public/%{name}-%{version}.tar.gz
# Source0-md5:	2b6ca9e0e658856d5de411203d36c04a
URL:		http://www.moovida.com/
BuildRequires:	moovida = %{version}
Provides:	moovida-plugins = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Good" plugins for Moovida

%description -l pl.UTF-8
"Dobre" wtyczki dla Moovidy

%prep
%setup -q -n elisa-plugins-good-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

#py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/*.pth
%{py_sitescriptdir}/%{module_name}/plugins/*

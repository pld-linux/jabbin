%define	_beta beta2a
Summary:	Instant messaging and VoIP Jabber client
Name:		jabbin
Version:	2.0
Release:	0.%{_beta}.1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/jabbin/%{name}-%{version}%{_beta}.tar.bz2
# Source0-md5:	b685999c6ba1f9c15eda2d69cc47361e
Patch0:		%{name}-openssl.patch
URL:		http://jabbin.com/
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	qt-devel
BuildRequires:	speex-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jabbin is a Instant messaging and VoIP Jabber client.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%patch0 -p1

%build
qmake jabbin.pro
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

chmod u+x ./install.sh
./install.sh $RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jabbin
%{_datadir}/jabbin

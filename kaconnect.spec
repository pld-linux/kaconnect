Summary:	A frontend for the aconnect utility
Summary(pl):	Nak³adka graficzna dla aconnect
Name:		kaconnect
Version:	1.1.1
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.suse.com/pub/people/mana/kalsatools-current/%{name}-%{version}.tar.bz2
# Source0-md5:	df012e2d7062f9055a031e74fb10f217
Patch0:		%{name}-paths_and_flags.patch
URL:		http://www.suse.de/~mana/kalsatools.html
BuildRequires:	alsa-lib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	alsa-utils

%description
Kaconnect is a QT version of the aconnect utility for the ALSA
sequencer subsystem.

%description -l pl
Kaconnect jest graficzn± nak³adk± opart± o bibliotekê QT dla
subsystemu sekwencera ALSA.

%prep
%setup -q
%patch -p1

%build
%{__make} -f make_kaconnect \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -c kaconnect $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS
%attr(755,root,root) %{_bindir}/*

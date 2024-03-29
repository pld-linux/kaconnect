Summary:	A frontend for the aconnect utility
Summary(pl.UTF-8):	Nakładka graficzna dla aconnect
Name:		kaconnect
Version:	1.1.1
Release:	0.2
License:	GPL
Group:		X11/Applications/Sound
Source0:	ftp://ftp.suse.com/pub/people/mana/kalsatools-current/%{name}-%{version}.tar.bz2
# Source0-md5:	df012e2d7062f9055a031e74fb10f217
Source1:	%{name}.desktop
Patch0:		%{name}-paths_and_flags.patch
URL:		http://www.suse.de/~mana/kalsatools.html
BuildRequires:	alsa-lib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel >= 6:3.0.5
Requires:	alsa-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kaconnect is a Qt version of the aconnect utility for the ALSA
sequencer subsystem.

%description -l pl.UTF-8
Kaconnect jest graficzną nakładką dla podsystemu sekwencera ALSA
opartą o bibliotekę Qt.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f make_kaconnect \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}
install -c kaconnect $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop

Summary:	Wireless network link quality monitor
Summary(pl):	Monitor jako¶ci ³±cza sieci bezprzewodowej
Name:		wmwave
Version:	0.4
Release:	0.1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/wmwave/%{name}-0-4.tgz
# Source0-md5:	8728507eccb01a9749336f53ac4182c5
#Source1:	%{name}.desktop
Patch0:		%{name}-opt.patch
URL:		http://wmwave.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dockapp to display statistical information about a current wireless
ethernet connection.

%description -l pl
Aplet wy¶wietlaj±cy statystyczne informacje o aktualnym ³±czu sieci
bezprzewodowej.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

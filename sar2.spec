#
Summary:	-
Summary(pl.UTF-8):	-
Name:		sar2
Version:	2.3.1
Release:	0.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://sourceforge.net/projects/sar2/files/%{name}-%{version}.tar.bz2
# Source0-md5:	180ad7c3a529e5c7c954b4ef6f758da0
Patch0:		%{name}-OpenAL.patch
URL:		-
BuildRequires:	scons
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	OpenAL-devel
BuildRequires:	freealut-devel
BuildRequires:	libvorbis-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p0

%build
/usr/bin/scons

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,share}
./install.sh $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG INSTALL LICENSE README HACKING
%attr(755, root, root) %{_bindir}/%{name}
%{_mandir}/man6/%{name}*
%{_datadir}/%{name}

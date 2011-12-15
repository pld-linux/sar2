#
Summary:	Open source helicopter simulator for Linux.
Summary(pl.UTF-8):	-
Name:		sar2
Version:	2.3.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://sourceforge.net/projects/sar2/files/%{name}-%{version}.tar.bz2
# Source0-md5:	180ad7c3a529e5c7c954b4ef6f758da0
Patch0:		%{name}-OpenAL.patch
URL:		http://sar2.sourceforge.net/
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
Search and Rescue II is a rescue helicopter simulator for Linux. It features
several missions in which the player pilots a helicopter in order to rescue 
people in distress. There are several scenarios and helicopter models.

SaR II has a strong focus on realistic physics and low graphics requirements.
It is a fork of the game "Search and Rescue" (http://searchandrescue.sf.net), 
originally developed by Wolfpack Entertainment.

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

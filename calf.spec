Summary:	Calf Studio Gear - audio plug-in pack for LV2 and Jack
Name:		calf
Version:	0.90.1
Release:	1
License:	LGPL v2.1, GPL v2
Group:		Applications
Source0:	https://github.com/calf-studio-gear/calf/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6935a982f6372551830a3d1968aae929
Patch0:		fluidsynth2.patch
URL:		http://calf-studio-gear.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	expat-devel
BuildRequires:	fluidsynth-devel >= 1.0.7
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lash-devel
BuildRequires:	libtool
BuildRequires:	lv2-devel
BuildRequires:	slv2-devel
#BuildRequires:	sordi-devel
Requires:	%{name}-lv2 = %{version}-%{release}
Requires:	%{name}-lv2-gui = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoprovfiles        %{_libdir}/lv2

%description
Calf Studio Gear is an audio plug-in pack for LV2 and JACK
environments under LINUX operating systems. The suite contains lots of
effects (delay, modulation, signal processing, filters, equalizers,
dynamics, distortion and mastering effects), instruments (SF2 player,
organ simulator and a monophonic synthesizer) and tools (analyzer,
mono/stereo tools, crossovers). Calf Studio Gear aims for a
professional audience.

%package lv2
Summary:	Calf Studio Gear LV2 plugins
Group:		Libraries

%description lv2
Calf Studio Gear is an audio plug-in pack for LV2 and JACK
environments under LINUX operating systems. The suite contains lots of
effects (delay, modulation, signal processing, filters, equalizers,
dynamics, distortion and mastering effects), instruments (SF2 player,
organ simulator and a monophonic synthesizer) and tools (analyzer,
mono/stereo tools, crossovers). Calf Studio Gear aims for a
professional audience.

This packages contain the LV2 plugins.

%package lv2-gui
Summary:	Calf Studio Gear LV2 plugins GUI
Group:		Libraries
Requires:	%{name}-lv2-gui = %{version}-%{release}

%description lv2-gui
Calf Studio Gear is an audio plug-in pack for LV2 and JACK
environments under LINUX operating systems. The suite contains lots of
effects (delay, modulation, signal processing, filters, equalizers,
dynamics, distortion and mastering effects), instruments (SF2 player,
organ simulator and a monophonic synthesizer) and tools (analyzer,
mono/stereo tools, crossovers). Calf Studio Gear aims for a
professional audience.

This packages contain GUIs for the LV2 plugins.

%package -n bash-completion-calf
Summary:	bash completion for Calf Studio Gear
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów dla Calf Studio Gear
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-calf
Bash completion for Calf Studio Gear.

%description -n bash-completion-calf -l pl.UTF-8
Bashowe dopełnianie parametrów dla Calf Studio Gear.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--with-lv2-dir=%{_libdir}/lv2 \
	--with-bash-completion-dir=%{bash_compdir} \
	--enable-experimental

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md TODO
%attr(755,root,root) %{_bindir}/calfjackhost
%{_desktopdir}/calf.desktop
%{_iconsdir}/hicolor/*/apps/calf.png
%{_iconsdir}/hicolor/scalable/apps/calf.svg
%{_mandir}/man1/calfjackhost.1*
%{_docdir}/%{name}

%files lv2
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}.la
%dir %{_libdir}/lv2/calf.lv2
%{_libdir}/lv2/calf.lv2/*.ttl
%{_libdir}/lv2/calf.lv2/calf.so
%attr(755,root,root) %{_libdir}/%{name}/%{name}.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sf2
%{_datadir}/%{name}/presets.xml
%{_mandir}/man7/calf.7*

%files lv2-gui
%defattr(644,root,root,755)
%{_libdir}/lv2/calf.lv2/calflv2gui.so
%{_datadir}/%{name}/calf-gui.xml
%{_datadir}/%{name}/gui
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/strips
%{_datadir}/%{name}/styles
%{_datadir}/%{name}/gui-*.xml
%{_iconsdir}/hicolor/*/apps/calf_plugin.png
%{_iconsdir}/hicolor/scalable/apps/calf_plugin.svg

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/%{name}

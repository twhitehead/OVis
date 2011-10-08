Name:		ovis
Version:	0.1.0+git20111008
Release:	1%{?dist}.SN.1
Summary:	OVis

Group:		User Interface/Desktops
License:	GPL+
URL:		http://www.sharcnet.ca
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	cmake
Requires(post,postun):	desktop-file-utils

%description
This package contains the SHARCNET Orlando Visualization tool


%prep
%setup -q


%build
%cmake .
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/ovis
%{_datadir}/applications/ovis.desktop
%{_datadir}/icons/hicolor
%doc


%post
update-desktop-database %{_datadir}/applications
touch --no-create %{_datadir}/icons/hicolor
[ -x /usr/bin/gtk-update-icon-cache ] && gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
exit 0


%postun
update-desktop-database %{_datadir}/applications
touch --no-create %{_datadir}/icons/hicolor
[ -x /usr/bin/gtk-update-icon-cache ] && gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
exit 0



%changelog
* Sat Oct 08 2011 Tyson Whitehead <twhitehead@gmail.com> - 0.1.0+git20111008-1.SN.1
- New upstream snapshot

* Thu Sep 29 2011 Tyson Whitehead <twhitehead@gmail.com> - 0.1.0+git20110929-1.SN.1
- Initial package based on current git repo version

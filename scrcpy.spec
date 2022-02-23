%define         pkgname         scrcpy
%global         forgeurl        https://github.com/Genymobile/%{pkgname}
Version:        1.23

%forgemeta -i

Name:           %{pkgname}
Release:        1%{?dist}
Summary:        Display and control your Android device
License:        ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://github.com/Genymobile/%{pkgname}/releases/download/v%{version}/%{pkgname}-server-v%{version}

BuildRequires:  meson gcc
BuildRequires:  java-devel >= 11

BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(libusb-1.0)

Requires:       adb

# https://github.com/Genymobile/scrcpy/blob/master/FAQ.md#issue-with-wayland
Recommends:       libdecor

%description
This application provides display and control of Android devices
connected on USB (or over TCP/IP).

%prep
%forgesetup

%build
%meson -Db_lto=true -Dprebuilt_server='%{S:1}'
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md DEVELOP.md FAQ.md
%{_bindir}/%{pkgname}
%{_datadir}/%{pkgname}
%{_mandir}/man1/%{pkgname}.1*
%{_mandir}/bash-completion/completions/%{pkgname}
%{_mandir}/zsh/site-functions/_%{pkgname}
%{_datadir}/icons/hicolor/*/apps/%{pkgname}.png

%changelog
* Wed Feb 23 2022 Udo Seidel <udoseidel@gmx.de> 1.23-1
- new release

* Sun Nov 14 2021 zeno <zeno@bafh.org> 1.20-3
- fix runtime dependencies

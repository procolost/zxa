%define         pkgname         scrcpy
%global         forgeurl        https://github.com/Genymobile/%{pkgname}
Version:        1.24

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

BuildRequires: ffmpeg
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(libusb-1.0)

Requires:       adb ffmpeg

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
%{_datadir}/icons/hicolor/*/apps/%{pkgname}.png
%{_datadir}/bash-completion/completions/%{pkgname}
%{_datadir}/zsh/site-functions/_%{pkgname}


%changelog
* Fri Apr 29 2022 Udo Seidel <udoseidel@gmx.de> 1.24-1
- Adapt input injection for Android 13 (#3186, #3190)
- Add --no-power-on (#3148, #3210)
- Read $ANDROID_SERIAL if no selector is specified (#3111, #3113)
- Consider emulators as TCP/IP devices (-e) (#3137)
- Apply requested window size in OTG mode (#3099, #3219)
- Add specific exit code for device disconnection (#3083, #3085)
- Enable libusb support for Windows 32-bit releases (#3204, #3206)
- Upgrade libusb to 1.0.26 in Windows releases (#3206)
- Upgrade platform-tools to 33.0.1 (adb) in Windows releases (#3206)
- Upgrade SDL to 2.0.22 in Windows releases
- Upgrade FFmpeg to 5.0.1 in Windows 64-bit releases
- Improve some error messages
- Various technical fixes

* Wed Feb 23 2022 Udo Seidel <udoseidel@gmx.de> 1.23-1
- Add HID/OTG support for Windows (--otg only) (#2773, #3011)
- Add HID/OTG support for macOS (#2774, #3031)
- Improve device selection (list devices, -d, -e) (#3005)
- Downscale and retry on MediaCodec error in more cases (#2990, #3043)
- Add ZSH completion script (#3012)
- Add Bash completion script (#2930, #3048)
- Add --no-cleanup option (#1764, #3020)
- Add --printf-fps (#468, #3030)
- Print both compiled and linked version of libs on --version
- Fix FPS counter (broken in v1.22)
- Various technical refactors and fixes

* Sun Nov 14 2021 zeno <zeno@bafh.org> 1.20-3
- fix runtime dependencies

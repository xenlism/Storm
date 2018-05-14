%global giturl  https://github.com/xenlism/storm
%global srcname Storm
%global project xenlism



Name:           %{project}-storm-icon-theme
Version:        2018.05beta2
Release:        1%{?dist}
Summary:        None form icons theme for X11 Desktop

License:        GPLv3+
URL:            %{giturl}
Source0:        https://github.com/%{project}/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils


%description
Minimalism And Realism Mix and match, macOS icon Style
xenlism is Computer Graphic And Programming project to make something better.
xenlism is about minimalism and realism.
xenlism Storm is icon themes for *nix desktop environment.
xenlism Storm inspired by macOS.

%prep
%setup -qn%{srcname}-%{version}
# W: hidden-file-or-dir, E: zero-length
find icons -name '.*' -print -delete
# W: spurious-executable-perm
#chmod -x Screenshot/*.png


%build
# nothing

%install
# copied from upstream install script
install -dm755 %{buildroot}%{_datadir}
cp -pr icons %{buildroot}%{_datadir}
find  %{buildroot}%{_datadir}/icons -type d -exec chmod 755 '{}' \;
find  %{buildroot}%{_datadir}/icons -type f -exec chmod 644 '{}' \;



%post
/bin/touch --no-create %{_datadir}/icons/Xenlism-Storm* &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Xenlism-Storm* &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Xenlism-Storm* &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Xenlism-Storm* &>/dev/null || :


%files
%license LICENSE
%doc README.md
%{_datadir}/icons/Xenlism-Storm/
%{_datadir}/icons/Xenlism-Storm-Xdwaita-Origin/
%{_datadir}/icons/Xenlism-Storm-Xdwaita-Mint/
%{_datadir}/icons/Xenlism-Storm-Xdwaita-FineDay/
#%%doc Screenshot/

%changelog
* Sun May 13 2018 Nattapong Pullkhow <ixenatt@gmail.com> - 2018.05beta2
- Add Xwaita Folder icons

* Sun May 06 2018 Nattapong Pullkhow <ixenatt@gmail.com> - 2018.05beta1
- Init



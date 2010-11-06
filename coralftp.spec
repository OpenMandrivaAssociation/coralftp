%define name	coralftp
%define version	0.2.2
%define release %mkrel 7

Name: 	 	%{name}
Summary: 	A graphical FTP client
Version: 	%{version}
Release: 	%{release}

Source:		CoralFTP-%{version}.tar.bz2
URL:		https://sourceforge.net/projects/coralftp/
License:	GPLv2+
Group:		Networking/File transfer
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel imagemagick desktop-file-utils 
Requires:	pygtk2.0 pygtk2.0-libglade gnome-python-gconf
BuildArch:	noarch

%description
CoralFTP is a GTK2-based FTP client program written in python. It has an
easy to understand interface, and it's useful for those whose local
charset is different from server's.

CoralFTP does not require gnome-python-gnomevfs or gnome-python-gconf,
but it will use them if available.

%prep
%setup -q -n CoralFTP-%{version}

%install
rm -rf %{buildroot}
./setup.py install --root=%{buildroot}

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Network" \
  --add-category="FileTransfer" \
  --add-category="P2P" \
  --add-category="X-MandrivaLinux-Internet-FileTransfer" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert -size 16x16 data/coralftp.xpm %{buildroot}%{_miconsdir}/%{name}.png
convert -size 32x32 data/coralftp.xpm %{buildroot}%{_iconsdir}/%{name}.png
convert -size 48x48 data/coralftp.xpm %{buildroot}%{_liconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog PKG-INFO README
%{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/*
%{py_puresitedir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

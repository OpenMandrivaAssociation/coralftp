%define name	coralftp
%define version	0.2.2
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	A graphical FTP client
Version: 	%{version}
Release: 	%{release}

Source:		CoralFTP-%{version}.tar.bz2
URL:		https://sourceforge.net/projects/coralftp/
License:	GPL
Group:		Networking/File transfer
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel ImageMagick
Requires:	pygtk2.0 pygtk2.0-libglade 
#Requires:	gnome-python gnome-python-gnomevfs gnome-python-gconf
BuildArch:	noarch

%description
CoralFTP is a GTK2-based FTP client program written in python. It has an
easy to understand interface, and it's useful for those whose local
charset is different from server's.

CoralFTP does not require gnome-python-gnomevfs or gnome-python-gconf,
but it will use them if available.

%prep
%setup -q -n CoralFTP-%version

%install
rm -rf $RPM_BUILD_ROOT
./setup.py install --root=%buildroot

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="Coral FTP" longtitle="Graphical FTP client" section="Internet/File Transfer" xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Network" \
  --add-category="FileTransfer" \
  --add-category="P2P" \
  --add-category="X-MandrivaLinux-Internet-FileTransfer" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 data/coralftp.xpm $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 data/coralftp.xpm $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 data/coralftp.xpm $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog PKG-INFO README
%{_bindir}/%name
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/python*/site-packages/%name
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

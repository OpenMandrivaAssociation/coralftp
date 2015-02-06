%define name	coralftp
%define version	0.2.2
%define release 9

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


%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.2.2-8mdv2011.0
+ Revision: 677618
- rebuild to add gconftool as req

* Sat Nov 06 2010 Jani Välimaa <wally@mandriva.org> 0.2.2-7mdv2011.0
+ Revision: 594339
- rebuild for python 2.7

* Mon Jun 22 2009 Jérôme Brenier <incubusss@mandriva.org> 0.2.2-6mdv2010.0
+ Revision: 388067
- fix license tag

* Sat Jan 24 2009 Funda Wang <fwang@mandriva.org> 0.2.2-5mdv2009.1
+ Revision: 333259
- cleanup spec

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jun 25 2007 Michael Scherer <misc@mandriva.org> 0.2.2-3mdv2008.0
+ Revision: 44160
- coralftp is noarch, so we need to use py_puresitedir

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - fix buildrequires
    - cosmetics
      from James Boothe <jamesb@borkedweb.com> :
      	o Added required dependency gnome-python-gconf
      	o Changes python site dir specification to %%py_platsitedir as per
      	  Mandriva rpm specs
    - Import coralftp



* Wed Sep 13 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.2.2-2mdv2007.0
- XDG

* Sat Aug 27 2005 Austin Acton <austin@mandriva.org> 0.2.2-1mdk
- initial package

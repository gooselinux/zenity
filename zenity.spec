Name:		zenity
Version:	2.28.0
Release:	1%{?dist}
Summary:	Display dialog boxes from shell scripts
Group:		Applications/System
License:	LGPLv2+
URL:		http://directory.fsf.org/zenity.html
Source:		http://download.gnome.org/sources/zenity/2.28/zenity-%{version}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gnome-doc-utils >= 0.3.2
BuildRequires: glib2-devel >= 2.7.3
BuildRequires: gtk2-devel >= 2.6.0
BuildRequires: libglade2-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: libnotify-devel >= 0.4.1
BuildRequires: scrollkeeper
BuildRequires: which
BuildRequires: gettext
BuildRequires: intltool
# for /usr/share/gnome/help, we should require yelp
# but we don't to avoid forcing firefox and libbeagle on live cds
# via anaconda -> zenity -> ...
#Requires: yelp

Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
Zenity lets you display Gtk+ dialog boxes from the command line and through
shell scripts. It is similar to gdialog, but is intended to be saner. It comes
from the same family as dialog, Xdialog, and cdialog.

%prep
%setup -q

intltoolize --force

%build
%configure --disable-scrollkeeper
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# we don't want a perl dependency just for this
rm $RPM_BUILD_ROOT%{_bindir}/gdialog

# save space by linking identical images in translated docs
helpdir=$RPM_BUILD_ROOT%{_datadir}/gnome/help/%{name}
for f in $helpdir/C/figures/*.png; do
  b="$(basename $f)"
  for d in $helpdir/*; do
    if [ -d "$d" -a "$d" != "$helpdir/C" ]; then
      g="$d/figures/$b"
      if [ -f "$g" ]; then
        if cmp -s $f $g; then
          rm "$g"; ln -s "../../C/figures/$b" "$g"
        fi
      fi
    fi
  done
done


%find_lang zenity --with-gnome


%clean
rm -rf $RPM_BUILD_ROOT


%post
scrollkeeper-update -q || :


%postun
scrollkeeper-update -q || :


%files -f zenity.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS THANKS README
%{_bindir}/zenity
%{_datadir}/zenity
%{_mandir}/man1/zenity.1.gz


%changelog
* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Tue Aug 11 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.90-1
- Update to 2.27.90

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update 2.26.0

* Thu Mar 12 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct  9 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-2
- Save some space

* Tue Sep 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Wed Jun 18 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.3.1-1
- Update to 2.23.3.1

* Tue Jun  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.2-1
- Update to 2.23.2

* Fri Apr 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Mon Feb 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.1-1
- Update to 2.21.1

* Sat Feb  9 2008 Matthias Clasen <mclasen@redhat.com> - 2.20.1-3
- Rebuild for gcc 4.3

* Sun Jan 20 2008 Matthias Clasen <mclasen@redhat.com> - 2.20.1-2
- Rebuild to fix upgrade path

* Tue Nov 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-1
- Update to 2.20.1 (translation updates)

* Mon Oct 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-3
- Rebuild against new dbus-glib

* Tue Sep 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-2
- Drop yelp dependency to avoid exploding live cds (#295091)

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Thu Aug 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-2
- Drop gdialog and the perl dependency

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-1
- Update to 2.19.2

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.1-4
- Use %%find_lang for help files

* Wed Aug  1 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.1-2
- Incorporate package review feedback

* Sat May 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.1-1
- Update to 2.19.1

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.92-1
- Update to 2.17.92

* Mon Feb 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.91-1
- Update to 2.17.91

* Mon Jan 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-1
- Update to 2.17.90

* Wed Jan 10 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.3-1
- Update to 2.17.3

* Tue Dec 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.2-1
- Update to 2.17.2

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-1
- Update to 2.17.1

* Mon Dec  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-2
- Add a BuildRequires for libnotify-devel

* Sun Oct 22 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0
- Add missing BRs

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-1.fc6
- Update to 2.15.92

* Sat Aug 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-1.fc6
- Update to 2.15.91

* Thu Aug  3 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.90-1.fc6
- Update to 2.15.90

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.15.2-4
- rebuild

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> 2.15.2-3
- Add missing BuildRequires

* Mon Jun  5 2006 Matthias Clasen <mclasen@redhat.com> 2.15.2-2
- Rebuild

* Tue May 16 2006 Matthias Clasen <mclasen@redhat.com> 2.15.2-1
- Update to 2.15.2
- Remove po/LINGUAS fixes

* Tue May  9 2006 Matthias Clasen <mclasen@redhat.com> 2.15.1-1
- Update to 2.15.1

* Tue Apr 18 2006 Matthias Clasen <mclasen@redhat.com> 2.14.1-4
- More package review feedback

* Mon Apr 17 2006 Matthias Clasen <mclasen@redhat.com> 2.14.1-3
- Incorporate package review feedback

* Tue Apr 11 2006 Matthias Clasen <mclasen@redhat.com> 2.14.1-2
- Initial revision

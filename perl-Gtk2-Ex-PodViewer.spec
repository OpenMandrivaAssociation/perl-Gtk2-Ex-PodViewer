%define	upstream_name	 Gtk2-Ex-PodViewer
%define	upstream_version 0.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A Gtk2 widget for displaying Plain old Documentation (POD)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Gtk2/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Glib) => 1.00
BuildRequires:	perl(Gtk2)
BuildRequires:	perl(ExtUtils::PkgConfig) 
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(IO::Stringy)
BuildRequires:	perl(Pod::Simple)
BuildRequires:	perl(Locale::gettext)
BuildRequires:  perl(Pod::Parser)
BuildArch:	noarch

Requires:	perl(Glib) >= 1.00
Provides:	perl-Gtk2-PodViewer = %{version}
Provides:	perl(Gtk2::PodViewer) = %{version}

%description
Gtk2::PodViewer is a widget for rendering Perl POD documents. It is based on
the Gtk2::TextView widget and uses Pod::Parser for manipulating POD data.

podviewer uses it in order to render POD documentation

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 
chmod 644 README

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc README
%{_bindir}/podviewer
%{_mandir}/*/*
%{perl_vendorlib}/Gtk2


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 403228
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2009.1
+ Revision: 292165
- update to new version 0.18

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.17-4mdv2009.0
+ Revision: 241443
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jun 26 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.17-2mdv2008.0
+ Revision: 44601
- rebuild


* Thu Sep 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2007.0
- new version

* Mon Jul 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2007.0
- New version 0.16

* Wed May 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdk
- New release 0.15
- drop patch (merged upstream)
- better source URL
- better buildrequires syntax

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-3mdk
- fix makefile

* Thu Dec 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-2mdk
- fix buildrequires

* Thu Nov 24 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdk
- New release 0.14

* Wed Oct 12 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdk
- name change
- new version
- spec cleanup
- rpmbuildupdate aware
- fix url
- fix group
- fix directory ownership
- noarch
- drop libgconf-devel build dependency

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-4mdk
- fix buildrequires

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.07-3mdk
- rebuild for new perl

* Fri Aug 13 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.07-2mdk
- rebuild for perl-5.8.5

* Wed Jun 02 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.07-1mdk
- 0.07
- cosmetics
- fix typo in spec file name

* Fri Apr 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.06-1mdk
- inital release


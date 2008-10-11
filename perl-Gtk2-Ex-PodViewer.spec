%define	module	Gtk2-Ex-PodViewer
%define	name	perl-%{module}
%define	version	0.18
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A Gtk2 widget for displaying Plain old Documentation (POD)
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/Gtk2/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Glib) => 1.00
BuildRequires:	perl(Gtk2)
BuildRequires:	perl(ExtUtils::PkgConfig) 
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:  perl(IO::Stringy)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Locale::gettext)
Requires:	perl(Glib) >= 1.00
Conflicts:	drakxtools < 9.1-15mdk
Obsoletes:	perl-Gtk2-PodViewer
Provides:	perl-Gtk2-PodViewer
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Gtk2::PodViewer is a widget for rendering Perl POD documents. It is based on
the Gtk2::TextView widget and uses Pod::Parser for manipulating POD data.

podviewer uses it in order to render POD documentation

%prep
%setup -q -n %{module}-%{version}
find -type d -name CVS | rm -rf 
chmod 644 README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/podviewer
%{_mandir}/*/*
%{perl_vendorlib}/Gtk2


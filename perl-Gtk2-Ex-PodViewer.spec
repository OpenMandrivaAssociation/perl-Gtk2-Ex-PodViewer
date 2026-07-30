%define	upstream_name	 Gtk2-Ex-PodViewer
%define upstream_version 0.18
Name:		perl-%{upstream_name}
Version:	0.18
Release:	1

Summary:	A Gtk2 widget for displaying Plain old Documentation (POD)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        https://metacpan.org/dist/%{upstream_name}/
Source0:	https://cpan.metacpan.org/authors/id/G/GB/GBROWN/Gtk2-Ex-PodViewer-0.18.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}
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



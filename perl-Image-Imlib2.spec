%include	/usr/lib/rpm/macros.perl
%define		pdir	Image
%define		pnam	Imlib2
Summary:	Interface to the Imlib2 image library
Name:		perl-Image-Imlib2
Version:	1.01
Release:	0.9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	506ddc41150c93da005e96ad987daee7
BuildRequires:	imlib2-devel
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Module-Build
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image::Imlib2 is a Perl port of Imlib2, a graphics library that does
image file loading and saving as well as manipulation, arbitrary
polygon support, etc. It does ALL of these operations FAST. It allows
you to create colour images using a large number of graphics
primitives, and output the images in a range of formats.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	destdir=$RPM_BUILD_ROOT
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README examples
%{perl_sitearch}/Image/Imlib2.pm
%{_mandir}/man[13]/*

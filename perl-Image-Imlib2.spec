#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Image
%define		pnam	Imlib2
Summary:	Interface to the Imlib2 image library
Summary(pl.UTF-8):	Interfejs do biblioteki obrazów Imlib2
Name:		perl-Image-Imlib2
Version:	2.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Image/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	303b91fae2b863903e41a3cac34fa0d3
URL:		http://search.cpan.org/dist/Image-Imlib2/
BuildRequires:	imlib2-devel
BuildRequires:	perl-Module-Build >= 0.20
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image::Imlib2 is a Perl port of Imlib2, a graphics library that does
image file loading and saving as well as manipulation, arbitrary
polygon support, etc. It does ALL of these operations FAST. It allows
you to create colour images using a large number of graphics
primitives, and output the images in a range of formats.

%description -l pl.UTF-8
Image::Imlib2 to perlowy port Imlib2 - biblioteki graficznej
wczytującej, zapisującej i przetwarzającej obrazy z obsługą dowolnych
wielokątów itp. Wykonuje WSZYSTKIE te operacje SZYBKO. Pozwala na
tworzenie kolorowych obrazów przy użyciu dużej liczby prymitywów
graficznych i zapis ich w wielu formatach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	destdir=$RPM_BUILD_ROOT
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd examples
for f in * ; do
	sed -e "s@#!/usr/local/bin/perl@#!/usr/bin/perl@" $f \
		> $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorarch}/Image/Imlib2.pm
%dir %{perl_vendorarch}/auto/Image/Imlib2
%{perl_vendorarch}/auto/Image/Imlib2/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Image/Imlib2/*.so
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*.txt
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/Image::Imlib2*.3pm*

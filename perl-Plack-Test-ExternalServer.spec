#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Plack
%define		pnam	Test-ExternalServer
%include	/usr/lib/rpm/macros.perl
Summary:	Plack::Test::ExternalServer - Run HTTP tests on external live servers
Name:		perl-Plack-Test-ExternalServer
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Plack/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb0806b4e5bc61064e3736991dd8640c
URL:		http://search.cpan.org/dist/Plack-Test-ExternalServer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTTP-Message
BuildRequires:	perl-Plack
BuildRequires:	perl-Test-TCP
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows your to run your Plack::Test tests against an
external server instead of just against a local application through
either mocked HTTP or a locally spawned server.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Plack/Test/*.pm
%{_mandir}/man3/*

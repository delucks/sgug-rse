Name:           perl-HTTP-CookieJar
Version:        0.008
Release:        13%{?dist}
Summary:        Minimalist HTTP user agent cookie jar
License:        ASL 2.0
URL:            https://metacpan.org/release/HTTP-CookieJar
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/HTTP-CookieJar-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter >= 5.8.1
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mozilla::PublicSuffix)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(strict), perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module implements a minimalist HTTP user agent cookie jar in
conformance with RFC 6265.

%prep
%setup -q -n HTTP-CookieJar-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CONTRIBUTING.mkdn LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-9
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 14 2016 Yanko Kaneti <yaneti@declera.com> 0.008-4
- Drop version requirements for perl(Time::Local) BR due to
  perl-Time-Local version going backwards recently

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov  9 2015 Yanko Kaneti <yaneti@declera.com> 0.008-1
- Update to 0.008. Upstream dropped minimal perl requirement to 5.8.1

* Thu Sep 24 2015 Yanko Kaneti <yaneti@declera.com> 0.007-1
- Update to 0.007. Upstream droppped the Time::Mock builddep

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-3
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-2
- Perl 5.20 rebuild

* Tue Jul 15 2014 Yanko Kaneti <yaneti@declera.com> 0.006-1
- Update to 0.006

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 26 2013 Yanko Kaneti <yaneti@declera.com> 0.005-1
- Update to 0.005

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.004-3
- Perl 5.18 rebuild

* Fri May 17 2013 Yanko Kaneti <yaneti@declera.com> 0.004-2
- Address review comments. (#963213#c1)

* Tue May 14 2013 Yanko Kaneti <yaneti@declera.com> 0.004-1
- Specfile autogenerated by cpanspec 1.78 and tweaked for submission

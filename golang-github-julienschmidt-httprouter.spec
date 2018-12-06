%bcond_without check
%global goipath github.com/julienschmidt/httprouter
%global commit  adbc77eec0d91467376ca515bc3a14b8434d0f18

%global common_description %{expand:
A high performance HTTP request router that scales well}

%gometa

Name:           %{goname}
Version:        1.1
Release:        14%{?dist}
Summary:        A high performance HTTP request router that scales well
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{common_description}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%if %{with check}
  %gochecks
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14.gitadbc77e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1-13.gitadbc77e
- Upload glide files

* Fri Jun 01 2018 Paul Gier <pgier@redhat.com> - 1.1-12
- Update to latest snapshot
- Minor updates to latest go packaging standards

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1-11
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.1-9
- Polish the spec file
  related: #1262566

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 1.1-2
- Update to spec-2.1
  resolves: #1262566

* Thu Aug 27 2015 jchaloup <jchaloup@redhat.com> - 1.1-1
- First package for Fedora
  resolves: #1257619


#
# Conditional build:
%bcond_with	javadoc		# build javadoc (doesn't build on builders)
#
%include	/usr/lib/rpm/macros.java
Summary:	Easy to use and powerful layout manager for Java
Summary(pl.UTF-8):	Łatwy w użyciu i potężny zarządca układów graficznych dla Javy
Name:		higlayout
Version:	1.0
Release:	4
License:	LGPL
Group:		Libraries
Source0:	http://www.autel.cz/dmi/HIGLayout%{version}.zip
# Source0-md5:	5bd79f33157824499b0fc03d6a5e080a
URL:		http://www.autel.cz/dmi/tutorial.html
BuildRequires:	jdk
BuildRequires:	rpm-javaprov
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	jpackage-utils
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy to use and powerful layout manager for Java.

%description -l pl.UTF-8
Łatwy w użyciu i potężny zarządca układów graficznych dla Javy.

%package javadoc
Summary:	Java API documentation for higlayout
Summary(pl.UTF-8):	Dokumentacja Java API dla higlayout
Group:		Documentation

%description javadoc
Java API documentation for higlayout.

%description javadoc -l pl.UTF-8
Dokumentacja Java API dla higlayout.

%package demo
Summary:	Demo for %{name}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{name}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{name}.

%prep
%setup -q -c
mv src/cz .
sed -i -e 's/\r//g' examples/*.java tutorial/*.html *.txt
rm -rf apidoc; mkdir apidoc

%build
%if %{with javadoc}
CLASSPATH=. %javadoc -link %{_javadocdir}/java -d apidoc cz.autel.dmi
%endif
%javac -source 1.4 cz/autel/dmi/*.java
%jar cf %{name}.jar cz/autel/dmi/*.class

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# install jar
cp -a %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# examples / tutorial
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples tutorial $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a apidoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc Changes.txt readme.txt
%{_javadir}/%{name}*.jar

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif

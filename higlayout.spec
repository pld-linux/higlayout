Summary:	Easy to use and powerful layout manager for Java
Summary(pl.UTF-8):   Łatwy w użyciu i potężny zarządca układów graficznych dla Javy
Name:		higlayout
Version:	1.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.autel.cz/dmi/HIGLayout%{version}.zip
# Source0-md5:	5bd79f33157824499b0fc03d6a5e080a
URL:		http://www.autel.cz/dmi/tutorial.html
BuildRequires:	java-sun
BuildRequires:	sed >= 4.0
Requires:	jre >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy to use and powerful layout manager for Java.

%description -l pl.UTF-8
Łatwy w użyciu i potężny zarządca układów graficznych dla Javy.

%package javadoc
Summary:	Java API documentation for higlayout
Summary(pl.UTF-8):   Dokumentacja Java API dla higlayout
Group:		Documentation

%description javadoc
Java API documentation for higlayout.

%description javadoc -l pl.UTF-8
Dokumentacja Java API dla higlayout.

%prep
%setup -q -c
mv src/cz .
sed -i -e 's/\r//g' examples/*.java tutorial/*.html *.txt
rm -rf apidoc ; mkdir apidoc

%build
javac -source 1.4 cz/autel/dmi/*.java
jar cf %{name}.jar cz/autel/dmi/*.class
javadoc -link %{_javadocdir}/java -d apidoc cz.autel.dmi

%install
rm -rf $RPM_BUILD_ROOT

install -Dpm 644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pR apidoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.txt LGPLicense.txt readme.txt examples/ tutorial/
%{_javadir}/%{name}*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}

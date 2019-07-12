#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-zookeeper
Version  : 3.4.6
Release  : 1
URL      : https://repo1.maven.org/maven2/org/apache/zookeeper/zookeeper/3.4.6/zookeeper-3.4.6.jar
Source0  : https://repo1.maven.org/maven2/org/apache/zookeeper/zookeeper/3.4.6/zookeeper-3.4.6.jar
Source1  : https://repo1.maven.org/maven2/org/apache/zookeeper/zookeeper/3.4.13/zookeeper-3.4.13.jar
Source2  : https://repo1.maven.org/maven2/org/apache/zookeeper/zookeeper/3.4.13/zookeeper-3.4.13.pom
Source3  : https://repo1.maven.org/maven2/org/apache/zookeeper/zookeeper/3.4.6/zookeeper-3.4.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-zookeeper-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-zookeeper package.
Group: Data

%description data
data components for the mvn-zookeeper package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.6
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.13
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.13

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.13
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.13

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.6


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.13/zookeeper-3.4.13.jar
/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.13/zookeeper-3.4.13.pom
/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.6/zookeeper-3.4.6.jar
/usr/share/java/.m2/repository/org/apache/zookeeper/zookeeper/3.4.6/zookeeper-3.4.6.pom

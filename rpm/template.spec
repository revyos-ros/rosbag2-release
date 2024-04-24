%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-rosbag2-examples-py
Version:        0.26.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rosbag2_examples_py package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-example-interfaces
Requires:       ros-jazzy-rclpy
Requires:       ros-jazzy-rosbag2-py
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-jazzy-example-interfaces
BuildRequires:  ros-jazzy-rclpy
BuildRequires:  ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-rosbag2-py
BuildRequires:  ros-jazzy-std-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-jazzy-ament-copyright
BuildRequires:  ros-jazzy-ament-flake8
BuildRequires:  ros-jazzy-ament-pep257
%endif

%description
Python bag writing tutorial

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/jazzy"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Wed Apr 24 2024 geoff <gbiggs@killbots.net> - 0.26.2-1
- Autogenerated by Bloom

* Fri Apr 19 2024 geoff <gbiggs@killbots.net> - 0.26.1-2
- Autogenerated by Bloom

* Wed Apr 17 2024 geoff <gbiggs@killbots.net> - 0.26.1-1
- Autogenerated by Bloom

* Tue Apr 16 2024 geoff <gbiggs@killbots.net> - 0.26.0-1
- Autogenerated by Bloom

* Thu Mar 28 2024 geoff <gbiggs@killbots.net> - 0.25.0-1
- Autogenerated by Bloom

* Mon Mar 11 2024 geoff <gbiggs@killbots.net> - 0.24.0-3
- Autogenerated by Bloom

* Wed Mar 06 2024 geoff <gbiggs@killbots.net> - 0.24.0-2
- Autogenerated by Bloom


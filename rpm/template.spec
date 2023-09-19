%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-rosbag2-storage-mcap
Version:        0.15.8
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rosbag2_storage_mcap package

License:        Apache-2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-ament-index-cpp
Requires:       ros-humble-mcap-vendor
Requires:       ros-humble-pluginlib
Requires:       ros-humble-rcutils
Requires:       ros-humble-rosbag2-storage
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ament-index-cpp
BuildRequires:  ros-humble-mcap-vendor
BuildRequires:  ros-humble-pluginlib
BuildRequires:  ros-humble-rcutils
BuildRequires:  ros-humble-rosbag2-storage
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-clang-format
BuildRequires:  ros-humble-ament-cmake-gmock
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
BuildRequires:  ros-humble-rcpputils
BuildRequires:  ros-humble-rosbag2-storage-mcap-testdata
BuildRequires:  ros-humble-rosbag2-test-common
BuildRequires:  ros-humble-std-msgs
%endif

%description
rosbag2 storage plugin using the MCAP file format

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Sep 19 2023 Foxglove <ros-tooling@foxglove.dev> - 0.15.8-1
- Autogenerated by Bloom

* Tue Jul 18 2023 Foxglove <ros-tooling@foxglove.dev> - 0.15.7-1
- Autogenerated by Bloom

* Tue Jun 06 2023 Foxglove <ros-tooling@foxglove.dev> - 0.15.6-1
- Autogenerated by Bloom

* Thu Apr 27 2023 Foxglove <ros-tooling@foxglove.dev> - 0.15.5-1
- Autogenerated by Bloom

* Wed Jan 11 2023 Foxglove <ros-tooling@foxglove.dev> - 0.15.4-2
- Autogenerated by Bloom

* Tue Jan 10 2023 Foxglove <ros-tooling@foxglove.dev> - 0.15.4-1
- Autogenerated by Bloom


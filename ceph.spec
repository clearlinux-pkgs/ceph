#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ceph
Version  : 11.2.0
Release  : 46
URL      : https://download.ceph.com/tarballs/ceph_11.2.0.orig.tar.gz
Source0  : https://download.ceph.com/tarballs/ceph_11.2.0.orig.tar.gz
Source1  : ceph.tmpfiles
Summary  : Ceph Base Package
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause BSL-1.0 CC-BY-SA-1.0 GPL-2.0 GPL-2.0-with-autoconf-exception LGPL-2.0 LGPL-2.1 MIT MTLL NTP
Requires: ceph-bin
Requires: ceph-legacypython
Requires: ceph-python3
Requires: ceph-config
Requires: ceph-lib
Requires: ceph-data
Requires: ceph-doc
Requires: ceph-python
Requires: pecan
Requires: requests
Requires: setuptools
BuildRequires : Cython
BuildRequires : Sphinx-python
BuildRequires : boost-dev
BuildRequires : bzip2-dev
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : expat-dev
BuildRequires : fcgi-dev
BuildRequires : googletest-dev
BuildRequires : gperftools-dev
BuildRequires : imagesize
BuildRequires : isa-l-dev
BuildRequires : keyutils-dev
BuildRequires : leveldb-dev
BuildRequires : libaio-dev
BuildRequires : libatomic_ops-dev
BuildRequires : lz4-dev
BuildRequires : openldap-dev
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pecan
BuildRequires : pip
BuildRequires : pkgconfig(nss)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : requests
BuildRequires : scons
BuildRequires : sed
BuildRequires : setuptools
BuildRequires : snappy-dev
BuildRequires : systemd-dev
BuildRequires : tox
BuildRequires : tox-python
BuildRequires : util-linux-dev
BuildRequires : valgrind
BuildRequires : valgrind-dev
BuildRequires : virtualenv
BuildRequires : xfsprogs-dev
BuildRequires : yasm
BuildRequires : zlib-dev
Patch1: 0001-Ceph-sudoers-entry.patch
Patch2: 0002-detect-clearlinux-init-system.patch
Patch3: 0003-Call-ceph-osd-prestart.sh-from-libexec-dir.patch
Patch4: 0004-systemd.patch
Patch5: 0005-bash-completion.patch
Patch6: 0006-os-release.patch
Patch7: 0007-rocksdb-gcc7-fix.patch
Patch8: 0008-Remove-Werror.patch

%description
Ceph is a massively scalable, open-source, distributed storage system that runs
on commodity hardware and delivers object, block and file system storage.

%package bin
Summary: bin components for the ceph package.
Group: Binaries
Requires: ceph-data
Requires: ceph-config

%description bin
bin components for the ceph package.


%package config
Summary: config components for the ceph package.
Group: Default

%description config
config components for the ceph package.


%package data
Summary: data components for the ceph package.
Group: Data

%description data
data components for the ceph package.


%package dev
Summary: dev components for the ceph package.
Group: Development
Requires: ceph-lib
Requires: ceph-bin
Requires: ceph-data
Provides: ceph-devel

%description dev
dev components for the ceph package.


%package doc
Summary: doc components for the ceph package.
Group: Documentation

%description doc
doc components for the ceph package.


%package legacypython
Summary: legacypython components for the ceph package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the ceph package.


%package lib
Summary: lib components for the ceph package.
Group: Libraries
Requires: ceph-data

%description lib
lib components for the ceph package.


%package python
Summary: python components for the ceph package.
Group: Default
Requires: ceph-legacypython
Requires: ceph-python3

%description python
python components for the ceph package.


%package python3
Summary: python3 components for the ceph package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ceph package.


%prep
%setup -q -n ceph-11.2.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509057483
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DWITH_LTTNG=OFF -DWITH_FUSE=OFF -DWITH_SYSTEMD=ON -DWITH_MGR=OFF -DWITH_PYTHON3=ON -DWITH_TESTS=OFF -DHAVE_BABELTRACE=OFF -DCMAKE_MODULE_PATH="/usr/share/cmake/Modules:/usr/share/cmake-3.8/Modules"
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1509057483
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/ceph.conf
## make_install_append content
install -d -m 750 %{buildroot}/usr/share/defaults/sudo/sudoers.d
install -p -D -m 440 ceph.sudoers %{buildroot}/usr/share/defaults/sudo/sudoers.d/ceph
install -d -m 755 %{buildroot}/usr/lib/udev/rules.d
install -p -D -m 644 udev/50-rbd.rules %{buildroot}/usr/lib/udev/rules.d
install -p -D -m 644 udev/60-ceph-by-parttypeuuid.rules %{buildroot}/usr/lib/udev/rules.d
install -p -D -m 644 udev/95-ceph-osd.rules %{buildroot}/usr/lib/udev/rules.d
rm -rf %{buildroot}/usr/etc
rm -rf %{buildroot}/usr/lib/systemd/system/ceph-fuse*
rm -rf %{buildroot}/usr/lib/systemd/system/ceph-mgr*
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ceph
/usr/bin/ceph-authtool
/usr/bin/ceph-bluefs-tool
/usr/bin/ceph-brag
/usr/bin/ceph-clsinfo
/usr/bin/ceph-conf
/usr/bin/ceph-create-keys
/usr/bin/ceph-crush-location
/usr/bin/ceph-dencoder
/usr/bin/ceph-detect-init
/usr/bin/ceph-disk
/usr/bin/ceph-disk-udev
/usr/bin/ceph-mds
/usr/bin/ceph-mon
/usr/bin/ceph-objectstore-tool
/usr/bin/ceph-osd
/usr/bin/ceph-post-file
/usr/bin/ceph-rbdnamer
/usr/bin/ceph-rest-api
/usr/bin/ceph-run
/usr/bin/ceph-syn
/usr/bin/cephfs-data-scan
/usr/bin/cephfs-journal-tool
/usr/bin/cephfs-table-tool
/usr/bin/crushtool
/usr/bin/librados-config
/usr/bin/monmaptool
/usr/bin/mount.ceph
/usr/bin/osdmaptool
/usr/bin/rados
/usr/bin/radosgw
/usr/bin/radosgw-admin
/usr/bin/radosgw-object-expirer
/usr/bin/radosgw-token
/usr/bin/rbd
/usr/bin/rbd-mirror
/usr/bin/rbd-nbd
/usr/bin/rbd-replay
/usr/bin/rbd-replay-many
/usr/bin/rbdmap
/usr/libexec/ceph/ceph-osd-prestart.sh
/usr/libexec/ceph/ceph_common.sh

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/ceph-disk@.service
/usr/lib/systemd/system/ceph-mds.target
/usr/lib/systemd/system/ceph-mds@.service
/usr/lib/systemd/system/ceph-mon.target
/usr/lib/systemd/system/ceph-mon@.service
/usr/lib/systemd/system/ceph-osd.target
/usr/lib/systemd/system/ceph-osd@.service
/usr/lib/systemd/system/ceph-radosgw.target
/usr/lib/systemd/system/ceph-radosgw@.service
/usr/lib/systemd/system/ceph-rbd-mirror.target
/usr/lib/systemd/system/ceph-rbd-mirror@.service
/usr/lib/systemd/system/ceph.target
/usr/lib/systemd/system/rbdmap.service
/usr/lib/tmpfiles.d/ceph.conf
/usr/lib/udev/rules.d/50-rbd.rules
/usr/lib/udev/rules.d/60-ceph-by-parttypeuuid.rules
/usr/lib/udev/rules.d/95-ceph-osd.rules

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/ceph
/usr/share/bash-completion/completions/rados
/usr/share/bash-completion/completions/radosgw-admin
/usr/share/bash-completion/completions/rbd
/usr/share/ceph/id_rsa_drop.ceph.com
/usr/share/ceph/id_rsa_drop.ceph.com.pub
/usr/share/ceph/known_hosts_drop.ceph.com
/usr/share/defaults/sudo/sudoers.d/ceph

%files dev
%defattr(-,root,root,-)
/usr/include/cephfs/ceph_statx.h
/usr/include/cephfs/libcephfs.h
/usr/include/rados/buffer.h
/usr/include/rados/buffer_fwd.h
/usr/include/rados/crc32c.h
/usr/include/rados/inline_memory.h
/usr/include/rados/librados.h
/usr/include/rados/librados.hpp
/usr/include/rados/librgw.h
/usr/include/rados/memory.h
/usr/include/rados/page.h
/usr/include/rados/rados_types.h
/usr/include/rados/rados_types.hpp
/usr/include/rados/rgw_file.h
/usr/include/radosstriper/libradosstriper.h
/usr/include/radosstriper/libradosstriper.hpp
/usr/include/rbd/features.h
/usr/include/rbd/librbd.h
/usr/include/rbd/librbd.hpp
/usr/lib64/libcephfs.so
/usr/lib64/librados.so
/usr/lib64/libradosstriper.so
/usr/lib64/librbd.so
/usr/lib64/librgw.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/ceph/*
%doc /usr/share/man/man8/*

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/ceph/compressor/libceph_snappy.so
/usr/lib64/ceph/compressor/libceph_snappy.so.2
/usr/lib64/ceph/compressor/libceph_snappy.so.2.0.0
/usr/lib64/ceph/compressor/libceph_zlib.so
/usr/lib64/ceph/compressor/libceph_zlib.so.2
/usr/lib64/ceph/compressor/libceph_zlib.so.2.0.0
/usr/lib64/ceph/erasure-code/libec_isa.so
/usr/lib64/ceph/erasure-code/libec_isa.so.2
/usr/lib64/ceph/erasure-code/libec_isa.so.2.14.0
/usr/lib64/ceph/erasure-code/libec_jerasure.so
/usr/lib64/ceph/erasure-code/libec_jerasure_generic.so
/usr/lib64/ceph/erasure-code/libec_jerasure_sse3.so
/usr/lib64/ceph/erasure-code/libec_jerasure_sse4.so
/usr/lib64/ceph/erasure-code/libec_lrc.so
/usr/lib64/ceph/erasure-code/libec_shec.so
/usr/lib64/ceph/erasure-code/libec_shec_generic.so
/usr/lib64/ceph/erasure-code/libec_shec_sse3.so
/usr/lib64/ceph/erasure-code/libec_shec_sse4.so
/usr/lib64/libcephfs.so.2
/usr/lib64/libcephfs.so.2.0.0
/usr/lib64/librados.so.2
/usr/lib64/librados.so.2.0.0
/usr/lib64/libradosstriper.so.1
/usr/lib64/libradosstriper.so.1.0.0
/usr/lib64/librbd.so.1
/usr/lib64/librbd.so.1.0.0
/usr/lib64/librgw.so.2
/usr/lib64/librgw.so.2.0.0
/usr/lib64/rados-classes/libcls_cephfs.so
/usr/lib64/rados-classes/libcls_cephfs.so.1
/usr/lib64/rados-classes/libcls_cephfs.so.1.0.0
/usr/lib64/rados-classes/libcls_hello.so
/usr/lib64/rados-classes/libcls_hello.so.1
/usr/lib64/rados-classes/libcls_hello.so.1.0.0
/usr/lib64/rados-classes/libcls_journal.so
/usr/lib64/rados-classes/libcls_journal.so.1
/usr/lib64/rados-classes/libcls_journal.so.1.0.0
/usr/lib64/rados-classes/libcls_kvs.so
/usr/lib64/rados-classes/libcls_kvs.so.1
/usr/lib64/rados-classes/libcls_kvs.so.1.0.0
/usr/lib64/rados-classes/libcls_lock.so
/usr/lib64/rados-classes/libcls_lock.so.1
/usr/lib64/rados-classes/libcls_lock.so.1.0.0
/usr/lib64/rados-classes/libcls_log.so
/usr/lib64/rados-classes/libcls_log.so.1
/usr/lib64/rados-classes/libcls_log.so.1.0.0
/usr/lib64/rados-classes/libcls_lua.so
/usr/lib64/rados-classes/libcls_lua.so.1
/usr/lib64/rados-classes/libcls_lua.so.1.0.0
/usr/lib64/rados-classes/libcls_numops.so
/usr/lib64/rados-classes/libcls_numops.so.1
/usr/lib64/rados-classes/libcls_numops.so.1.0.0
/usr/lib64/rados-classes/libcls_rbd.so
/usr/lib64/rados-classes/libcls_rbd.so.1
/usr/lib64/rados-classes/libcls_rbd.so.1.0.0
/usr/lib64/rados-classes/libcls_refcount.so
/usr/lib64/rados-classes/libcls_refcount.so.1
/usr/lib64/rados-classes/libcls_refcount.so.1.0.0
/usr/lib64/rados-classes/libcls_replica_log.so
/usr/lib64/rados-classes/libcls_replica_log.so.1
/usr/lib64/rados-classes/libcls_replica_log.so.1.0.0
/usr/lib64/rados-classes/libcls_rgw.so
/usr/lib64/rados-classes/libcls_rgw.so.1
/usr/lib64/rados-classes/libcls_rgw.so.1.0.0
/usr/lib64/rados-classes/libcls_statelog.so
/usr/lib64/rados-classes/libcls_statelog.so.1
/usr/lib64/rados-classes/libcls_statelog.so.1.0.0
/usr/lib64/rados-classes/libcls_timeindex.so
/usr/lib64/rados-classes/libcls_timeindex.so.1
/usr/lib64/rados-classes/libcls_timeindex.so.1.0.0
/usr/lib64/rados-classes/libcls_user.so
/usr/lib64/rados-classes/libcls_user.so.1
/usr/lib64/rados-classes/libcls_user.so.1.0.0
/usr/lib64/rados-classes/libcls_version.so
/usr/lib64/rados-classes/libcls_version.so.1
/usr/lib64/rados-classes/libcls_version.so.1.0.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

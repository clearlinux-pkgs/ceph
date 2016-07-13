#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ceph
Version  : 10.2.2
Release  : 18
URL      : http://ceph.com/download/ceph-10.2.2.tar.gz
Source0  : http://ceph.com/download/ceph-10.2.2.tar.gz
Source1  : ceph.tmpfiles
Summary  : Ceph Base Package
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 CC-BY-SA-1.0 GPL-2.0 GPL-2.0-with-autoconf-exception LGPL-2.0 LGPL-2.1 MIT
Requires: ceph-bin
Requires: ceph-python
Requires: ceph-config
Requires: ceph-lib
Requires: ceph-data
Requires: ceph-doc
BuildRequires : Sphinx-python
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : boost-dev
BuildRequires : bzip2-dev
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : expat-dev
BuildRequires : fcgi-dev
BuildRequires : gettext-bin
BuildRequires : googletest-dev
BuildRequires : gperftools-dev
BuildRequires : imagesize
BuildRequires : isa-l-dev
BuildRequires : keyutils-dev
BuildRequires : leveldb-dev
BuildRequires : libaio-dev
BuildRequires : libatomic_ops-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : lz4-dev
BuildRequires : m4
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : python-dev
BuildRequires : python3-dev
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
Patch2: 0002-Do-not-parse-lsb_release.patch
Patch3: 0001-detect-clearlinux-init-system.patch
Patch4: 0001-use-uname-instead-of-arch.patch
Patch5: 0001-Call-ceph-osd-prestart.sh-from-libexec-dir.patch

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


%package lib
Summary: lib components for the ceph package.
Group: Libraries
Requires: ceph-data
Requires: ceph-config

%description lib
lib components for the ceph package.


%package python
Summary: python components for the ceph package.
Group: Default

%description python
python components for the ceph package.


%prep
%setup -q -n ceph-10.2.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export LANG=C
%reconfigure --disable-static --with-nss \
--without-cryptopp \
--without-librocksdb \
--without-cython \
--without-openldap
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/ceph.conf
## make_install_append content
install -d -m 750 %{buildroot}/usr/share/defaults/sudo/sudoers.d
install -p -D -m 440 ceph.sudoers %{buildroot}/usr/share/defaults/sudo/sudoers.d/ceph
install -d -m 755 %{buildroot}/usr/lib/udev/rules.d
install -p -D -m 644 udev/50-rbd.rules %{buildroot}/usr/lib/udev/rules.d
install -p -D -m 644 udev/95-ceph-osd.rules %{buildroot}/usr/lib/udev/rules.d
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/ceph/ceph-monstore-update-crush.sh

%files bin
%defattr(-,root,root,-)
/usr/bin/ceph
/usr/bin/ceph-authtool
/usr/bin/ceph-bluefs-tool
/usr/bin/ceph-brag
/usr/bin/ceph-clsinfo
/usr/bin/ceph-conf
/usr/bin/ceph-coverage
/usr/bin/ceph-create-keys
/usr/bin/ceph-crush-location
/usr/bin/ceph-debugpack
/usr/bin/ceph-dencoder
/usr/bin/ceph-detect-init
/usr/bin/ceph-disk
/usr/bin/ceph-disk-udev
/usr/bin/ceph-fuse
/usr/bin/ceph-mds
/usr/bin/ceph-mon
/usr/bin/ceph-objectstore-tool
/usr/bin/ceph-osd
/usr/bin/ceph-post-file
/usr/bin/ceph-rbdnamer
/usr/bin/ceph-rest-api
/usr/bin/ceph-run
/usr/bin/ceph-syn
/usr/bin/cephfs
/usr/bin/cephfs-data-scan
/usr/bin/cephfs-journal-tool
/usr/bin/cephfs-table-tool
/usr/bin/crushtool
/usr/bin/librados-config
/usr/bin/monmaptool
/usr/bin/mount.ceph
/usr/bin/mount.fuse.ceph
/usr/bin/osdmaptool
/usr/bin/rados
/usr/bin/radosgw
/usr/bin/radosgw-admin
/usr/bin/radosgw-object-expirer
/usr/bin/radosgw-token
/usr/bin/rbd
/usr/bin/rbd-fuse
/usr/bin/rbd-mirror
/usr/bin/rbd-nbd
/usr/bin/rbd-replay
/usr/bin/rbd-replay-many
/usr/bin/rbdmap
/usr/libexec/ceph/ceph-osd-prestart.sh
/usr/libexec/ceph/ceph_common.sh

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/ceph-create-keys@.service
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
/usr/lib/udev/rules.d/95-ceph-osd.rules

%files data
%defattr(-,root,root,-)
/usr/share/ceph/id_dsa_drop.ceph.com
/usr/share/ceph/id_dsa_drop.ceph.com.pub
/usr/share/ceph/known_hosts_drop.ceph.com
/usr/share/defaults/sudo/sudoers.d/ceph

%files dev
%defattr(-,root,root,-)
/usr/include/cephfs/libcephfs.h
/usr/include/rados/buffer.h
/usr/include/rados/buffer_fwd.h
/usr/include/rados/crc32c.h
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
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/ceph/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/ceph/compressor/libceph_example.so
/usr/lib64/ceph/compressor/libceph_example.so.0
/usr/lib64/ceph/compressor/libceph_example.so.0.0.0
/usr/lib64/ceph/compressor/libceph_snappy.so
/usr/lib64/ceph/compressor/libceph_snappy.so.2
/usr/lib64/ceph/compressor/libceph_snappy.so.2.0.0
/usr/lib64/ceph/compressor/libceph_zlib.so
/usr/lib64/ceph/compressor/libceph_zlib.so.2
/usr/lib64/ceph/compressor/libceph_zlib.so.2.0.0
/usr/lib64/ceph/erasure-code/libec_isa.so
/usr/lib64/ceph/erasure-code/libec_jerasure.so
/usr/lib64/ceph/erasure-code/libec_jerasure_generic.so
/usr/lib64/ceph/erasure-code/libec_jerasure_sse3.so
/usr/lib64/ceph/erasure-code/libec_jerasure_sse4.so
/usr/lib64/ceph/erasure-code/libec_lrc.so
/usr/lib64/ceph/erasure-code/libec_shec.so
/usr/lib64/ceph/erasure-code/libec_shec_generic.so
/usr/lib64/ceph/erasure-code/libec_shec_sse3.so
/usr/lib64/ceph/erasure-code/libec_shec_sse4.so
/usr/lib64/rados-classes/libcls_cephfs.so
/usr/lib64/rados-classes/libcls_hello.so
/usr/lib64/rados-classes/libcls_journal.so
/usr/lib64/rados-classes/libcls_kvs.so
/usr/lib64/rados-classes/libcls_lock.so
/usr/lib64/rados-classes/libcls_log.so
/usr/lib64/rados-classes/libcls_numops.so
/usr/lib64/rados-classes/libcls_rbd.so
/usr/lib64/rados-classes/libcls_refcount.so
/usr/lib64/rados-classes/libcls_replica_log.so
/usr/lib64/rados-classes/libcls_rgw.so
/usr/lib64/rados-classes/libcls_statelog.so
/usr/lib64/rados-classes/libcls_timeindex.so
/usr/lib64/rados-classes/libcls_user.so
/usr/lib64/rados-classes/libcls_version.so

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

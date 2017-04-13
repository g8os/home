# G8OS

G8OS is a stateless cloud OS.

G8OS is an open-source operating system based on the Linux kernel and designed for building distributed, self-healing datacenters, optimized for running both containerized applications and virtual machines.

G8OS is stateless by not needing locally stored data, not even G8OS system files.

G8OS is lightweight, efficient and secure by only containing the components required to run containers and virtual machines, keeping the potential attack surface to the bare minimal, and administration easy.

G8OS boots containers from flists. Flists are relatively small metadata files that allow G8OS to fetch files from a storage cluster through a thin UnionFS-based FUSE layer. This happens on demand, only when the files are actually needed.

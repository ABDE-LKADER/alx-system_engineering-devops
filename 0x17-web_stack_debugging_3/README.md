# 0x17. Web Stack Debugging #3

## Overview

This project involves debugging a WordPress website running on a LAMP stack (Linux, Apache, MySQL, PHP). The objective is to identify and fix a 500 Internal Server Error using `strace` and automate the solution with Puppet.

## Concepts

For this project, we focused on:
- Understanding the basics of web servers and how to debug web stacks.
- Using `strace` to trace system calls and signals.
- Writing Puppet manifests to automate system configuration and fixes.

## Requirements

- All files are interpreted on **Ubuntu 14.04 LTS**.
- Every file must end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Puppet manifests must pass `puppet-lint` version **2.1.1** without any errors.
- Puppet manifests must run without error and should have:
  - A first-line comment explaining what the manifest does.
  - A `.pp` file extension.
- Files are checked with **Puppet v3.4**.

## Installation

To install `puppet-lint` on your system, run:

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

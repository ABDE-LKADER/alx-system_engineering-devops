# Web Stack Debugging #4

## Project Overview

This project focuses on debugging and optimizing a web stack involving Nginx. It involves two main tasks:

1. **Sky is the Limit**: Fix issues with the Nginx setup to handle a high volume of requests without failure.
2. **User Limit**: Adjust OS configuration to resolve errors related to file limits and user logins.

## Tasks

### 0. Sky is the Limit

**Objective**: Optimize Nginx configuration to handle a significant number of concurrent requests without errors.

**Details**:
- The web server setup was tested using ApacheBench with 2000 requests at a concurrency level of 100.
- Initial results showed a high number of failed requests.
- The goal was to optimize the configuration so that the number of failed requests drops to zero.

**Solution**:
- Modified the Nginx configuration to handle the load efficiently.
- The updated configuration was tested, and the number of failed requests was successfully reduced to zero.

**Files**:
- `0-the_sky_is_the_limit_not.pp`: Puppet manifest used for Nginx optimization.

**Results**:
- Before Optimization: 943 failed requests out of 2000.
- After Optimization: 0 failed requests out of 2000.

### 1. User Limit

**Objective**: Adjust OS configuration to resolve issues with file limits that prevent the `holberton` user from opening files.

**Details**:
- Encountered errors related to "Too many open files" when attempting to switch to the `holberton` user and open files.
- The goal was to change OS settings to allow the user to log in and open files without errors.

**Solution**:
- Adjusted OS configuration to increase the file descriptor limit.
- The configuration changes were applied successfully, resolving the file limit errors.

**Files**:
- `1-user_limit.pp`: Puppet manifest used to change OS configuration for user limits.

**Results**:
- Errors related to file limits were resolved, and the `holberton` user was able to log in and open files successfully.

## Requirements

- **Operating System**: Ubuntu 14.04 LTS
- **Files**:
  - All files must end with a new line.
  - Puppet manifests must pass `puppet-lint` version 2.1.1 without errors.
  - Puppet manifests must run without errors and must end with the `.pp` extension.
  - The first line of Puppet manifests should be a comment explaining its purpose.

**Installation of `puppet-lint`**:
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

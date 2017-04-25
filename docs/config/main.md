# Main Configuration

The main configuration is auto-loaded from the `g8os.toml` file.

In the [g8os/initramfs](https://github.com/g8os/initramfs) repository that you'll use for creating the G8OS boot image, `g8os.toml` can be found in the `/config/g8os` directory.

`g8os.toml` has the following sections:

- [\[main\]](#main)
- [\[sink\]](#sink)
- [\[logging\]](#logging)
- [\[stats\]](#stats)
- [\[globals\]](#globals)
- [\[extension\]](#extension)


<a id="main"></a>
## [main]

```toml
[main]
max_jobs = 200
include = "/config/root"
network = "/config/g8os/network.toml"
log_level = "debug"
```

- **max_jobs**: Max parallel jobs the core can execute concurrently (as its own direct children), once this limit is reached core0 will not pull for any new jobs from its dedicated Redis queue until it has at least one free job slot to fill
- **include**: Path to the directory with TOML files to include, this directory can have configurations for startup services and extensions, when core0 boots it will try to load all `.toml` files from the given locations, each of these TOML file can define one or more extensions to the core0 commands, and/or start up services
- **log_level** sets the logging level of core0 logs (what prints on console)
- **network**: Path to the network configuration file, discussed in [Network Configuration](network.md)


<a id="sink"></a>
## [sink]

A sink is a source of commands to run jobs.

Theoretically more than one sink type is supported. Currently only `redis` is supported as a sink type.

Each sink is defined in its own section as `[sink.<name>]` where name can be anything.

```
[sink.main]
# `url` Redis source url as shown below
url = "redis://127.0.0.1:6379"
# `password` optional Redis password.
password = ""
```


<a id="logging"></a>
## [logging]

In this section you define how Core0 processes logs from running processes.

Available loggers types are:

- **console**: prints logs on stdout (console) of Core0
- **redis**: forwards logs to Redis

For each logger you define log levels, specifying which log levels are logged to this logger.

Example:

```
[logging]
[logging.console]
type = "console"
levels = [1, 2, 4, 7, 8, 9]

[logging.redis]
type = "redis"
levels = [1, 2, 4, 7, 8, 9]
address = "127.0.0.1:6379"
batch_size = 1000
```

In the above example:

- The `[logging]` can be omitted since there are no shared settings for both loggers
- The second logger, of type `redis`, specifies with `batch_size` (wrongly chosen name) how many log messages are kept in the queue before older log messages will get dropped

See the section [Logging](../monitoring/logging.md) for more details about logging.

<a id="stats"></a>
## [stats]

This is where the statistics loggings is configured.

Here's an example:

```
[stats]
interval = 60000 # milliseconds (1 min)

[stats.redis]
enabled = true
flush_interval = 10 # seconds
address = "127.0.0.1:6379"
```

In this example there is one shared setting for all statistics logging, in this case specifying the `interval` (is deprecated)

See the section [Stats](../monitoring/stats.md) for more details about stats.


<a id="globals"></a>
## [globals]

Here all global module parameters are set.

Example:

```
[globals]
fuse_storage = "ardb://hub.gig.tech:16379"
```

With `fuse_storage` you set the default key-value store that will be mounted by [G8ufs](../g8ufs/g8ufs.md) when creating containers using the [container.create()](../interacting/commands/corex.md#create) command. The default, as shown above, is the ARDB storage cluster implemented in [G8OS Hub](../g8ufs/hub/hub.md). When creating a new container you can override this default by specifying any other ARDB storage cluster, as documented in [Creating Containers](../containers/creating.md).


<a id="extension"></a>
## [extension]

An extension is simply a new command or functionality to extend what core0 can do. This allows you to add new functionality and commands to core0 without actually changing its code. An extension works as a wrapper around the `core.system` command by wrapping the actual command call.

The below example is a user management extension for adding and removing users, and changing their passwords:

```toml
[extension."user.add"]
binary = "useradd"
args = ["-m", "{username}"]

[extension."user.delete"]
binary = "userdel"
args = ["-f", "-r", "{username}"]

[extension."user.chpasswd"]
binary = "sh"
args = ["-c", "echo '{username}:{password}' | chpasswd"]
```

Adding the above into a TOML file and saving it in one of the paths specified in the `include` section of the main configuration file will add the following commands to core0:

 - **user.add**
   - Args: `{"username": "user name to add"}`
 - **user.delete**
   - Args: `{"username": "user name to remove"}`
 - **user.chpasswd**
   - Args: `{"username": "user", "password": "password to set"}`

This allows you to call the extension from the Python client as follows:

```python
client.raw("user.add", {"username": "testuser"})
client.raw("user.chpasswd", {"username": "testuser", "password": "new-password"})
```

> Core0 takes care of substituting the `{key}` notation in the extension arguments with the ones passed from the client.

Extension also supports the following attributes:

```toml
[extension.test]
binary = "binary"
args = ["args", "list", "to", "binary"]
# cwd of the binary
cwd = "/path"

#env variables will be available during command execution
[extension.test.env]
env1 = "value-1"
env2 = "value-2"
```

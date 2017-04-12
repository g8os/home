# Core Commands

Available commands:

- [core.ping](#ping)
- [core.system](#system)
- [core.kill](#kill)
- [core.killall](#killall)
- [core.state](#state)
- [core.reboot](#reboot)


<a id="ping"></a>
## core.ping

Returns a "pong". Doesn't take any arguments. Main use case is to check wether the core is responding.


<a id="system"></a>
## core.system

Executes a given command.

Arguments:
```javascript
{
	"command": "{command}",
	"dir": "{directory}",
	"env": "{environment-variables}",
	"stdin": "{stdin-data}"
}
```

Values:
- **command**: command to execute including its arguments,  ex: 'ls -l /root'
- **directory**: Directory where to execute the command
- **env**: Comma separated environment values, in following format: `"ENV1": "VALUE1", "ENV2": "VALUE2"`
- **stdin-data**: Data to pass to executable over stdin

<a id="kill"></a>
## core.kill

Kills the process with given process/command ID. The process/command ID is the ID of the command used to start this process in the first place.

Arguments:
```javascript
{
    "id": "{process-id-to-kill}"
}
```


<a id="killall"></a>
## core.killall

Kills all processes on the system, i.e. only the ones that where started by core0 itself and still running by the time of calling this command. Takes no arguments.


<a id="state"></a>
## core.state

Returns aggregated state of all processes plus the consumption of Core0 itself (cpu, memory, etc...). Takes no arguments.


<a id="reboot"></a>
## core.reboot

Immediately reboot the machine. Takes no arguments.

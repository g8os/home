# Process Commands

Available commands:

- [process.list](#list)
- [process.kill](#kill)


<a id="list"></a>
## process.list

Lists all running processes.

Arguments:
```javascript
{
  'pid': {pid},
}
```

Values:
- **pid**: Optional parameter in order to list only one specific process



<a id="kill"></a>
## process.kill

Kills a process with given ID.

Arguments:
```javascript
{
  'id': {id},
  'signal': {signal},
}
```

> WARNING: beware of what you kill, if you killed Redis for example core0 or coreX won't be reachable.

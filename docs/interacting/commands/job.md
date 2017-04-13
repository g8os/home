# Job Commands

Available commands:

- [job.list](#list)
- [job.kill](#kill)


<a id="list"></a>
## job.list

Lists all running jobs.

Arguments:
```javascript
{
  'id': {id},
}
```

Values:
- **id**: Optional parameter in order to list only one specific job

<a id="kill"></a>
## job.kill

Kills a job with given ID.

Arguments:
```javascript
{
  'id': {id},
  'signal': {signal},
}
```

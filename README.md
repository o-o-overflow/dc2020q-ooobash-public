# ooobash

Intended solution: 13 locks to unlock to get the flag! Check the source code, and grep for `// OOOhack` for hints. See the list below for a short summary.

Unintended solution: I wrote the chall for last year's quals... and in the meantime it seems a [great "bash bug"](https://www.exploit-db.com/exploits/47726) popped out. Oops :-)


## info on locks

- 0 unlockbabylock built-in (unlockbabylock)
  - Just execute $ unlockbabylock
- 1 redir + noclobber (badr3d1r)
  - set noclobber option, redirect to existing file, filename len > 15, filename starts with badr3dir
- 2 sneakyoption (verysneaky)
  - set sneaky option, write a file with .sneaky extension
- 3 -L CLI option (you need to start another instance of bash to make it!) (leetness)
  - invoke bash with -L option
- 4 OOOENV var (vneooo)
  - OOOENV var needs to be set to "alsulkxjcn92"
- 5 call a sequence of commands in a row (eval)
- 6 check the return value from a program is 57 (ret)
  - (exit 57) (with parenthesis)
- 7 redirect to /dev/tcp/\*/53 (n3t)
  - echo xxx > /dev/tcp/localhost/53
- 8 USR1 signal (sig)
  - kill -s USR1 $(pgrep bash)
- 9 dup alias (yo)
  - redefine an alias, called yo, with a 'echo yo!'
- 10 "declare" on a read-only variable called ARO (aro)
- 11 invoke a function peppa so that: peppa does NOT exist, but peppax does. (modify the function look up) (fnx)
- 12 if / line number (ifonly)
  - write an if [] at line 7, where the "true" would actually return != 0

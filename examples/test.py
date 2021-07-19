from shell import Shell

sh = Shell("myShell")


def test(string):
    print(string)

sh.add_command(test)
sh.run()
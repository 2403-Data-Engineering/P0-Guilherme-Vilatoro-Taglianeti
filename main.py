from presentation.terminal import Terminal 

if __name__ == "__main__":
    terminal = Terminal()
    print("test")
    print(terminal.running)
    while (terminal.running):
        val = terminal.currentMenu.render()

        if (val[0] == 1):
            quit()
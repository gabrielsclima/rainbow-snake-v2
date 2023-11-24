# Getting started

# Running the code successfully
## Libraries
- [keyboard](https://pypi.org/project/keyboard/) (root is required on Linux);
- [time](https://docs.python.org/3/library/time.html) (alredy pre-installed);

## System requirements
I have developed this code when I still used Windows 7, but the built-in cmd didn't worked with ANSI colors.

I tested this code in the following systems:
* Windows 11 ✅;
* Windows 10✅;
* Pop!_OS 22.04LTS (My current OS)✅;
* Ubuntu 20.04LTS✅;
* Windows 7❌;

# Common Issues
* [Snake missing colors (Windows 10 >)](#snake-missing-colors-(windows));

## Snake missing colors (Windows)
Let's try the following steps:
1. Press Win + R, type "regedit" and press Enter;
2. Go to HKEY_CURRENT_USER and then Console;
3. Check if there is a DWORD called "VirtualTerminalLevel". If yes, open it and change the value to 1. If not:
   3.1. Click with the right button at the Console folder;
   3.2. Click on New > DWORD value (32 bits);
   3.3. Name the DWORD as "VirtualTerminalLevel";
   3.4. Open the DWORD you created and change its value to 1 (make sure to mark hexadecimal);
4. Relaunch the Command Prompt and see if it works.

If it didn't helped, make a report on [Issues](https://github.com/gabrielsclima/rainbow-snake-v2/issues) so I can have a better look into it.

## Am I lazy to solve the cross-platform issues?
No, I just want to foccus in developing the main idea before solving those issues.
  

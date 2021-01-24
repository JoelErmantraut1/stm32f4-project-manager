# stm32f4-project-manager

A group of scripts to create projects, compile code, flash on board and debug on STM32F4 discovery board.
Based in [LiviuBeraru Blink Example](https://github.com/LiviuBeraru/tuts/tree/master/stm/blinky).

# Description

This scripts provides a way of programming STM32F4 boards, without needing to use heavy IDEs, like [Eclipse](https://www.eclipse.org/eclipseide/).

# Usage

You can follow [Liviu Instructions](https://github.com/LiviuBeraru/tuts/blob/master/stm/blinky/Readme.md) to set all
dependencies needed to do all this work.

I had modified his scripts a bit to automate some tasks and make it more comfortable for daily use.

About files:

 - "add_libraries.py": Executable file which you need to run each time you want to add a library. Receives
 any number of parameters which represent libraries to add. Take care that:
    - In case of standard libraries you can time only it "base name" (for example "rcc" instead of "stm32f4xx_rcc.h").
    - If you want to add a file, include its path.
    - If you have a folder with libraries, include its path (of the folder) and it will add all .h and .c files (not recursively).
 - "create_project": Executable file which clones this repository and set files to create a new project.
 It receives a parameters that represents project name.
 - "Libraries": This file is included in Makefile, and is where libraries are added.
 - "Location": File that stores the location of the standard library software of STM, also included in Makefile.

# Take care of

In [Liviu Usage Instructions](https://github.com/LiviuBeraru/tuts/blob/master/stm/blinky/Readme.md#usage),
you will see you need to download standard library software, and:

> Edit the Makefile if needed:
>  - STM_DIR stores the location of the standard library folder.

In this case, you will need to edit "Location" file, in the same way. That is because "add_libraries.py" also
uses it, and in this way you edit it only once.

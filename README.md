## An implmentation of herbert language

A simple language which was created for the purpose of a puzzle/riddle game whit the same name.

### Install

	$ pip install herbert



### Run

	$ herbert code.h


### Usage

As an output the language will generate a chain combined of `s`, `r`, `l`, eg `sssrrssllss`

Where :
s - stands for straight This makes the robot move straight ahead;
l - stands for left) This makes the robot turns to its left;
r - stands for right) This makes the robot turns to its right.

Each of this steps is responsible of changing state of the game character.

For example the program `sssslssssr` means "move four units straight,
then turn to your left, move four units straight, then turn right."
Of course, any level may be solved just with these.

But the real objective of the game, is to write small programs (the smallest possible).
In order to do that language provides **functions**.

#### Basics

To call the same sequence of steps more than once. Functions are just a way
to group a sequence of commands that you can reuse many times.
For example, here is a program that creates a function:

	f:ssss
	flfr

The first line defines the function. Function have names consisting of
one lower case letter (here we named it 'f'), after the function name comes a ':'(colon)
then the instructions (called the function body, here it is 'ssss'),
and a new line terminates the definition. Now you can "call" the function
simply using its name as a new instruction, that is "flfr" is now equivalent to "sssslssssr".
Note that you cannot name a function 'r', 's' or 'l'
since those three letters are reserved for the three primitives of "h".

Function bodies can contain any instructions even other function calls. For example:
	
	f:ssss
	q:flfr
	q

#### Recursion

This program is equivalent to the above. Note how it defines
two functions ('f' and 'q'), and how the second one calls the first.
Functions can even call themselves, this is called recursion:

	f:sf
	f

In this program we define a function that executes an 's',
and then calls itself which executes 's', which calls 'f' again .... etc.
This means that, when executing the 'f' the robot well keep moving forward infinitely.


#### Numeric arguments (not implemented)


Functions can take arguments to control their behavior. There are two types of
arguments: instruction arguments, and numeric arguments. Here is an example of
numeric arguments:

	f[A]:ssslf[A-1]
	f[4]

The 'f' function takes a single argument (called 'A'). Argument names must be
one upper case letter.  When using such a function you must append the
parameters you want to pass (surrounded by round brackets) to the function
name. In the example, we passed 5 as the value of A. The 'f' function will
execute "sssl" and then calls itself with a parameter of A-1. That is, calling
f(4) will call f(3), which will call f(2), which will call f(1). Calling f(1)
will result in the execution of "sssl" but f(0) will never be called. This is
because if one of the numeric parameters to a function call is zero or less, the
call is not performed at all. In summary calling f(4) will result in
"ssslssslssslsssl". You can use any expression (for numeric parameters)
involving constants (such as 1, -5,..), argument names (A,B,..), plus sign ('+')
and minus sign ('-').


### Step arguments


There another kind of arguments called instruction arguments. Here is an example:

	f(B):Bf(Bs)
	f(l)
	
Here the parameter passed to 'f' is not supposed to be a number but an
instruction sequence (like "ssslssl"). In order to invoke the instuction
sequence passed as an argument simply use the argument name as a function call
(as in "f(A):sAlA"). In the above example, f is called with a single 'l'
instruction as a parameter. 'f' then invokes/executes its parameter, before
calling itself with the same parameter to which it appends a new 's'. In the end
this will result in the following (infinit) instruction sequence:
"llslsslssslsssslssssslssssss..."


#### Mixing arguments (not implemented)

Of course, you can have more than one argument and you can mix both types within
the same function:

	f(A)[B]:Arf(sA)[B-1]

Now f(s)[5] will result in "srssrsssrssssrsssssr"

That's it! You know all you need to know to write "h" programs.

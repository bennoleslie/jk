jk-lang
========

jk is a programming languaged designed for low-level systems programming.

Target applications are things such as embedded systems, operating system
kernels and language runtimes.

If you think C is too high-level and doesn't expose enough sufficiently
expose the underlying machine, then this might interest you.

If you think assembler is pretty neat but could do with some automatic
register allocation and stacking and a little bit of type safety,
then this might interest you.

If the first thing that comes to mind when someone says 'automatic
memory management' you think *stack*, not *heap* and certainly
not *garbage collection*, then this might interest you.

If you prefer your lanaguage with a truly minimal runtime, then this
might interest you. Long live `crt0.s`.

If you're scared by pointers, then this probably isn't for you.

If you think `++` was the best thing to happen to `C`, you probably
won't like this.

If you think "jQuery is bare-metal, then this certainly isn't for you.

Status
-------

Very early design phase. No code, no spec, no effects.

Everything is a work in progress; most everything here is unfinished;
the design is far from coherant. It is in the idea phase. I'm trying
something new in making this public instead of just scribbling in
notebooks! In all likelihood when you read this the project will
have been abandoned.

Concepts
---------

jk is an imperative language. As in most imperative languages core
is organised in to blocks.

Each element in a block is an *operation*. You can consider an
opeartion as somewhat analogous to a static inline function in C.  I
choose to avoid the term function under some crazy notation of
mathematical purity and so I didn't get harangued by that vicious
functional programming cabal for introducing side-affects to
functions.

So, the syntax for calling (executing? using? invoking?) an operation
is:

    oper_name a1 a2 ... aN => r1 r2 .. rN

Which basically mean invoke `oper_name` passing `a1` through `aN` as
arguments and place results in `r1` through `rN`.

Input parameters are automatically immutable in the invoked operation.
The input parameters, and results are passed by reference to
operation.

The syntax is somewhat inspired by assembly languages, with the
critical point of clearly delineating inputs from outputs with the
massive bit of syntax. You never need to worry about in which order
the parameters to `mov` belong.

As a practical example the C statement `r = a + b` would look something
like:

    add a b => r

There is a special chained syntax which may also be used:

    oper1 a1 ... aN => oper2 . b1 ... bN => r

In this example the result from invoking `oper1` is passed as the
first argument to `oper2`. This avoids the need to explicitly
allocation a temporary variable.

And for a practical example: `r = a * b + c`:

    mul a b => add . c => r

Note, that the special `.` automatic temporary can be passed
as any argument. Since `add` is commutative, the following is
equivalent:

    mul a b => add c . => r

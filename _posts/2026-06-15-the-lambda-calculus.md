---
layout : post
title : The λ Calculus
permalink : /the-lambda-calculus/
---

![lambda-lambda-lambda](/assets/images/the-lambda-calculus/banner.png)

> Note: This is a slightly edited reposting of [an Observable notebook originally published in 2021.](https://observablehq.com/@eitanlees/the-lambda-calculus)

I had not really understood what Lambda-calculus was or why it was important until I saw David Beazley's talk [Lambda Calculus from the Ground Up](https://youtu.be/pkCLMl0e_0k). I watched in amazement as Beazley turned a few simple functions into a universal computing machine. My goal here is to share that same experience with you. If you would rather watch than read, then seriously go watch Beazley's talk. It's amazing, he's amazing, I highly recommend it. 

**A Word of Warning**

This is a long journey with many treacherous paths, some of which may spiral out of control. You will be asked to 
<span style="background:#EFEFEF;padding:0 5px;border-radius:4px;font-weight:800">Pause & Ponder</span> throughout your adventure, but do not wander too far from the path I have set forth, as you may never return. Your efforts will be rewarded with the awe that accompanies understanding and hopefully the journey will give you more appreciation for all things computational.  

## Part 1: The Humble Function
![desert](/assets/images/the-lambda-calculus/desert.png)

Our story begins in a rather odd place. Instead of the rich and vibrant world of mathematics, you are accustomed to, we begin with almost nothing. A desolate wasteland with nothing but single-variable functions. You remember functions, right? 

$$f(x)$$

Plug in a value for $x$ and see what comes out. In middle school, you probably first learned about functions.

$$f(x) = 2x+3$$

The rules were pretty simple. Essentially you just replace $x$ with whatever you plugged in, turn the crank, and see what comes out.

$$f(5) = 2 \cdot 5 + 3 = 13$$

Those who have some experience with programming will also be familiar with functions. Their behavior is very similar to the mathematical ideal.


```
def f(x):
    return 2 * x + 3
```


```
f(5)
```




    13




```
f(2)
```




    7




```
f(1729)
```




    3461



There is no funny business here. The same old single-variable functions you met long ago, and have probably not paid much attention to since. 

In this strange land that is all there is. 

Nothing else...

* No packages
* No objects
* No strings
* No number
* No datatypes

... nothing but single variable functions.


```python
def f(x): return x + 1   # NOT ALLOWED! No numbers! No plus!

def f(x, y):  ...        # NOT ALLOWED! Single arguments only
```

This all sounds pretty restrictive! Well, what _can_ you do?

```python
def f(x): return x     # Yes.

def f(x): return x(x)  # Yes. x is a function. Everything is a function.

def f(x):
  def g(y):
    return x(y)        # Yes. f can construct and then return g.
  return g             # We will talk about that again soon ... 
```

Those are the rules. It's all very abstract and doesn't feel very useful. How are you expected to _do_ anything?! [David Beazley](https://www.dabeaz.com/) calls this a programming "Escape Room". 

How can we break out of this world of functions and make something more useful? That last example was sort of unusual. How does this have to do with computer science? Where are all of the lambdas?!?

![pause-and-ponder](/assets/images/the-lambda-calculus/pause-and-ponder.png)

Long before computers were integrated into every aspect of our lives, mathematicians were interested in the limits of mathematics, and computation played a vital role. The dream was to plug the rules of mathematics into a giant computation machine, let it run, and discover all the mathematics in the universe. The pursuit of such a dream led to the birth of computer science, and many other revolutionary ideas. Lambda calculus was introduced by [Alonzo Church](https://en.wikipedia.org/wiki/Alonzo_Church) as part of his research into formal mathematics and logical systems in the 1930s. In Church's work, he defined functions in a slightly different way than you learned in middle school. 



First of all instead of having named functions like $f$ or $g$, Church used $\lambda$ to define all of his functions 

$$ f(x) \Rightarrow \lambda x $$
$$ g(y) \Rightarrow \lambda y $$

These unnamed functions are sometimes called "[Anonymous Functions](https://en.wikipedia.org/wiki/Anonymous_function)" in computer programming. What the function _does_ is then written after a period like such 


$$ f(x) = 2x + 3\Rightarrow \lambda x.2x+3 $$
$$ g(y) = y^2 \Rightarrow \lambda y.y^2 $$

These examples are only to illustrate the notation. I'm breaking lots of rules. Look at all of those numbers! They aren't allowed! Addition!? No way!



Functions _can_ return other functions though, so can do something like 

$$ \lambda x. \lambda y. x(y) $$

which is exactly what we did in the example above when I was explaining the rules. Pass in an "$x$" and return a function which expects a "$y$". When that function is called it computes $x(y)$. Sometimes the notation is further abbreviated to 

$$ \lambda xy. xy $$

but remember that the extra λ's are still there, just assumed. The technique of turning a two-variable function into a series of single-variable functions is known as "Currying" named after [Haskell Curry](https://en.wikipedia.org/wiki/Haskell_Curry) and will be used frequently. 

Many programming languages have anonymous functions. For example, in Python, we could write


```
lambda x: 2 * x + 3
```




    <function __main__.<lambda>(x)>



The problem is that if we want to use that function elsewhere we have to give it a name. This is officially against the rules, but again I will break the rules for pedagogical reasons. I will break the rules a lot. Pay no attention to the man behind the curtain!


```
my_function = lambda x: 2 * x + 3
```


```
my_function(5)
```




    13



Curried functions can also be constructed by chaining function definitions


```
pythagoras = lambda a: lambda b: a*a + b*b
```


```
pythagoras(3)(4)
```




    25



Note the we are only ever passing single variables. `pythagoras` takes in the 3 and returns another function, which we then pass 4.

Now that we know the rules of the game, we can begin our journey!

## Part 2: The Switch

![switch](/assets/images/the-lambda-calculus/switch.png)

We almost got lost in the notation there for a minute. Where were we ... coming up with all of computer science from desolate wasteland single-variable functions, that's right. 

How did it go? It's hard to even make the first step. Let me show you a few things we can do to make some headway.

Let's define a function that takes in a few variables (one at a time) and then returns the "left" thing.


```
LEFT = lambda a: lambda b: a
```


```
LEFT('✅')('❌')
```




    '✅'



We could also consider the complimentary "right" function


```
RIGHT = lambda a: lambda b: b
```


```
RIGHT('✅')('❌')
```




    '❌'



It doesn't really matter what is the argument of the function is. You can think of these functions as a type of switch.


```
LEFT('On')('Off')
```




    'On'




```
RIGHT('On')('Off')
```




    'Off'



Flip the switch to the left and power is on. Flip the switch to the right and the power is off.

* Left, Right
* On, Off
* Zero, One

The dualistic behavior of these functions will the basis for constructing boolean values.



$$T \Rightarrow \lambda xy.x$$


```
TRUE = lambda x: lambda y: x
```

$$F \Rightarrow \lambda xy.y$$


```
FALSE = lambda x: lambda y: y
```

In fact they are exactly the same as our left and right functions. It is interesting that these functions represent a behavior, rather than the variables they take in. You might ask what is True? What does it mean to be True? Is it a thing or a behavior?

![pause-and-ponder](/assets/images/the-lambda-calculus/pause-and-ponder.png)

With True and False in hand, let's continue building up our logical toolkit. 

Next, we will consider the NOT operator. 

$$\neg x$$

We would expect the following behavior

```
NOT(TRUE)  ---> FALSE
NOT(FALSE) ---> TRUE
```

TRUE and FALSE are also functions and the NOT operator essentially flips their behavior. 


```
NOT = lambda x: x(FALSE)(TRUE)
```


```
NOT(TRUE)('✅')('❌')
```




    '❌'




```
NOT(FALSE)('✅')('❌')
```




    '✅'



Looking pretty good!

What about the behavior of AND?

$$
x \land y
$$

Sometimes it's helpful to look at a truth table to understand the behavior of a logical operator. Here is the truth table for the AND function.

| X | Y | Output |
|---|---|--------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

The behavior here is pretty simple. If the first value is `True`, then you need to go to the second value to determine the outcome. If the first value is `False`, then you are done — it's always `False`.

The AND function we construct would need to follow the same behavior. If `True`, then check the second variable. If `False`, then return `False`.

This does the trick.


```
AND = lambda x: lambda y: x(y)(x)
```

We can run through some examples to see if they match the truth table


```
AND(TRUE)(TRUE)('✅')('❌')
```




    '✅'




```
AND(TRUE)(FALSE)('✅')('❌')
```




    '❌'




```
AND(FALSE)(TRUE)('✅')('❌')
```




    '❌'




```
AND(FALSE)(FALSE)('✅')('❌')
```




    '❌'



And look at that! We've got an AND operator.

Let's keep this train rolling and build the OR operator.

$$
x \lor y
$$

| X | Y | Output |
|---|---|--------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |


```
OR = lambda x: lambda y: x(x)(y)
```


```
OR(TRUE)(TRUE)('✅')('❌')
```




    '✅'




```
OR(TRUE)(FALSE)('✅')('❌')
```




    '✅'




```
OR(FALSE)(TRUE)('✅')('❌')
```




    '✅'




```
OR(FALSE)(FALSE)('✅')('❌')
```




    '❌'



Now we are cooking with gas! If you notice the form of AND and OR are similar. 

$$\land \Rightarrow \lambda xy. xyx$$
$$\lor \Rightarrow \lambda xy. xxy$$

Almost like compliments of each other. This similarity feels right, intuitively. 


So far, we have made a switch and a handful of logical operators. You might have heard that all you need is a couple of logic gates like `AND`, `OR`, and `NOT` to [build an entire computer](https://www.nand2tetris.org/). While that is true, it is not the path we will take. In the 1930s the focus was more on the foundations of mathematics, so we will turn our attention to the fundamentals. 

## Part 3: Learning to Count

![abacus](/assets/images/the-lambda-calculus/abacus.png)

Almost all cultures have a system of counting. It is often taught to elementary school children using objects to represent numbers. 
* Five apples
* Two birds
* Six trees

Children quickly learn to use their fingers to keep track of larger tallies. As one becomes comfortable with counting, more abstract concepts can be tallied. 
* How many times did I eat today?
* How much do my shoes cost?
* How old am I?

Numbers play a vital role in the foundations of mathematics. How will we represent numbers in our world of single-variable functions?

Let me show you a few numbers and you might see the pattern


```
ONE = lambda f: lambda x: f(x)
```


```
TWO = lambda f: lambda x: f(f(x))
```


```
THREE = lambda f: lambda x: f(f(f(x)))
```

It seems the number of times a function is being called represents our "number". As good as any other object to represent number I guess.

What is a little odd is that our number `THREE` is itself another function. Everything is a function! It's the function that does something three times. By itself, it doesn't do


```
THREE
```




    <function __main__.<lambda>(f)>



Only by applying `THREE` to something can we see what it is doing. We can create a function which adds one to a value each time it is called


```
TALLY = lambda x: x + 1
```


```
TALLY(TALLY(TALLY(0)))
```




    3




```
THREE(TALLY)(0)
```




    3



`THREE` seems to be in good working order. Representing numbers in this fashion is called [Church Encoding](https://en.wikipedia.org/wiki/Church_encoding), and the numbers are sometimes called Church Numerals.


Our numbers can be applied to other functions as well


```
STAR = lambda x: x + '⭐'
```


```
THREE(STAR)('')
```




    '⭐⭐⭐'




```
FIB = lambda t: t + [t[-1] + t[-2]]
```


```
THREE(FIB)([1, 1])
```




    [1, 1, 2, 3, 5]



It is important to understand the "API" of the Church Numerals. You supply a function and a starting value, turn the crank, and see what comes out. It doesn't matter what the function or value is, what matters is the behavior of `THREE`.

With a few numbers already defined, we are off to the races!


```
FOUR = lambda f: lambda x: f(f(f(f(x))))
```


```
FIVE = lambda f: lambda x: f(f(f(f(f(x)))))
```

You might consider what `ZERO` would be in such a system. 

So far we have 

$$
\begin{aligned}
1 &\Rightarrow \lambda fx.fx \\
2 &\Rightarrow \lambda fx.ffx \\
3 &\Rightarrow \lambda fx.fffx \\
4 &\Rightarrow \lambda fx.ffffx \\
5 &\Rightarrow \lambda fx.fffffx \\
\end{aligned}
$$

Following this pattern, it appears that `ZERO` is just $x$. The "do nothing" operation. 


```
ZERO = lambda f: lambda x: x
```


```
ZERO(TALLY)(0)
```




    0



Interestingly the Church Numeral for `ZERO` is the exact same form as our boolean definition of `FALSE`. Zero, Nothing, False. Intuitively this feels right. Oddly, the `ONE` function is not exactly the same as `TRUE` though. Some food for thought ...

![ponder](/assets/images/the-lambda-calculus/pause-and-ponder.png)

As many kids experience, counting to five is pretty simple, but then you run out of fingers! Another hand full of fingers helps, but only so much. We have created a similar problem by hard-coding each number. To get a new number we have to add it to our list, and boy are there a lot of numbers!

## Part 4: Onwards and Upwards

![math](/assets/images/the-lambda-calculus/math.png)

What if we devised a scheme that takes us from one number to the next. All we would need is a starting place, say `ZERO`, and a "successor function" to walk along the number line. 

How to build such a function?

```
SUCC(TWO) ---> THREE
```

We want `SUCC` to take in a number, and output the next number. In effect, we want to apply our function "one more time" to our starting value. That is how Church Numerals are defined. So `SUCC` will need three parameters (but remember, only one at a time). 

1. $n$, the current number 
2. $f$, the function to apply 
3. $x$, the starting value

The logic is then to count up to the current number, and apply the function "one more time". In lambda notation it would look like 

$$\text{SUCC} \Rightarrow \lambda n f x . f(n f x)$$


```
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
```


```
SUCC(TWO)(TALLY)(0)
```




    3



Look at that! From `TWO` we have reached `THREE`. The concept of a successor function comes from the work of [Giuseppe Peano](https://en.wikipedia.org/wiki/Giuseppe_Peano) long before lambda calculus was created. Peano was interested in what the fundamental building blocks of mathematics were and developed the [Peano axioms](https://en.wikipedia.org/wiki/Peano_axioms). 

We now have the ingredients to build up other mathematical operations. For example, addition is similar to how it's done in elementary school. Start with your number, and then continue to "add one" the appropriate number of times. The "add one" is our successor function. 

$$ x + y \Rightarrow \lambda xy.y(SUCC)(x) $$


```
ADD = lambda x: lambda y: y(SUCC)(x)
```


```
ADD(FOUR)(FIVE)(TALLY)(0) # remember we still need to evaluate our number to see the result
```




    9



Multiplication is just repeated application of our function

$$ x \cdot y \Rightarrow \lambda xyf. x(yf) $$


```
MUL = lambda x: lambda y: lambda f: x(y(f))
```


```
MUL(FIVE)(TWO)(TALLY)(0)
```




    10



Exponentiation is the repetition of the repetition

$$ x^y \Rightarrow \lambda xy. y(x) $$


```
EXP = lambda x: lambda y: y(x)
```


```
EXP(TWO)(FIVE)(TALLY)(0)
```




    32



I hope by now you are starting to get the feeling that the world of single-variable functions, is not as desolate as I lead you to believe. It seems you have pulled yourself up by your bootstraps and created all of mathematics! Well not quite yet, but you are making progress. It turns out lambda calculus can be used to create other exciting things ...

## Part 5: All Roads Lead to λ

![gold-lambda](/assets/images/the-lambda-calculus/gold-lambda.png)

We have been talking a lot about mathematics, but lambda calculus can be used to create objects that are much more computer science oriented. 

For instance, we could define an object, like a tuple, which holds a pair of numbers. A "data structure" if you will. 


```
PAIR = lambda a: lambda b: lambda f: f(a)(b)
```


```
my_tuple = PAIR(2)(3)
```

As always this data structure is a function (everything is a function), so in order to inspect the contents, you need to call it appropriately.


```
my_tuple(TRUE)
```




    2




```
my_tuple(FALSE)
```




    3



You might make some accessor functions to make it easier to work with


```
FIRST = lambda p: p(TRUE)
```


```
SECOND = lambda p: p(FALSE)
```


```
FIRST(my_tuple)
```




    2




```
SECOND(my_tuple)
```




    3



These tuples can be nested to create lists of numbers.


```
my_list = PAIR(2)(PAIR(3)(4))
```


```
SECOND(SECOND(my_list))
```




    4



With these data structures, I will do something peculiar.  

Let's define a function $\phi$ which takes a `PAIR` as input and produces a `PAIR` as the output. 

The behavior of $\phi$ is a little unusual. It takes the first element of the input `PAIR`, adds one to it, then saves that in the first element of the output `PAIR`. The second element of the output `PAIR` is then just the first element of the input `PAIR` before the addition. Weird, I know, but we would expect this behavior

```
PHI( (0, 0) ) ---> (1, 0)
PHI( (1, 0) ) ---> (2, 1)
PHI( (2, 1) ) ---> (3, 2)
PHI( (3, 2) ) ---> (4, 3)
```

We can create such behavior with the tools we have built already by returning a `PAIR` of the `SUCC` of the `FIRST` and the `FIRST`. 


```
PHI = lambda p: PAIR(SUCC(FIRST(p)))(FIRST(p))
```


```
phi_test = FOUR(PHI)(PAIR(ZERO)(ZERO))
```


```
FIRST(phi_test)(TALLY)(0)
```




    4




```
SECOND(phi_test)(TALLY)(0)
```




    3



Nice, but what was the point of that? 

Remember earlier we defined a successor function? Now you have the tools to define its complement which calculates the predecessor of a given Church Numeral. 

The procedure is to count up to the given number using the $\phi$ function, starting with the `PAIR(ZERO, ZERO)` as input. Then take the second value of the output `PAIR`.  


```
PRED = lambda n: SECOND(n(PHI)(PAIR(ZERO)(ZERO)))
```

Let's check everything is working with a big number

$$4^5 - 1 = 1024 - 1 = 1023$$


```
big_number = EXP(FOUR)(FIVE)
```


```
PRED(big_number)(TALLY)(0)
```




    1023



Hurray! It's kind of silly to count all the way up to a big number and then subtract one, BUT it works! We are exploring what is possible, not what is efficient. 

With `PRED` you can define subtraction in a similar fashion to how you created addition

$$x - y \Rightarrow \lambda xy. y(PRED)(x)$$


```
SUB = lambda x: lambda y: y(PRED)(x)
```


```
SUB(FIVE)(TWO)(TALLY)(0)
```




    3



If this all feels a bit contrived, that is ok. It's a bit of a hack. There is a more formal definition of subtraction but it's long and complicated. The hack is more fun! 

There is one final object we will build that has to do with control flow. When programing you want a way to make decisions and change your behavior based on the outcome. For that, we will create a function that tests if a number is `ZERO` and return `TRUE` or `FALSE`. 

```
ISZERO(ZERO) ---> TRUE
ISZERO(ONE) ---> FALSE
ISZERO(TWO) ---> FALSE
```

To construct this function remember the "API" for all Church Numerals. They need a function and a starting value. The behavior of `ZERO` is to return the starting value, ignoring the function. In our case, we would want to return `TRUE`. Then the question is what should the function we pass to our number? Well, we want it to always evaluate to `FALSE` because by definition if the function is used, the number is not `ZERO`. So we will pass in the "always `FALSE`" function. 

Our conditional logic can be written up as 


```
IS_ZERO = lambda n: n(lambda f: FALSE)(TRUE)
```


```
IS_ZERO(ZERO)('True')('False')
```




    'True'




```
IS_ZERO(TWO)('True')('False')
```




    'False'



And it works! You have control flow now. Oh, the places you'll go!

Let's review what you have created thus far, and reflect on the journey we have made. Here is a table of all of the functions we have cobbled together:

| Name | Description |
|------|-------------|
| `TRUE` | Boolean True |
| `FALSE` | Boolean False |
| `NOT` | Logical Not |
| `AND` | Logical And |
| `OR` | Logical Or |
| `ONE`, `TWO`, `THREE`, ... | Church Numeral |
| `SUCC` | Successor of a Number |
| `PRED` | Predecessor of a Number |
| `ADD` | Addition |
| `SUB` | Subtraction |
| `MUL` | Multiplication |
| `EXP` | Exponentiation |
| `PAIR` | Tuple Data Structure |
| `FIRST` | `PAIR` accessor method |
| `SECOND` | `PAIR` accessor method |
| `ISZERO` | Zero Conditional |

You started from the world of single-variable functions and have built up up up until arriving at a sort of assembly language you could use to write some programs. I think this is really incredible! I think this calls for some introspection ... what else could we do? What _can't_ we do!?

![pp](/assets/images/the-lambda-calculus/pause-and-ponder.png)

What a journey it has been. I hope along the way you have come to appreciate some of the beauty and wonder of lambda calculus. 

Here is an outline of what we did:
1. From the world of single-variable functions construct the booleans `TRUE` and `FALSE`. 
2. With booleans defined, create a few logical operators `NOT`, `AND`, and `OR`. 
3. Define a number system, `ONE`, `TWO`, `THREE`, and create a successor function `SUCC`. 
4. Using `SUCC` and number composition, create arithmetic operations `ADD`, `MUL`, `EXP`
5. Create some "data structures" such as the `PAIR` function. 
6. Using `PAIR` and a few accessor methods, `FIRST` and `SECOND`, hack together subtraction using `PHI`, `PRED`, and `SUB`.
7. Define an `ISZERO` function to allow for control flow.

A surprising result! With this momentum is seems we could do anything!

## Part 6: Self Reflection

![mirror](/assets/images/the-lambda-calculus/mirror.png)

You have come a long way on this journey into lambda calculus. For this final part of our adventure, I'll do the heavy lifting. This is a special treat. A reward for your efforts. 

Sit back, relax, and let me show you something cool. 

Combinatory logic is a field of study closely related to lambda calculus. The idea of a "combinator" is what you have been creating all along. The functions you have made are all considered combinators. They can be combined and joined in interesting ways, to create a whole family of interesting behavior, as we have already seen. 

I would like to introduce possibly the most famous combinator of all ... 

✨✨✨ __The Y Combinator__ ✨✨✨

The Y combinator is nothing more than a function. As with all of the functions we have made so far, we are trying to capture some kind of behavior. In this case, we are interested in recursion. 

Let's first look at how recursive functions are often created using self-reference. 

Our object of study will be the [Factorial](https://en.wikipedia.org/wiki/Factorial). 

$$ n!=n\cdot (n-1)\cdot (n-2)\cdot (n-3)\cdot \cdots \cdot 3\cdot 2\cdot 1 $$

For example,

$$ 5!=5\cdot 4\cdot 3\cdot 2\cdot 1=120 $$

We can create a function that performs this calculation


```
fact = lambda x: 1 if x == 0 else x * fact(x - 1)
```


```
fact(5)
```




    120



We have defined the factorial function by calling the factorial function. This is a hallmark of recursion. A function calling itself.

One issue is in lambda calculus we are not allowed to assign names to functions. Everything is anonymous. We have been storing our functions as named variables, but that was just me breaking the rules.

How could we re-write our factorial function without using the name in the definition? Suppose this was our starting definition

```
fact = lambda x: 1 if x == 0 else x * fact(x - 1)
```

We could try pulling out the internal function call into a separate variable that we then pass to the function. Sort of like "factoring out" the function call. 
```
fact = ( lambda f: lambda x: 1 if x == 0 else x * f(x - 1) )( fact )
```

but that won't _really_ work. We have just pushed our problems to the side, literally! 

Here is where the magic happens. Pay attention! The function we pass in will be **the same** as the function definition

```
fact = ( lambda f: lambda x: 1 if x == 0 else x * f(x - 1) ) \
       ( lambda f: lambda x: 1 if x == 0 else x * f(x - 1) )
```
but that won't _really_ work. We are calling our function incorrectly. The "API" of our new function takes two parameters, `f` and `x`. 

Modifying our function calls should do the trick. 


```
fact = ( lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1) ) \
       ( lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1) )
```

Amazingly that works!


```
fact(5)
```




    120



It really works! Whoa! In case that happened too fast, go back and follow the steps. 

We started with a self-referential function. Then
1. We "factored out" the self-reference
2. We "repeated ourselves" by replacing the passed function with the inner definition
3. We did an "API correction" to account for calling the function

I would like to draw special attention to the first step of "factoring out" the function.

```
fact = ( lambda x: 1 if x == 0 else x * fact(x - 1) )
fact = ( lambda f: lambda x: 1 if x == 0 else x * f(x - 1) )( fact )
```
If we replace the inner definition with `R` we find
```
R = ( lambda f: lambda x: 1 if x == 0 else x * f(x - 1) )
fact = R(fact)
```
This is an interesting result. When `fact` is passed to the `R` function, it returns `fact`. A mathematician would say `fact` is a "fixed point" of `R`. 

The [fixed point](https://en.wikipedia.org/wiki/Fixed_point_(mathematics)) of a function is any input that results in the same output when the function is applied. For example, given the function
$$f(x)=x^{2}-3x+4$$
we would say that $2$ is a fixed point of $f$, because $f(2) = 2$. Fixed points are an area of interest for mathematicians. Not all functions have a fixed point, for example $f(x) = x + 1$ has no fixed point. Every input maps to a different output. Some functions when applied repeatedly approach a fixed point. For instance, the square root function, $f(x)=\sqrt{x}$,  approaches 1 when repeatedly applied. 

$$f(f(\ldots f(x) \ldots )) = \sqrt{\sqrt{\cdots\sqrt{x}}} = 1$$

We can use our Church Numerals to repeatedly apply the `math.sqrt` function. 


```
import math
ONE(math.sqrt)(1729)
```




    41.58124577258358




```
TWO(math.sqrt)(1729)
```




    6.448352174981108




```
THREE(math.sqrt)(1729)
```




    2.5393605838834916



... until finally ...


```
big_number(math.sqrt)(1729)
```




    1.0



In our factorial example `fact` looked like a fixed point of `R`. Functions can be fixed points of functions. It's turtles all the way down! 

Now suppose there is a function `Y` which can calculate the fixed point of `R`. Let's apply our steps from before and see what happens

```
Y(R) ---> Fixed point of R

Y(R) = R(Y(R))                                               # Replacing fact

Y(R) = (lambda x: R(x))(Y(R))                                # Factoring out Y(R)

Y(R) = (lambda x: R(x))(lambda x: R(x))                      # Repeat yourself

Y(R) = (lambda x: R(x(x)))(lambda x: R(x(x)))                # API correction

Y(R) = (lambda f: (lambda x: f(x(x)))(lambda x: f(x(x))))(R) # Factor out R

   Y = (lambda f: (lambda x: f(x(x)))(lambda x: f(x(x))))    # Divide both sides by (R)

```

That is it! ✨✨✨[The Y Combinator](https://en.wikipedia.org/wiki/Fixed-point_combinator#Fixed-point_combinators_in_lambda_calculus)✨✨✨

$$ Y=\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))\ .$$


```
Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))
```

If we define the inner part of our factorial function,


```
R = lambda f: lambda x: 1 if x == 0 else x * f(x - 1)
```

we can give it a whirl!

```
factorial_Y = Y(R)

---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)
Cell In[86], line 1
----> 1 factorial_Y = Y(R)

Cell In[84], line 1, in <lambda>(f)
----> 1 Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))

Cell In[84], line 1, in <lambda>(x)
----> 1 Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))

Cell In[84], line 1, in <lambda>(x)
----> 1 Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))

Cell In[84], line 1, in <lambda>(x)
----> 1 Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))

    [... skipping similar frames: <lambda> at line 1 (2972 times)]

Cell In[84], line 1, in <lambda>(x)
----> 1 Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))

RecursionError: maximum recursion depth exceeded
```

Unfortunately, the Y combinator runs off and never returns. The error here has to do with how the function is evaluated. Essentially there is no bottom when constructing the Y combinator. The computer keeps unraveling the definition until the stack overflows. To avoid this problem we can introduce a dummy variable $v$ which will be passed through the function.

```
Y       = lambda f: (lambda x: f(           x(x)    ))   (lambda x: f(          x(x)   ))  \\ Original
Y_prime = lambda f: (lambda x: f( lambda v: x(x)(v) ))   (lambda x: f(lambda v: x(x)(v)))  \\ Modified
```
What we have done is trick the computer to avoid the evaluation of the function parameters, until execution. This modified Y Combinator is known as the Z combinator. 

$$ Z=\lambda f.(\lambda x.f(\lambda v.xxv))\ (\lambda x.f(\lambda v.xxv))\ .$$


```
Z = lambda f: (lambda x: f( lambda v: x(x)(v) ))   (lambda x: f(lambda v: x(x)(v)))
```


```
factorial_Z = Z(R)
```


```
factorial_Z(5)
```




    120



and it works! We have made a combinator that can turn the definition of a single recursive step into a proper recursive function.

As another example consider the Fibonacci sequence


```
Fibonacci = lambda f: lambda x: x if x <= 1 else f(x-1) + f(x-2)
```


```
Fib_Z = Z(Fibonacci)
```


```
Fib_Z(10)
```




    55



and sure enough, the tenth Fibonacci number is 55!

The power of lambda calculus seems to know no bounds. In fact lambda calculus is a universal computing machine. It can calculate anything that is possible to calculate! The [Church–Turing thesis](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis) outlines the very limit of what computation is. You have been playing with some very powerful ideas here, I think it's time to ...

![pp](/assets/images/the-lambda-calculus/pause-and-ponder.png)

For a grand finale, I wanted to define the factorial using only the lambda functions we created earlier but ran into some trouble.


```
R_lambda = lambda f: lambda x: IS_ZERO (x) ( ONE ) ( MUL (x) ( f( PRED(x) ) ) )
```

I think the logic above is sound. Then I fed it to the Z combinator


```
FACT = Z(R_lambda)
```

no issues yet ... but when I ran it I hit an error 🙁



```
FACT(FIVE)(TALLY)(0)

---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)
Cell In[94], line 1
----> 1 FACT(FIVE)(TALLY)(0)

Cell In[92], line 1, in <lambda>(x)
----> 1 R_lambda = lambda f: lambda x: IS_ZERO (x) ( ONE ) ( MUL (x) ( f( PRED(x) ) ) )

Cell In[86], line 1, in <lambda>(v)
----> 1 Z = lambda f: (lambda x: f( lambda v: x(x)(v) ))   (lambda x: f(lambda v: x(x)(v)))

Cell In[92], line 1, in <lambda>(x)
----> 1 R_lambda = lambda f: lambda x: IS_ZERO (x) ( ONE ) ( MUL (x) ( f( PRED(x) ) ) )

Cell In[86], line 1, in <lambda>(v)
----> 1 Z = lambda f: (lambda x: f( lambda v: x(x)(v) ))   (lambda x: f(lambda v: x(x)(v)))

Cell In[92], line 1, in <lambda>(x)
----> 1 R_lambda = lambda f: lambda x: IS_ZERO (x) ( ONE ) ( MUL (x) ( f( PRED(x) ) ) )

Cell In[86], line 1, in <lambda>(v)
----> 1 Z = lambda f: (lambda x: f( lambda v: x(x)(v) ))   (lambda x: f(lambda v: x(x)(v)))

    [... skipping similar frames: <lambda> at line 1 (1484 times), <lambda> at line 1 (1483 times)]

Cell In[86], line 1, in <lambda>(v)
----> 1 Z = lambda f: (lambda x: f( lambda v: x(x)(v) ))   (lambda x: f(lambda v: x(x)(v)))

Cell In[92], line 1, in <lambda>(x)
----> 1 R_lambda = lambda f: lambda x: IS_ZERO (x) ( ONE ) ( MUL (x) ( f( PRED(x) ) ) )

Cell In[68], line 1, in <lambda>(n)
----> 1 PRED = lambda n: SECOND(n(PHI)(PAIR(ZERO)(ZERO)))

Cell In[59], line 1, in <lambda>(p)
----> 1 SECOND = lambda p: p(FALSE)

RecursionError: maximum recursion depth exceeded
```

I do not know why this is happening. I am not sure if it's a problem with my definitions, an Observable limitation, or a JavaScript quirk. I am stumped and a man can only stare into the abyss so long before he goes crazy, so I have left it as an exercise to the reader 😉 to figure out why this isn't working. Seriously, feel free to fork this notebook, play around, and submit a change.

**UPDATE**:

For years this unresolved issue kept bothering me. I would be out on a nice walk and think to myself

> Hey remember that lambda calculus piece you did where you were unable to figure out the big finale?!?

Well it turns out that five years later I have become the reader for which I left this problem as an exercise. This is starting to sound a bit recursive ...

Let's get back to the issue

Earlier when trying to use the Y Combinator we ran into a similar issue. The definition of the Y Combinator was correct, but when trying to use it we ran into an issue of eager evaluation. To address this we introduced a dummy variable to defer evaluation.

Now a similar issue is happening but in the branches of our recursive definition. To defer the evaluation of a branch we again can introduce a dummy variable.


```
R_lambda = lambda f: lambda x: (
    IS_ZERO(x)
        (lambda: ONE)
        (lambda: MUL(x)(f(PRED(x))))
)()
```


```
FACT = Z(R_lambda)
```

and now ... drum roll ...


```
FACT(FIVE)(TALLY)(0)
```




    120



🎉🎉🎉 Hooray!!! 🎉🎉🎉

A recursive factorial function defined entirely in terms of lambda calculus. Amazing!

## Conclusion

I hope you enjoyed this journey into the world of lambda calculus! Maybe next time you use a computer, take a moment to <span style="background:#EFEFEF;padding:0 5px;border-radius:4px;font-weight:800">Pause & Ponder</span> all the amazing things happening right under your nose. 

For thoese interested in learning more, I've included a few references used while making this piece:
- [Lambda Calculus from the Ground Up](https://youtu.be/pkCLMl0e_0k) by David Beazley
- [A Flock of Functions Part 1](https://youtu.be/3VQ382QG-y4) & [Part 2](https://youtu.be/pAnLQ9jwN-E) by Gabriel Lebec
- [Combinatory Logic: From Philosophy and Mathematics to Computer Science](https://www.um.edu.mt/library/oar/bitstream/123456789/38118/1/Alexander%20Farrugia.pdf) by Alexander Farrugia
- [Y and Z combinators in Javascript](https://medium.com/swlh/y-and-z-combinators-in-javascript-lambda-calculus-with-real-code-31f25be934ec) by Enrico Piccinin
- [Combinators and the Story of Computation](https://writings.stephenwolfram.com/2020/12/combinators-and-the-story-of-computation/) by Stephen Wolfram

Till next time, 

-Eitan 

# solid_principle
1) The Single-responsibility principle (SRP)
“A class should have one, and only one, reason to change”
In other words, every component of your code (in general a class, but also a function) should have one and only one responsibility. As a consequence of that, there should be only a reason to change it.


2) The Open–closed principle (OCP)
“Software entities … should be open for extension but closed for modification”
In other words: You should not need to modify the code you have already written to accommodate new functionality, but simply add what you now need.
This does not mean that you cannot change your code when the code premises needs to be modified, but that if you need to add new functions similar to the one present, you should not require to change other parts of the code.

3) The Liskov substitution principle (LSP)
“Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it”
Alternatively, this can be expressed as “Derived classes must be substitutable for their base classes”.
In (maybe) simpler words, if a subclass redefines a function also present in the parent class, a client-user should not be noticing any difference in behaviour, and it is a substitute for the base class.
For example, if you are using a function and your colleague change the base class, you should not notice any difference in the function that you are using.

4) The Interface Segregation Principle (ISP)
“Many client-specific interfaces are better than one general-purpose interface”
In the contest of classes, an interface is considered, all the methods and properties “exposed”, thus, everything that a user can interact with that belongs to that class.
In this sense, the IS principles tell us that a class should only have the interface needed (SRP) and avoid methods that won’t work or that have no reason to be part of that class.


5) The Dependency Inversion Principle (DIP)
“Abstractions should not depend on details. Details should depend on abstraction. High-level modules should not depend on low-level modules. Both should depend on abstractions”
So, that abstractions (e.g., the interface, as seen above) should not be dependent on low-level methods but both should depend on a third interface.

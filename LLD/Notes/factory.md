## Agenda

- 1 Motivation
  ------------


  1. Real world
  2. Technical
     2. Simple Factory
     1. implementation
     2. code
     3. Factory Method
- Abstract Factory

  1. Factory of Factories
- ![solution1.png](assets/solution1.png)




Factory:

1. jute --->C/T/S
2. modern -->C/T/S
3. victoria-->C/T/S


### Algorithms

1. step-1:Product interface
   1.Button: onclick(),render()
   2. CheckBoox:onSelect(),render()
2. concreate product classes
   1. Button----> light
   2. Button ---> dark
   3. checkBox--->light
   4. checkBox--->dark
3. abstract factory interface
   1. two method - checkboxcreate()
   2. buttonCreated()
4. create family of factory
   example:
   1. lightformfactory
   2. darkformfactory

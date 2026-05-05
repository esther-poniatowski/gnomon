# Proof and Derivation Encoding - Atomic Epistemic Acts

It seems that there exists a family of epistemic acts that are *atomic* in the sense that they perform a single transformation or introduce a single new information. 

For instance:

- introducing the target quantity to be expanded or solved
- substituting a definition into a formula / instantiating an expression with specific parameters
- developping / factorizing an expression
- simplifying an expression by algebraic manipulation (i.e. eliminating redundant terms, canceling factors, etc)
- solving an elementary equation
- differentiating a function with respects to a variable
- integrating a function over a domain
- applying an identity (e.g. trigonometric, combinatorial, etc)
- applying a theorem (once all the conditions of applicability are already established, it consists in explicitly listing the conditions and deducing the conclusion)
- identifying a portion of an expression to define a new auxiliary object
- identifying a singularity (i.e. a point where a function is not defined, or a term that becomes infinite, etc)
- introducing a case distinction

Within a goal-directed reasoning, those acts can be chained. For the purpose of revealing the internal logic of the reasoning and to gain intelligibility:

- *each* act must be an **explicit, inspectable, and composable unit**
- each act must be preceded by the **remaining gap** it is meant to fill (i.e. why the goal is not yet satisfied from the previous step), to make explicit how it advances the overall inquiry.

For instance:

- **Goal**: solve an equation for a variable $x$
- **Step 1**: introduce the target quantity $y = f(x)$
- **Step 2**: apply the definition of $f$ to rewrite $y$ in terms of $x$
- **Step 3**: develop the resulting expression
- **Step 4**: simplify the resulting expression
- **Step 4**: isolate the variable $x$ on one side of the equation
- **Step 5**: identify the solution as $x = g(y)$
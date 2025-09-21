# LangGraph Core Concepts 

## Graph  
A **Graph** in LangGraph defines the overall structure, representing how nodes (steps) are connected through edges to enable flow control.

## Node  
A **Node** is an individual unit of computation or logic in LangGraph, responsible for performing a specific task within the graph.

## Edges  
**Edges** are connections between nodes in LangGraph that determine the flow of execution based on conditions or outcomes.

## State  
**State** in LangGraph represents the current data or context being passed and modified throughout the graph execution.

## Reducer  
A **Reducer** is a function in LangGraph responsible for merging updates to the state after each node's execution.

## LangGraph Model Execution  

**LangGraph Model Execution** is the process of running the graph, starting from an initial state, passing through nodes via edges, updating state via reducers until completion.
it has multipe steps 
1) graph definition 
    state schema 
    nodes 
    edge
2) compilation
    .compile function -it check all nodes there connections
3) invocation
    run the graph by using .invoke(initial state)
    then langgraph send initial state as a message to the entry node
4) super step begin
    execution proceed in rounds

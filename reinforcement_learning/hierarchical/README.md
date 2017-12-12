---
layout: default
title: Hierarchical RL
---

# Hierarchical RL

| Year | Title | Authors | Affiliation | Code | Other |
| --- | --- | --- | --- | --- | --- |
| 2017 | [Communicating Hierarchical Neural Controllers for Learning Zero-Shot Task Generalization](papers/communicating_hierarchical_neural_controllers.pdf, "The ability to generalize from past experience to solve previously unseen tasks is a key research challenge in reinforcement learning (RL). In this paper, we consider RL tasks defined as a sequence of high-level instructions described by natural language and study two types of generalization: to unseen and longer sequences of previously seen instructions, and to sequences where the instructions themselves were previously not seen. We present a novel hierarchical deep RL architecture that consists of two interacting neural controllers: a meta controller that reads instructions and repeatedly communicates subtasks to a subtask controller that in turn learns to perform such subtasks. To generalize better to unseen instructions, we propose a regularizer that encourages to learn subtask embeddings that capture correspondences between similar subtasks. We also propose a new differentiable neural network architecture in the meta controller that learns temporal abstractions which makes learning more stable under delayed reward. Our architecture is evaluated on a stochastic 2D grid world and a 3D visual environment where the agent should execute a list of instructions. We demonstrate that the proposed architecture is able to generalize well over unseen instructions as well as longer lists of instructions.") | Junhyuk Oh, Satinder Singh, Honglak Lee | Michigan/Microsoft | | |
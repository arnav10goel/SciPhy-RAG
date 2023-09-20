# SciPhy-RAG

- This project aims to apply techniques from the domain of controllable scientific text generation to <b> High School Physics </b>
- The main idea behind the research project stems from the hypothesis that Physics Word Problems (PWPs) require understanding of concepts based on physics formulae and is thus a fundamentally different task from Math Word Problems (MWPs).

## Fine-Tuning Vicuna using LoRA

- Vicuna is a state-of-the-art model, and fine-tuning it can yield superior results for specific applications. This document provides an overview of how we fine-tuned Vicuna using the LoRA technique for both 8-bit and 16-bit.
- LoRA (Low-Rank Adaptation) is a method used to efficiently fine-tune large neural networks. By adapting only a small part of the model, it allows for quicker updates and can yield significant benefits in performance, especially when there's limited data for fine-tuning.
- The rank of the matrix is adjusted for achieving 8-bit and 16-bit quantisation.
- We refer to the following repository for helping us fine-tune using LoRA: [Link](https://github.com/jackaduma/Vicuna-LoRA-RLHF-PyTorch)

This repository contains all the scripts, datasets, and additional resources to reproduce the results and further delve into the details of fine-tuning Vicuna with LoRA.

---

Happy fine-tuning!


### Retrieval Experiment Setup (SciPhy-RAG):
- Wikipedia Articles are extracted using <b> similarity search </b> on sub-topics and the title of Wikipedia pages.
- These are stored as embeddings in a vector database (e.g. Pinecone).
<img width="822" alt="Screenshot 2023-09-21 at 3 11 45 AM" src="https://github.com/arnav10goel/SciPhy-RAG/assets/97335445/86f4d63a-d9bd-41a3-8031-af5c123f5d7f">

- At the time of inference when running the model, the question is sent to the vector database. Here Approximate Nearest Neighbor (ANN) search is applied to find N relevant passages for solving the question.
- The question and N relevant passages are then sent as input-prompt to the Language Model for solving the question.

### Final Results:
<img width="782" alt="Screenshot 2023-09-21 at 3 16 00 AM" src="https://github.com/arnav10goel/SciPhy-RAG/assets/97335445/f9ef8a96-d343-4bea-8435-2ecf0fb5be5d">



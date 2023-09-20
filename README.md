# SciPhy-RAG

- This project was awarded the <b> Summer Undergraduate Research Fellowship 2023 </b> and is done under the guidance of Dr. Rajiv Ratn Shah from MIDAS-IIITD.
- It aims to apply techniques from the domain of controllable scientific text generation to <b> High School Physics </b>
- The main idea behind the research project stems from the hypothesis that Physics Word Problems (PWPs) require understanding of concepts based on physics formulae and is thus a fundamentally different task from Math Word Problems (MWPs).

## Data Collection and Augmentation:
- Topics from Indian High School Physics textbooks are collected alongwith questions from datasets such as SCIMAT (Kollepara et al. 2021) which consist of inconsistencies we fix.
- Linear transformations are applied on the questions to augment the data to a bigger size based off the idea that linearly transformed questions will help the language model better understand the underlying concept.

## Fine-Tuning Vicuna using LoRA
- Vicuna is a state-of-the-art model, and fine-tuning it can yield superior results for specific applications. This document provides an overview of how we fine-tuned Vicuna using the LoRA technique for both 8-bit and 16-bit.
- Low-Rank Adaptation or LoRA (Hu et al. 2021) is a method used to efficiently fine-tune large neural networks by decomposing the weight matrix to lower rank matrices. By adapting only a small part of the model, it allows for quicker updates and can yield significant benefits in performance, especially when there's infrastructure for fine-tuning.
- The rank of the matrix is adjusted for achieving 8-bit and 16-bit quantisation.
- We refer to the following repository for helping us fine-tune using LoRA: [Link](https://github.com/jackaduma/Vicuna-LoRA-RLHF-PyTorch)

- We use our hand-annotated dataset comprising 9.5K physics questions. We divide that into a training and testing split and fine-tune the model on the training set using supervised fine-tuning.
- We check for inference on the test set.

## Retrieval Experiment Setup (SciPhy-RAG):
- Wikipedia Articles are extracted using <b> similarity search </b> on sub-topics and the title of Wikipedia pages.
- These are stored as embeddings in a vector database (e.g. Pinecone).
<img width="822" alt="Screenshot 2023-09-21 at 3 11 45 AM" src="https://github.com/arnav10goel/SciPhy-RAG/assets/97335445/99718311-f725-4f0e-983a-685f1de12744">


- At the time of inference when running the model, the question is sent to the vector database. Here Approximate Nearest Neighbor (ANN) search is applied to find N relevant passages for solving the question.
- The question and N relevant passages are then sent as input-prompt to the Language Model for solving the question. The inference is checked on the test again to get the results.

### Final Results:
<img width="782" alt="Screenshot 2023-09-21 at 3 16 00 AM" src="https://github.com/arnav10goel/SciPhy-RAG/assets/97335445/685c7713-abd6-4715-8bb5-bcd3eb5ab43d">

- We release our data augmentation codes for generating the dataset alongwith the train and testing questions used.
- We additionally release the code for the retrieval pipeline.


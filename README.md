# Daraselia, S. (2024) Issues in Training the TreeTagger for Georgian. Corpora. ISSN 1749-5032 (In Press) 

The paper describes the process of retraining the TreeTagger program (Schmid, 1994) for the Georgian language. This includes some general procedures such as designing a training corpus, creating a tagging lexicon, and training the TreeTagger on Georgian texts. I use a novel KATAG tagset and enclitic tokenization approach in part-of-speech tagging. The KATAG tagset is based on a new morphosyntactic language model (Daraselia and Hardie, fc). In this paper, I address some major disambiguation issues that were revealed in training the
TreeTagger on Georgian texts. I discuss some ways to get around these issues, such as implementing a workaround to the tagging lexicon. I report on the performance of the TreeTagger program and compare how different parameters such as the size of the training
lexicon or context and affix lengths have effects on the Tagger’s performance.
https://eprints.whiterose.ac.uk/205337/1/Daraselia_Training%20TreeTagger.pdf 



# Daraselia, Sophiko (2019) Computational Analysis of Morphosyntactic Categories in Georgian. PhD thesis, University of Leeds.

This thesis describes the development of part-of-speech tagging resources for the Georgian language, consisting of i.) a new morphosyntactic language model for part-of-speech (POS) tagging purposes; ii.) tagging guidelines for tagging and post-editing; iii.) the KATAG tagset and iv.) the trained parameter files the probabilistic TreeTagger program needs to work on Georgian texts. A new morphosyntactic model of Georgian for part-of-speech tagging purposes is described in the thesis. The thesis also describes a tagset (KATAG) defined in accordance with a new morphosyntactic model of the language and a set of design principles and tagging guidelines. A stochastic methodology is used here to perform tagging in Georgian. Namely, the Treetagger - a probabilistic part-of-speech tagging program has been trained on Georgian texts. The justification for this choice is discussed. I use two tokenisation approaches in part-of-speech tagging. An accuracy of 92.41% using an enclitic tokenisation approach and accuracy of 87.13% was achieved using a non-enclitic tokenisation approach, corroborating my hypothesis that treating enclitic elements separately from the host words results in better tagging performance. To make the tagger program easily adaptable for a range of inputs (type, variety or genre of text), the performance of the probabilistic TreeTagger program was evaluated according to the obtained test set consisting of five different genres such as academic, informal, legal, fiction and news.

The PhD thesis is available at White Rose eTheses Online here: https://etheses.whiterose.ac.uk/25313/ 

This repository contains TreeTagger tagging files for Georgian, trained TreeTagger parameter files, tagging lexicon, KATAG tagset for POS-tagging
